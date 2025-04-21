import json
from typing import Union

import docker
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

client = docker.from_env()

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


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
    name: str
    new_name: str
    image: str


class DeleteContainer(BaseModel):
    id: str


@app.get("/containers")
def get_containers(query: str | None = None):
    try:
        containers = client.containers.list(all=True)
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
        client.containers.run(image=container.image, name=container.name, detach=True)
        print("cook")
        return Response(status_code=200)
    except NameError:
        return Response(status_code=500)


@app.put("/container")
def update_container(container: UpdateContainer):
    update = client.containers.get(container.name)
    update.rename(container.new_name)
    update.restart()
    print("update container")


@app.delete("/container")
def delete_container(container: DeleteContainer):
    try:
        response = client.containers.get(container.id)
        response.stop()
        response.remove()
        return Response(status_code=200)
    except NameError:
        print(NameError)
        return Response(status_code=500)
