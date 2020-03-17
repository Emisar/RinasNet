from aiohttp import web

from settings import SETTINGS
from application.modules.db.DB import DB
from application.modules.neyron.Neyron import Neyron
from application.router.Router import Router


db = DB(SETTINGS['DB'])
neyron = Neyron(SETTINGS['NEYRON'])
app = web.Application()

Router(app, web, neyron)

async def on_startup(app):
    print('Запустился!!')

async def on_shutdown(app):
    print('Умер')

async def on_cleanup(app):
    print('Очистился')

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)
app.on_cleanup.append(on_cleanup)

web.run_app(app)