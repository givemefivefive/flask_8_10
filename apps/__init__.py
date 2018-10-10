from flask import Flask
from flask_cors import CORS

from apps.ext import init_ext
from apps.urls import init_api

app = Flask(__name__,template_folder='../static',static_folder='../static',static_url_path='')

#
#
app.debug = True

CORS(app, supports_credentials=True)


def create_app():
    init_api(app)
    init_ext(app)

    return app