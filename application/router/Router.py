import random
'''
from application.game.Game import Game
from application.db.DB import DB
from application.user.UserManager import UserManager
'''

class Router:
    def __init__(self, app, web, neyron):
        self.web = web
        self.neyron = neyron

        routers = [
            ('POST', '/api/getImg/', self.getImgHandler),
            ('*', '/', self.staticHandler)
        ]
        app.router.add_static('/js/', path=str('./public/js/'))
        for route in routers:
            app.router.add_route(route[0], route[1], route[2])

    def staticHandler(self, request):
        return self.web.FileResponse('./public/index.html')

    """ Войти в систему """
    async def getImgHandler(self, request):
        data = await request.post()
        img = data.get('img')
        result = self.neyron.toPrediction(img)
        return self.answer(result, 'Ошибка!')
    
    def answer(self, data, error):
        if data:
            return self.good(data)
        else:
            return self.bad(error)

    def good(self, data):
        return self.web.json_response({
            'result': 'ok',
            'data': data
        })

    def bad(self, error):
        return self.web.json_response({
            'result': 'error',
            'data': error
        })