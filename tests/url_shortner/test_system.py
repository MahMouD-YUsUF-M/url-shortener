def test_health_check(app_urlshortner):
    response = app_urlshortner.get('/hc')
    assert response.status_code == 200
    assert response.json()['success'] == True
