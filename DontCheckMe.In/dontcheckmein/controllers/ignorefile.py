import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dontcheckmein.lib.base import BaseController, render

log = logging.getLogger(__name__)

class IgnorefileController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/ignorefile.mako')
        # or, return a string
        return 'Hello World'
        
    def Add(self):
        """ Displays the standard form"""
        return render('/ignorefile/add.html')

    def Add_processing(self):
	return "processed it bitch tits"


    def Search(self):
      pass
