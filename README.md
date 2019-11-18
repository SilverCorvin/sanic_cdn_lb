# Sanic-cdn-lb
## Configure
You can configure this application by modifying app.env file:

    CDN_A_ADDR - specify first cdn addr in FQDN format(for e.g. cdn-a.example.com)
    CDN_B_ADDR - specify second cdn addr in FQDN format(for e.g. cdn-b.example.com)
    CDN_A_WEIGHT - specify weight for the first cdn
    CDN_B_WEIGHT - specify weight for the second cdn
    ORIGIN_WEIGHT - specify weight for an origin
    USE_CACHE - 0|1 if used(by default) prepared redirect addr will be received form cache backend

## Run
To run this app:
    
    $ make 

Webapp will be available on 0.0.0.0:8000 by default

### Test
To run tests:
    
    $ make test

### Lint
To run linter:
    
    $ make lint
