import pytest


@pytest.fixture(scope="session", autouse=True)
def engine_urlurl_shortener():
    import liburlurl_shortener

    engine = liburlurl_shortener.data.engine_urlurl_shortener
    assert engine.url.database == f'urlurl_shortener'

    liburlurl_shortener.data.models.tables.create_all()

    return engine


@pytest.fixture(scope="session")
def data_urlurl_shortener(engine_urlurl_shortener):
    pass


@pytest.fixture(scope="session", autouse=True)
def app_urlurl_shortener(data_urlurl_shortener):
    from fastapi.testclient import TestClient
    from appurlurl_shortener.web import app

    return TestClient(app)
