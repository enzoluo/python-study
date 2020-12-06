from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

Base = declarative_base()


# 创建单表
class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(32))
    age = Column(INTEGER)
    birth_day = Column(VARCHAR(32))


# # 一对多
# class Favor(Base):
# __tablename__ = 'favor'
# nid = Column(Integer, primary_key=True)
# caption = Column(String(50), default='red', unique=True)

# class Person(Base):
# __tablename__ = 'person'
# nid = Column(Integer, primary_key=True)
# name = Column(String(32), index=True, nullable=True)
# favor_id = Column(Integer, ForeignKey("favor.nid"))

# # 多对多
# class ServerToGroup(Base):
# __tablename__ = 'servertogroup'
# nid = Column(Integer, primary_key=True, autoincrement=True)
# server_id = Column(Integer, ForeignKey('server.id'))
# group_id = Column(Integer, ForeignKey('group.id'))

# class Group(Base):
# __tablename__ = 'group'
# id = Column(Integer, primary_key=True)
# name = Column(String(64), unique=True, nullable=False)

# class Server(Base):
# __tablename__ = 'server'

# id = Column(Integer, primary_key=True, autoincrement=True)
# hostname = Column(String(64), unique=True, nullable=False)
# port = Column(Integer, default=22)

# Base.metadata.create_all(engine)  #创建表
# # Base.metadata.drop_all(engine)   #删除表