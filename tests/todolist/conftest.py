import pytest


@pytest.fixture(scope="session", autouse=True)
def engine_urlshortner():
    import liburlshortner

    engine = liburlshortner.data.engine_urlshortner
    assert engine.url.database == f'urlshortner'

    liburlshortner.data.models.tables.create_all()

    return engine


@pytest.fixture(scope="session")
def data_urlshortner(engine_urlshortner):
    pass


@pytest.fixture(scope="session", autouse=True)
def app_urlshortner(data_urlshortner):
    from fastapi.testclient import TestClient
    from appurlshortner.web import app

    return TestClient(app)
