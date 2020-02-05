# -*- coding: utf-8 -*-
from simple.config import sql_db
from utils import Base


# 定义user表,user表里面只有两个字段,name和age
class User(Base):
    __table__ = sql_db.table("user")
    # 当表里面没有主键的时候,反向映射报错,指定一个主键
    __mapper_args__ = {
        'primary_key': [sql_db.table("user").c.name]
    }
