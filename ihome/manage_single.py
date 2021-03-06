# -- coding: utf-8 --

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

import redis


# 创建flask的应用对象
app = Flask(__name__)


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
    SESSION_TYPE = "redis"  # 使用缓存类型为redis
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 指定缓存实例
    SESSION_USE_SIGNER = True  # 对cookies中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期，单位：秒


# 导入配置文件
app.config.from_object(Config)

# 数据库
db = SQLAlchemy(app)

# 创建redis链接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 利用flask-session,将session数据保存到redis中
Session(app)

# 为flask补充csrf防护
CSRFProtect(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    app.run()
