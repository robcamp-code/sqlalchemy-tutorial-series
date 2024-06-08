""" models.py """
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date, Float
from sqlalchemy.orm import Relationship
from sqlalchemy.orm import declarative_base
from main import session

Model = declarative_base()
Model.query = session.query_property()


class User(Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, default=datetime.now())
    last_updated = Column(DateTime, onupdate=datetime.now())
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    # uselist ensures you get a single value when querying instead of a list, which would be the case for on to many relatiohsips
    author_profile = Relationship("AuthorProfile", 
                                  back_populates="user", 
                                  passive_deletes=True, 
                                  uselist=False)


class AuthorProfile(Model):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # unique forces one to one relationship
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'), unique=True, nullable=True)
    display_name = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    
    user = Relationship("User", back_populates="author_profile")
    # many to many with blog
    blogs = Relationship("Blog",
                         secondary="blog_author",
                         passive_deletes=True,
                         back_populates="authors"
                        )


class BlogAuthor(Model):
    __tablename__ = "blog_author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_profile_id = Column(Integer, ForeignKey("author.id", ondelete='CASCADE'), nullable=True)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=True)


class Blog(Model):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    created_at = Column(DateTime, default=datetime.now())
    last_updated = Column(DateTime, onupdate=datetime.now())
    authors = Relationship("AuthorProfile",
                         secondary="blog_author",
                         passive_deletes=True,
                         back_populates="blogs")
    title = Column(String, nullable=False)
    tagline = Column(String, nullable=True)
    content = Column(String, nullable=False)
    comments = Relationship("Comment")


class Comment(Model):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_id = Column(Integer, ForeignKey("blog.id", ondelete='CASCADE'), nullable=True)
    text = Column(String, nullable=False)
    blog = Relationship("Blog",
                         passive_deletes=True,
                         back_populates="comments",
                         uselist=False)