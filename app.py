import argparse
import logging.config
from aiohttp import web, log
from application.handlers import app


parser = argparse.ArgumentParser(description="aiohttp framework")
# parser.add_argument('--host')
# parser.add_argument('--port')

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app)
