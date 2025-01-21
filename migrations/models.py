# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, server_default=text("nextval('authors_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    active = Column(Boolean)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('posts_id_seq'::regclass)"))
    title = Column(String(50), nullable=False)
    content = Column(String(50), nullable=False)
    author_id = Column(ForeignKey('authors.id'), nullable=False)
    date = Column(DateTime, nullable=False)

    author = relationship('Author')
