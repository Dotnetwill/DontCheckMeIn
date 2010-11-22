import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from sqlalchemy.sql.expression import desc 
from dontcheckmein.lib.base import BaseController, render
from dontcheckmein import model

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index(self):
        c.ignore_list = model.Session.query(model.objects.IgnoreFile).order_by(desc(model.objects.IgnoreFile.submitted_date))[0:5]
        
        return render('home.html')

    def get_by_views(self):
        c.ignore_list = model.Session.query(model.objects.IgnoreFile).order_by(desc(model.objects.IgnoreFile.views))[0:5]
        
        return render('res.html')
    
    def get_by_latest(self):
        c.ignore_list = model.Session.query(model.objects.IgnoreFile).order_by(desc(model.objects.IgnoreFile.submitted_date))[0:5]
        
        return render('res.html')