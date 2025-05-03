import hashlib

import docker
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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


class UpdateContainer(BaseModel):
    id: str
    new_name: str
    image: str


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
        if container.name == "" or container.image == "":
            return

        hashed_name = hash_name(container.name)
        create_public_url(hashed_name)
        client.containers.run(image=container.image, name=hashed_name, detach=True)
        return Response(status_code=200)
    except NameError:
        return Response(status_code=500)


@app.put("/container")
def update_container(container: UpdateContainer):
    try:
        if container.new_name == "" and container.image == "":
            return

        data = client.containers.get(container.id)

        if data.name is not None:
            hashed_name = hash_name(data.name)
            update_public_url(hashed_name, data.name)

            data.rename(hashed_name)
            data.restart()
        return Response(status_code=200)
    except NameError:
        return Response(status_code=500)


@app.delete("/container")
def delete_container(container: DeleteContainer):
    try:
        data = client.containers.get(container.id)
        delete_public_url(data.name)
        data.stop()
        data.remove()
        return Response(status_code=200)
    except NameError:
        print(NameError)
        return Response(status_code=500)
