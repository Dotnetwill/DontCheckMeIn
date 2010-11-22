import logging
import formencode
import datetime

from sqlalchemy.orm.exc import NoResultFound
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from dontcheckmein.lib.base import BaseController, render
from dontcheckmein import model
from dontcheckmein.lib.taghelpers import GetTagList

log = logging.getLogger(__name__)
class UniqueNiceUrl(formencode.validators.String):
    def _to_python(self, value, c):
        url_count = model.Session.query(model.objects.IgnoreFile.id).filter(model.objects.IgnoreFile.nice_url == value).count()
        if url_count > 0:
            raise formencode.validators.Invalid('Sorry %s is already taken' % \
                                                value, value, c)
                                                
        return formencode.validators.String._to_python(self, value, c)

class IgnorefileForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True

    submitter = formencode.validators.NotEmpty()
    content = formencode.validators.NotEmpty()
    title = formencode.validators.NotEmpty()
    desc = formencode.validators.NotEmpty()
    niceurl = UniqueNiceUrl()
    tags = formencode.ForEach(formencode.validators.String())

class IgnorefileController(BaseController):

    def add(self):
        """ Displays the standard form"""
        c.tags =  model.Session.query(model.objects.Tag).all()
                             
        return render('/ignorefile/add.html')

    @validate(IgnorefileForm(), form='add')
    def add_processing(self):
        if request.method == 'POST':
            new_ignore = model.objects.IgnoreFile()
            new_ignore.title = self.form_result['title']
            new_ignore.content = self.form_result['content']
            new_ignore.desc = self.form_result['desc']
            new_ignore.submitted_by = self.form_result['submitter']
            new_ignore.nice_url = self.form_result['niceurl']
            new_ignore.submitted_date = datetime.datetime.now()
            new_ignore.views = 0
            new_ignore.rating = 0
            new_ignore.tags = GetTagList(self.form_result['tags'])
            
            model.Session.add(new_ignore)
            model.Session.commit()
          
            redirect("/ignorefile/view/%d" % new_ignore.id)

    def view_by_niceurl(self, nice_url=None):
        if(nice_url == None):
            abort(404, 'Sorry not mapped to an ignore file')
        
        try:
             c.ignore_file = model.Session.query(model.objects.IgnoreFile).filter(model.objects.IgnoreFile.nice_url == nice_url).one()
             
             c.ignore_file.views = c.ignore_file + 1
             model.Session.commit()
        except NoResultFound:
            abory(404, 'Sorry not mapped to an ignore file')
            
        return render('/ignorefile/view.html')
    
    def view(self, id=None):
        if id == None:
            abort(404, 'ignore file not found')
            
        c.ignore_file = self._get_ignore_by_id(id)
        
        c.ignore_file.views = c.ignore_file.views + 1
        model.Session.commit()
        
        return render('/ignorefile/view.html')

    def download(self, id=None):
        if id == None:
            abort(404, 'Not found')
        
        ignore_file = self._get_ignore_by_id(id)
        
        response.content_type = 'text/plain'
        response.content_disposition = 'attachment; filename=' + self._get_filename(ignore_file) + '.ignore'
                 
        return ignore_file.content 

    def _get_ignore_by_id(self, id):
        try:
             return model.Session.query(model.objects.IgnoreFile).filter(model.objects.IgnoreFile.id == id).one()
        except NoResultFound:
            abort(404, 'Not found')
            
    def _get_filename(self, ignore_file):
        return "_".join([tag.tag for tag in ignore_file.tags])
    
