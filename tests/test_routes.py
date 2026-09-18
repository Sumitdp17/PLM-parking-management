from run import create_app


def test_route_health():
    app = create_app()
    client = app.test_client()
    for route in ["/auth/login", "/entry/", "/exit/", "/dashboard/"]:
        res = client.get(route)
        assert res.status_code == 200
