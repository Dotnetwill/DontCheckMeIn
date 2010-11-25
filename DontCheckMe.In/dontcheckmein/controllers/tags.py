import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dontcheckmein.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TagsController(BaseController):

    def index(self):
        return render('explore_tag.html')
    
    def filter_by_tags(self, tags):
        pass
