# -*- coding:utf-8 -*-

from sanic import Blueprint
from sanic.request import Request
from sanic.response import json
from sanic.views import HTTPMethodView

guomei_blueprint = Blueprint('guomei')

class GoldData(HTTPMethodView):
    def __init__(self):
        super(GoldData, self).__init__()
        @staticmethod
        async def options(request: Request, app_id: int):
            return text('', headers={
                'Access-Control-Allow-Methods': 'GET,PUT,DELETE,OPTIONS',
                'Access-Control-Max-Age:': '62400',
            })


    @staticmethod
    async def get(request: Request):
        return json({'guomeihuangjin':'11223344'})

guomei_blueprint.add_route(GoldData.as_view(), '/guomei/gold')
        