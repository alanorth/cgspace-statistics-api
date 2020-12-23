from falcon import testing
import pytest

from dspace_statistics_api.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_get_docs(client):
    """Test requesting the documentation at the root."""

    response = client.simulate_get("/")

    assert isinstance(response.content, bytes)
    assert response.status_code == 200


def test_get_openapi_json(client):
    """Test requesting the OpenAPI JSON schema."""

    response = client.simulate_get("/docs/openapi.json")

    assert isinstance(response.content, bytes)
    assert response.status_code == 200


def test_get_swagger_ui(client):
    """Test requesting the Swagger UI."""

    response = client.simulate_get("/swagger")

    assert isinstance(response.content, bytes)
    assert response.status_code == 200


def test_get_status(client):
    """Test requesting the status page."""

    response = client.simulate_get("/status")

    assert isinstance(response.content, bytes)
    assert response.status_code == 200