import datetime

from flask_caching import Cache
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    init_db(app)
    init_login(app)
    # Config()
    # init_cache(app)


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask10'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '123456'
    db.init_app(app)
    migrate.init_app(app, db)

# 用户系统
login_manager=LoginManager()

def init_login(app):
    # login_manager.login_view=''     # 表示当用户没有登陆,自动跳转到登陆界面,相当于django的login_url
    login_manager.session_protection='strong' # basic strong None,安全强度,默认basic
    login_manager.login_message='登陆之后才能访问'
    login_manager.init_app(app)

# class Config():
#     SECRET_KEY = '123'
#     SESSION_TYPE='redis'    # session存储到redis
#     PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=10)  # 设置过期时间为10天,默认是浏览器关闭后session自动过期
#     REMEMBER_COOKIE_DURATION=datetime.timedelta(days=10)    # 设置cookie过期时间,默认为365天
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#
# cache = Cache()
#
#
# def init_cache(app):
#     cache_config = {
#         'CACHE_DEFAULT_TIMEOUT': 60,  # 默认的过期时间 单位秒
#         'CACHE_TYPE': 'redis',  # 缓存类型
#         'CACHE_REDIS_HOST': '127.0.0.1',  # IP地址
#         'CACHE_REDIS_PORT': 6379,  # 端口
#         'CACHE_REDIS_PASSWORD': 123456,  # 密码
#         'CACHE_REDIS_DB': 1,  # 连接数据库的编号
#         'CACHE_KEY_PREFIX': 'view_'  # 缓存key的前缀
#     }
#     cache.init_app(app, cache_config)