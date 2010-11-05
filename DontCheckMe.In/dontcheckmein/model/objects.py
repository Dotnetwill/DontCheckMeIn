from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from dontcheckmein.model.meta import Base

class IgnoreFile(Base):
    __tablename__ = "ignorefile"

    id = Column(Integer, primary_key=True)
    submitted_by = Column(Unicode(50))
    submitted_date = Column(DateTime)
    title = Column(Unicode(130))
    desc = Column(Unicode)
    content = Column(Unicode)
    
    def __str__(self):
      return title
	