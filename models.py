from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

import sys

db = SQLAlchemy()

# 用户表
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# 热点数据表
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    hot_value = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    fetched_at = db.Column(db.DateTime, server_default=db.func.now())