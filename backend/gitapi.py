import os
import shutil

import docker
import git

client = docker.from_env()


def get_repository(url_repo: str):
    directory_name = url_repo.split("/")[4].split(".")[0]
    git.Repo.clone_from(url_repo, f"/tmp/repositories/{directory_name}")
    return directory_name


def build(repo, container_name):
    client.images.build(
        path=f"/tmp/repositories/{repo}/frontend",
        tag=f"mangomongo-{container_name}-frontend:latest".lower(),
    )

    client.images.build(
        path=f"/tmp/repositories/{repo}/backend",
        tag=f"mangomongo-{container_name}-backend:latest".lower(),
    )

    client.containers.run(
        name=f"mango-mongo-{container_name}-frontend",
        image=f"mangomongo-{container_name}-frontend:latest",
        detach=True,
    )

    client.containers.run(
        name=f"mango-mongo-{container_name}-backend",
        image=f"mangomongo-{container_name}-backend:latest",
        detach=True,
    )


def build_repository(container_name, repo_url):
    repo = get_repository(repo_url)
    build(repo, container_name)
