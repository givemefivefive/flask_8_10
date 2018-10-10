import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from apps.ext import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    expire_date = db.Column(db.DateTime, default=datetime.datetime.now())
    is_vip = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    passwd = db.Column(db.String(128))
    is_manager = db.Column(db.Boolean, default=False)  # 是否管理员

    @property
    def password(self):
        return self.passwd

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            # 对密码进行加密
            self.passwd = generate_password_hash(password)
        else:
            raise Exception('密码不符合规范')

    def verify_password(self, password):
        return check_password_hash(self.passwd, password)


class Vipcode(db.Model):
    __tablename__ = 't_vipcode'
    id = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.String(32))
    is_use = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    expire_date = db.Column(db.DateTime, default=datetime.datetime.now())
