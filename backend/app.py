import hashlib

import docker
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gitapi import *
from tunnel import *

client = docker.from_env()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def hash_name(name: str):
    hashed_object = hashlib.sha256(name.encode())
    hashed_name = hashed_object.hexdigest()
    hashed_name = "mangomongo" + "-" + name
    return hashed_name


class Info(BaseModel):
    status: str


class Container(BaseModel):
    id: str
    name: str
    image: str
    info: Info


class CreateContainer(BaseModel):
    name: str
    image: str
    github: str
    enable_github: bool


class UpdateContainer(BaseModel):
    id: str
    new_name: str
    image: str
    update_image: bool


class DeleteContainer(BaseModel):
    id: str


@app.get("/containers")
def get_containers(query: str | None = None):
    try:
        containers = client.containers.list(all=True)
        if len(containers) == 0:
            return []

        response = []
        for container in containers:
            print(container.name)
            contain = Container(
                id=container.id,
                name=container.name,
                image=container.image.attrs["RepoTags"][0],
                info=Info(status=container.status),
            )
            response.append(contain)
        return response
    except NameError:
        print(NameError)
        return Response(status_code=500)


@app.get("/container_info")
def get_container_info():
    try:
        containers = client.containers.list(all=True)
        networks = client.networks.list()
        images = client.images.list()

        container_amount = len(containers)
        network_amount = len(networks)
        image_amount = len(images)

        response = {
            "containers": container_amount,
            "networks": network_amount,
            "images": image_amount,
        }
        return response
    except:
        return Response(status_code=500)


@app.post("/containers")
def create_container(container: CreateContainer):
    try:
        if container.github:
            build_repository(container.name, container.github)
            return

        if container.name == "" or container.image == "":
            return

        hashed_name = hash_name(container.name)
        labels = [
            "traefik.enable=true",
            f"traefik.http.routers.{hashed_name}-http.rule=Host('{hashed_name}.home.tysonjenkins.dev')",
            "traefik.http.routers.{hashed_name}-http.entrypoints=web",
            "traefik.http.routers.{hashed_name}-https.tls=true",
            "traefik.http.routers.{hashed_name}-https.tls.certresolver=cloudflare",
            "traefik.http.routers.{hashed_name}-https.entrypoints=websecure",
            f"traefik.http.routers.{hashed_name}-https.rule=Host('{hashed_name}.home.tysonjenkins.dev') || Host('{hashed_name}.tysonjenkins.dev')",
        ]
        client.containers.run(
            image=container.image, name=hashed_name, detach=True, labels=labels
        )
        create_public_url(hashed_name)
        return Response(status_code=200)
    except NameError:
        return Response(status_code=500)


@app.put("/container")
def update_container(container: UpdateContainer):
    try:
        if container.new_name == "" and container.image == "":
            return

        data = client.containers.get(container.id)
        image = data.image
        print(data.image.attrs["RepoTags"][0])

        if container.update_image == True:
            client.images.pull(repository=data.image.attrs["RepoTags"][0], tag="latest")

        if data.name and image is not None:
            hashed_name = hash_name(container.new_name)
            data.stop()
            data.remove()
            labels = [
                "traefik.enable=true",
                f"traefik.http.routers.{hashed_name}-http.rule=Host('{hashed_name}.home.tysonjenkins.dev')",
                "traefik.http.routers.{hashed_name}-http.entrypoints=web",
                "traefik.http.routers.{hashed_name}-https.tls=true",
                "traefik.http.routers.{hashed_name}-https.tls.certresolver=cloudflare",
                "traefik.http.routers.{hashed_name}-https.entrypoints=websecure",
                f"traefik.http.routers.{hashed_name}-https.rule=Host('{hashed_name}.home.tysonjenkins.dev') || Host('{hashed_name}.tysonjenkins.dev')",
            ]
            client.containers.run(
                image=image, name=hashed_name, detach=True, labels=labels
            )
            update_public_url(hashed_name, data.name)
        return Response(status_code=200)
    except NameError:
        return Response(status_code=500)


@app.delete("/container")
def delete_container(container: DeleteContainer):
    try:
        data = client.containers.get(container.id)
        data.stop()
        data.remove()
        delete_public_url(data.name)
        return Response(status_code=200)
    except NameError:
        print(NameError)
        return Response(status_code=500)
