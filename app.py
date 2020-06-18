import argparse
import logging.config
from aiohttp import web, log
from application.handlers import app


parser = argparse.ArgumentParser(description="aiohttp framework")
parser.add_argument('--path', default='0.0.0.0')
parser.add_argument('--port', default="8080")

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, host=args.path, port=args.port, access_log_format="{'status': '%s'}")
