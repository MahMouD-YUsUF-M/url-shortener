import pytest


@pytest.fixture(scope="session", autouse=True)
def engine_url_shortener():
    import liburl_shortener

    engine = liburl_shortener.data.engine_url_shortener
    assert engine.url.database == f'url_shortener'

    liburl_shortener.data.models.tables.create_all()

    return engine


@pytest.fixture(scope="session")
def data_url_shortener(engine_url_shortener):
    pass


@pytest.fixture(scope="session", autouse=True)
def app_url_shortener(data_url_shortener):
    from fastapi.testclient import TestClient
    from appurl_shortener.web import app

    return TestClient(app)
