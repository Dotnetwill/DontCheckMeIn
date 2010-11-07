from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.orm import relation, backref

from dontcheckmein.model.meta import Base

ignorefile_tags = Table('ignorefile_tags', Base.metadata,
    Column('ignorefile_id', Integer, ForeignKey('ignorefile.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')))

class IgnoreFile(Base):
    __tablename__ = "ignorefile"

    id = Column(Integer, primary_key=True)
    submitted_by = Column(Unicode(50))
    submitted_date = Column(DateTime)
    title = Column(Unicode(130))
    desc = Column(Unicode)
    content = Column(Unicode)
    nice_url = Column(Unicode(25))

    # many to many ignore file<->tag
    tags = relation('Tag', secondary=ignorefile_tags, backref='tags')
    
    def __str__(self):
      return title

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    tag = Column(Unicode(130))
    desc = Column(Unicode)
    
    def __init__(self, tag):
        self.tag = tag
        self.desc = ''
    
    def __str__(self):
        return self.tag


