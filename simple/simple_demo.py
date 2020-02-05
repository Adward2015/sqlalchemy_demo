# -*- coding: utf-8 -*-
"""
通过SqlAlchemy反向映射表
进行增删改查
"""
from model.models import User
from simple.config import sql_db
from utils import session_scope

def simple_show():
    with session_scope(sql_db.session()) as session:
        # 清表
        session.query(User).delete()
        # 增
        dic1 = {"name": "Adward", "age": 18}
        dic2 = {"name": "Dragon", "age": 18}
        session.add(User(**dic1))
        session.add(User(**dic2))
        # 删
        session.query(User).filter(User.name == "Dragon").delete()
        # 改
        session.query(User).filter(User.name == "Adward").update({"age": 17})
        # 查
        result = session.query(User).all()
        print([each.__dict__ for each in result if each.__dict__.pop("_sa_instance_state")])


if __name__ == '__main__':
    simple_show()
