# -*- coding: utf-8 -*-
from contextlib import contextmanager

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


@contextmanager
def session_scope(session):
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()


class SessionByLink(object):
    def __init__(self, link: str):
        self.link = link
        self.engine = create_engine(self.link)
        self.metadata = MetaData(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def table(self, table_name):
        __table__ = Table(table_name, self.metadata, autoload=True)  # 自动加载表结构
        return __table__
