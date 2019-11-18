from sanic import Sanic
from sanic.response import json, redirect
from sanic_redis_ext import RedisExtension

from conf import app as app_conf
from helpers import get_cdn_host, get_from_cache, prepare_cdn_addr, store_in_cache


app = Sanic()
app.config.from_object(app_conf)
RedisExtension(app)


@app.route("/")
async def handle(request):
    resource = request.args.get('video')
    if not resource:
        return json(
            {"error": "video parameter is required in get params"},
            status=400
        )

    cdn_host = get_cdn_host(request.app)
    if not cdn_host:
        return redirect(resource)

    if not request.app.config.USE_CACHE:
        return redirect(prepare_cdn_addr(resource, cdn_host))

    cached_value = await get_from_cache(request.app, resource, cdn_host)
    if cached_value:
        return redirect(cached_value)

    redirect_addr = await store_in_cache(request.app, resource, cdn_host)
    return redirect(redirect_addr)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
