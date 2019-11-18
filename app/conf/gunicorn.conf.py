import multiprocessing
import os


bind = os.getenv('APP_BIND_ADDR', '127.0.0.1:8000')

worker_class = 'sanic.worker.GunicornWorker'
workers = os.getenv('WORKERS', multiprocessing.cpu_count() * 2 + 1)
