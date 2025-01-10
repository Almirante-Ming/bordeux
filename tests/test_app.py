from http import HTTPStatus

from fastapi.testclient import TestClient

from bordeux import app

client = TestClient(app)


def test_read_root_return_ok():
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
