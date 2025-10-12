def test_health_check(app_urlurl_shortener):
    response = app_urlurl_shortener.get('/hc')
    assert response.status_code == 200
    assert response.json()['success'] == True
