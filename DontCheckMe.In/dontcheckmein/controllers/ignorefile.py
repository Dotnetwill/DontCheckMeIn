import logging
import formencode
import datetime

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from dontcheckmein.lib.base import BaseController, render
from dontcheckmein import model

log = logging.getLogger(__name__)

class IgnorefileForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True

    submitter = formencode.validators.NotEmpty()
    content = formencode.validators.NotEmpty()

class IgnorefileController(BaseController):

    def index(self):
        c.ignore_list=model.Session.Query(model.objects.Ignorefile).order_by(model.objects.Ignorefile.submitted_date)[0:5]
        return render('/ignorefile/latest.html')
    
    def Add(self):
        """ Displays the standard form"""
        return render('/ignorefile/add.html')

    @validate(IgnorefileForm(), form='Add')
    def Add_processing(self):
        if request.method == 'POST':
            new_ignore = model.objects.IgnoreFile()
            new_ignore.content = self.form_result['content']
            new_ignore.submitted_by = self.form_result['submitter']
            new_ignore.submitted_date = datetime.datetime.now()
            
            model.Session.add(new_ignore)
            model.Session.commit()
            
            redirect("/Ignorefile/Success")

    def Success(self):
        return 'did it bitches'

    def Search(self):
        pass
