# -- coding: utf-8 --

import redis


class Config(object):
    """配置信息"""

    # session加密信息
    SECRET_KEY = "NXSAONFS374543ndosnv#%$?"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:admin123@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookies中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期，单位：秒


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develope": DevelopmentConfig,
    "product": ProductConfig,
}