from aiohttp import web
from pathlib import Path
from pkgutil import iter_modules
from importlib import import_module
from application.middlewares import request_middlware
from aiohttp.web_middlewares import normalize_path_middleware



app = web.Application(middlewares=[request_middlware])

# add each handlers as subapp
package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")
    subapp = getattr(module, 'app')
    app.add_subapp(module.root_path, subapp)
