from sqlalchemy.orm.exc import NoResultFound

from dontcheckmein.model.objects import Tag
from dontcheckmein import model

def GetTagList(tag_string = None):
    taglist = []
    for tag in tag_string:
        try:
            taglist.append(model.Session.query(Tag).filter(Tag.tag == tag).one())
        except NoResultFound:
            taglist.append(Tag(tag))
            
    return taglist