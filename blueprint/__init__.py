# -*- coding: utf-8 -*-

from sanic import Sanic
from .guomei_gold import *

def manage_app():
	app = Sanic(__name__)
	app.register_blueprint(guomei_blueprint)

	app.run(host='0.0.0.0', port=8080, debug=True)