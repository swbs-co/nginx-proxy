import pytest


@pytest.mark.parametrize("http_method,expected_code", [
    ("GET", 301),
    ("HEAD", 308),
    ("POST", 308),
    ("PUT", 308),
    ("PATCH", 308),
    ("DELETE", 308),
    ("OPTIONS", 308),
    ("CONNECT", 308),
    ("TRACE", 308),
])
def test_default_redirect_by_method(
    docker_compose,
    nginxproxy,
    http_method: str,
    expected_code: int,
):
    r = nginxproxy.request(
        method=http_method,
        url='http://nginx-proxy.tld',
        allow_redirects=False,
    )
    assert r.status_code == expected_code
    assert r.headers['Location'] == 'https://nginx-proxy.tld/'
