from flask_restful import Resource, fields, marshal_with, reqparse

from apps.movies.models import Img, Film, Catalog, Res, Loc, Decade, Subclass

banners = {
    'img_url': fields.String,
}

films = {
    'id': fields.String,  # ID
    'cata_log_name': fields.String,  # 类型 动画 电影
    'actor': fields.String,  # 演员
    'image': fields.String,  # 图片地址,相对路径
    'loc_name': fields.String,  # 国籍:美国
    'name': fields.String,  # 电影名
    'on_decade': fields.String,  # 上映时间
    'plot': fields.String,  # 介绍
    'update_time': fields.String,  # 更新时间
    'status': fields.String,  # 状态:全集?
    'sub_class_name': fields.String,  # 类型1:喜剧片
    'sub_class_id': fields.String,  # 喜剧片id
    'type_name': fields.String,  # 类型2:奇幻片
    'type_id': fields.String,  # 奇幻片id
    'evaluation': fields.String,  # 评分
}

catalogs = {                # 分类名称表
    'name': fields.String,  # 名字
    'isVip': fields.Integer,  # 是否vip专用
}

reses = {
    'link': fields.String,  # 下载链接
    'name': fields.String,  # 名称
}

loces = {
    'name': fields.String,  # 地区
}

decades = {
    'name': fields.String,  # 年代
}

subclasses = {
    'name': fields.String,  # 子类
}

data = {
    'banners': fields.List(fields.Nested(banners)),
    'films': fields.List(fields.Nested(films)),
    'catalogs': fields.List(fields.Nested(catalogs)),
    'reses': fields.List(fields.Nested(reses)),
    'loces': fields.List(fields.Nested(loces)),
    'decades': fields.List(fields.Nested(decades)),
    'subclasses': fields.List(fields.Nested(subclasses)),
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.String(default=200),
    'data': fields.Nested(data)
}

args_names = 'name'
args_order = 'order'
args_id = 'id'
args_sub_type = 'film_type_sub'
args_type_name = 'type_name'


class BannerApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(args_names, type=str, required=False)
        self.parser.add_argument(args_order, type=str, required=False)
        self.parser.add_argument(args_id, type=str, required=False)
        self.parser.add_argument(args_sub_type, type=str, required=False)
        self.parser.add_argument(args_type_name, type=str, required=False)

    @marshal_with(result)
    def get(self):
        args = self.parser.parse_args()
        name = args.get(args_names)
        id = args.get(args_id)
        order = args.get(args_order)
        sub_type = args.get(args_sub_type)
        type_name = args.get(args_type_name)

        banners = Img.query.all()
        catalogs = Catalog.query.filter(Catalog.is_use == 1).all()
        reses = Res.query.filter(Res.is_use == 1).filter(Res.film_id == id).all()
        loces = Loc.query.all()
        decades = Decade.query.all()

        # scores=[]
        # for film in Film.query.all():
        #     if film.raties:
        #         score_list=[]
        #         for scorees in film.raties:
        #             score_list.append(int(scorees.score))
        #         result = sum(score_list) // len(score_list)
        #         scores.append(result)
        #     else:
        #         scores.append(0)
        if id:
            films = Film.query.filter(Film.id == id).first()
            subclasses = Subclass.query.first()
        elif name:
            if name == '电影' or '电视剧' or '动漫' or '短视频':
                catalogs_id = Catalog.query.filter(Catalog.name == name).first().id
                subclasses = Subclass.query.filter(Subclass.catalog_id == catalogs_id).all()
                if order == '1':
                    films = Film.query.filter(Film.cata_log_name == name).order_by(Film.update_time.desc()).limit(
                        10)  # 降序,从大到小
                elif order == '0':
                    films = Film.query.filter(Film.cata_log_name == name).limit(12)
                else:
                    films = Film.query.filter(Film.cata_log_name == name).all()
            else:
                films = Film.query.filter(Film.name == name).first()
                subclasses = Subclass.query.first()
        elif sub_type:
            if type_name:
                films = Film.query.filter(Film.sub_class_name == sub_type).filter(Film.type_name == type_name).limit(8)
            else:
                films = Film.query.filter(Film.sub_class_name == sub_type).all()
            subclasses = Subclass.query.first()
        else:
            films = Film.query.first()
            subclasses = Subclass.query.first()
        data = {
            'banners': banners,
            'films': films,
            'catalogs': catalogs,
            'reses': reses,
            'loces': loces,
            'decades': decades,
            'subclasses': subclasses,
        }
        result = {'data': data}
        return result
