def test_health_check(app_urlshortener):
    response = app_urlshortener.get('/hc')
    assert response.status_code == 200
    assert response.json()['success'] == True
