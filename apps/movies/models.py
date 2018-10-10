from apps.ext import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(255))


class Film(db.Model):
    __tablename__ = 't_film'
    id = db.Column(db.String(255), primary_key=True)
    actor = db.Column(db.String(255))  # 演员
    cata_log_name = db.Column(db.String(255))  # 类型:电影
    cata_log_id = db.Column(db.String(255))  # 类型id
    evaluation = db.Column(db.String(255))  #
    image = db.Column(db.String(255))  # 图片地址,相对路径
    is_use = db.Column(db.Integer)  # 是否可用?
    loc_name = db.Column(db.String(255))  # 国籍:美国
    loc_id = db.Column(db.String(255))  # 国籍id
    name = db.Column(db.String(255))  # 电影名
    on_decade = db.Column(db.String(255))  # 上映时间
    plot = db.Column(db.Text)  # 介绍
    resolution = db.Column(db.String(255))  # 清晰度
    status = db.Column(db.String(255))  # 状态:全集?
    sub_class_name = db.Column(db.String(255))  # 类型1 喜剧片
    sub_class_id = db.Column(db.String(255))  # 类型id
    type_name = db.Column(db.String(255))  # 类型2:  奇幻片
    type_id = db.Column(db.String(255))  # 类型id
    update_time = db.Column(db.String(255))  # 更新时间
    is_vip = db.Column(db.Integer)  # 是否vip
    raties=db.relationship('Raty', backref='film')
    reses=db.relationship('Res', backref='film')


class Catalog(db.Model):  # 分类名称表
    __tablename__ = 't_catalog'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))
    sort = db.Column(db.Integer)  # 排序
    isVip = db.Column(db.Integer, default=0)


class Decade(db.Model):  # 年代表
    __tablename__ = 't_decade'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))
    sort = db.Column(db.Integer)  # 排序


class Level(db.Model):  # 优先级?
    __tablename__ = 't_level'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))


class Loc(db.Model):  # 电影来自哪个地方 国家?
    __tablename__ = 't_loc'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))


class Raty(db.Model):  # 评分 Film一对多 film子表
    __tablename__ = 't_raty'
    id = db.Column(db.String(255), primary_key=True)
    en_time = db.Column(db.String(255))
    film_id = db.Column(db.String(255), db.ForeignKey(Film.id))
    score = db.Column(db.String(32))



class Res(db.Model):  # 电影详情 film子表
    __tablename__ = 't_res'
    id = db.Column(db.String(255), primary_key=True)
    episodes = db.Column(db.Integer)  # 发作?
    is_use = db.Column(db.Integer)
    link = db.Column(db.Text)  # 下载链接
    link_type = db.Column(db.String(255))  # 链接类型
    name = db.Column(db.Text)  # 电影名称
    update_time = db.Column(db.String(255))  # 上传时间
    film_id = db.Column(db.String(255), db.ForeignKey(Film.id))  # film id


class Subclass(db.Model):  # 电影名称的类型 子表    动作 喜剧
    __tablename__ = 't_subclass'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))
    catalog_id = db.Column(db.String(255), db.ForeignKey(Catalog.id))


class Type(db.Model):  # 电影名称类型的 子类型  爱情 犯罪等
    __tablename__ = 't_type'
    id = db.Column(db.String(255), primary_key=True)
    is_use = db.Column(db.Integer)
    name = db.Column(db.String(32))
    subclass_id = db.Column(db.String(255), db.ForeignKey(Subclass.id))
