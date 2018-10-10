from flask_restful import Api
from apps.movies.apis import BannerApi
from apps.user.apis import UserApi

api = Api()			# 实例化一个api

api.add_resource(UserApi, '/user/')
api.add_resource(BannerApi,'/movie/')

def init_api(app):		# 注册api
    api.init_app(app)