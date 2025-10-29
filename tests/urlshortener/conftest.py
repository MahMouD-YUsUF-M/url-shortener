import pytest


@pytest.fixture(scope="session", autouse=True)
def engine_urlshortener():
    import liburlshortener

    engine = liburlshortener.data.engine_urlshortener
    assert engine.url.database == f'urlshortener'

    liburlshortener.data.models.tables.create_all()

    return engine


@pytest.fixture(scope="session")
def data_urlshortener(engine_urlshortener):
    pass


@pytest.fixture(scope="session", autouse=True)
def app_urlshortener(data_urlshortener):
    from fastapi.testclient import TestClient
    from appurlshortener.web import app

    return TestClient(app)
