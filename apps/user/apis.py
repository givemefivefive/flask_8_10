from flask_login import logout_user, login_user
from flask_restful import fields, Resource, reqparse, marshal_with

from apps.ext import db, login_manager
from apps.user.models import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
}

data = {
    'user': fields.Nested(user_fields)
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.List(fields.Nested(data))
}

arg_username = 'username'
arg_password = 'password'


class UserApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(arg_username, type=str, required=True, help=u'用户名不能为空')
        self.parser.add_argument(arg_password, type=str, required=True, help=u'密码不能为空')

    # 获取用户信息 登陆   查
    @marshal_with(result)
    def get(self):
        args = self.parser.parse_args()
        username = args.get(arg_username,'')
        password = args.get(arg_password,'')
        if username and password:
            user = User.query.filter(User.username == username).first()
            if user:
                if user.verify_password(password):
                    login_user(user, remember=True)
                    data = {'user': user}
                    result = {'data': data}
                    return result
                else:
                    return {'status': 404, 'msg': '账号密码错误'}
            else:
                return {'status': 404, 'msg': '账号不存在'}
        else:
            return {'status': 404, 'msg': '用户名密码不符合规范,请检查后重试'}

    # 注册    增
    @marshal_with(result)
    def post(self):
        args = self.parser.parse_args()
        username = args.get(arg_username,'')
        password = args.get(arg_password,'')
        if username and password:
            try:
                user = User()
                user.username = username
                user.passwd = password
                db.session.add(user)
                db.session.commit()
                data = {'user': user}
                result = {
                    'data': data
                }
                return result
            except:
                db.session.rollback()

    # 修改    改
    def put(self):
        pass

    # 登出,删除 删
    def delete(self):
        logout_user()  # 什么都不用传,直接登出
