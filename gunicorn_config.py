import os
import multiprocessing

worker_class = 'aiohttp.worker.GunicornWebWorker'
reload = bool(os.environ.get('GUNICORN_RELOAD', True))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')

sendfile = False
timeout = 6000
workers = int(os.environ.get('GUNICORN_WORKERS', '1'))
worker_connections = 1000
limit_request_line = 32000
limit_request_field_size = 32000

loglevel = (os.environ.get('GUNICORN_LOGLEVEL', 'info')).lower()
accesslog = '-'
access_log_format = ('''{"status_code": "%s", "requester_ip": "%a", "time": "%t", "content_type": "%{Content-Type}o"}, "Authorization": "%{Authorization}i"}''')
