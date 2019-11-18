from hashlib import sha256
from random import choices
from urllib.parse import urlparse, urlunparse


def get_cdn_host(app):
    cdn_servers = [app.config.CDN_A_ADDR, app.config.CDN_B_ADDR, None]
    weights = [
        app.config.CDN_A_WEIGHT,
        app.config.CDN_B_WEIGHT,
        app.config.ORIGIN_WEIGHT
    ]
    return choices(cdn_servers, weights=weights)[0]


def prepare_cdn_addr(payload, cdn_host):
    url = urlparse(payload)
    srv_name = url.hostname.split('.')[0]
    parts = (url.scheme, cdn_host, f'{srv_name}{url.path}', '', '', '')
    return urlunparse(parts)


def get_key(cdn_host, payload):
    m = sha256()
    m.update(cdn_host.encode())
    m.update(payload.encode())
    return m.hexdigest()


async def get_from_cache(app, payload, cdn_host):
    with await app.redis as redis:
        key = get_key(cdn_host, payload)
        return await redis.get(key)


async def store_in_cache(app, payload, cdn_host):
    with await app.redis as redis:
        addr = prepare_cdn_addr(payload, cdn_host)
        key = get_key(cdn_host, payload)
        await redis.set(key, addr)
        return addr
