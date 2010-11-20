import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sqlalchemy.orm.exc import NoResultFound

from dontcheckmein.lib.base import BaseController, render
from dontcheckmein import model
from dontcheckmein.model.objects import Tag

log = logging.getLogger(__name__)

class SearchController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/search.mako')
        # or, return a string
        return 'Hello World'
        
    def tag(self, tag=None):
        if tag == None:
            abort(404, "oh tits")
        
        try:
            c.cur_tag = model.Session.query(Tag).filter(Tag.tag == tag).one()
        except NoResultFound:
            abort(404, 'Tag not found, maybe this should be part of the page')
            
        return render('/search_results.html')
