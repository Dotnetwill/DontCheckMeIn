from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from dontcheckmein.model.meta import Base

class IgnoreFile_Tags(Base):
    __tablename__ = "ignorefile_tags"
    
    ignorefile_id = Column(Integer)
    tag_id = Column(Integer)
    

class IgnoreFile(Base):
    __tablename__ = "ignorefile"

    id = Column(Integer, primary_key=True)
    submitted_by = Column(Unicode(50))
    submitted_date = Column(DateTime)
    title = Column(Unicode(130))
    desc = Column(Unicode)
    content = Column(Unicode)
    nice_url = Column(Unicode(25))

    # many to many BlogPost<->Keyword
    tags = relation('tags', secondary=IgnoreFile_Tags, backref='Tag')
    
    def __str__(self):
      return title

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    tag = Column(Unicode(130))
    desc = Column(Unicode)

