from fastapi.testclient import TestClient

from app import app, client

app = TestClient(app)


def test_create_container():
    client.containers.run(image="ubuntu:latest", name="test")
    container = client.containers.get("test")

    assert container.name == "test"


def test_get_container():
    container = client.containers.get("test")
    assert container.name == "test"


def test_remove_container():
    container = client.containers.get("test")
    container.stop()
    container.remove()

    try:
        client.containers.get("test")
        assert False
    except:
        assert True
