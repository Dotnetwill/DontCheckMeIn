import logging
import formencode
import datetime

from sqlalchemy.orm.exc import NoResultFound
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from dontcheckmein.lib.base import BaseController, render
from dontcheckmein import model
from dontcheckmein.lib.taghelpers import GetTagListFromString

log = logging.getLogger(__name__)

class IgnorefileForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True

    submitter = formencode.validators.NotEmpty()
    content = formencode.validators.NotEmpty()
    title = formencode.validators.NotEmpty()
    desc = formencode.validators.NotEmpty()
    niceurl = formencode.validators.String()
    tags = formencode.validators.String()

class IgnorefileController(BaseController):

    def add(self):
        """ Displays the standard form"""
        return render('/ignorefile/add.html')

    @validate(IgnorefileForm(), form='Add')
    def add_processing(self):
        if request.method == 'POST':
            new_ignore = model.objects.IgnoreFile()
            new_ignore.title = self.form_result['title']
            new_ignore.content = self.form_result['content']
            new_ignore.desc = self.form_result['desc']
            new_ignore.submitted_by = self.form_result['submitter']
            new_ignore.nice_url = self.form_result['niceurl']
            new_ignore.submitted_date = datetime.datetime.now()
            
            new_ignore.tags = GetTagListFromString(self.form_result['tags'])
            
            model.Session.add(new_ignore)
            model.Session.commit()
            
            redirect("/Ignorefile/Success")

    def view(self, id=None):
        if id == None:
            abort(404, 'ignore file not found')
            
        try:
            c.ignore_file = model.Session.query(model.objects.IgnoreFile).filter(model.objects.IgnoreFile.id == id).order_by(model.objects.IgnoreFile.submitted_date).one()
        
            return render('/ignorefile/view.html')

        except NoResultFound:
            abort(404, 'Not found')

        
