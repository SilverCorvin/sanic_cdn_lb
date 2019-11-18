from hashlib import sha256
from unittest.mock import patch, MagicMock

from app.helpers import prepare_cdn_addr, get_key, get_cdn_host


def test_get_cdn_host():
    app = MagicMock()
    app.config.CDN_A_ADDR = 'cdn_a'
    app.config.CDN_B_ADDR = 'cdn_b'
    app.config.CDN_A_WEIGHT = 30
    app.config.CDN_B_WEIGHT = 10
    app.config.ORIGIN_WEIGHT = 1
    with patch('app.helpers.choices', lambda population, weights: [app.config.CDN_A_ADDR]):
        assert app.config.CDN_A_ADDR == get_cdn_host(app)


def test_prepare_cdn_addr():
    payload = 'http://s1.origin-cluster/some/1488/resource.m3u8'
    cdn_host = 'cdn_addr'
    expected = 'http://cdn_addr/s1/some/1488/resource.m3u8'
    assert expected == prepare_cdn_addr(payload, cdn_host)


def test_get_key():
    cdn_host = 'cdn_addr'
    payload = 'some_payload'
    m = sha256()
    m.update(cdn_host.encode())
    m.update(payload.encode())
    assert m.hexdigest() == get_key(cdn_host, payload)
