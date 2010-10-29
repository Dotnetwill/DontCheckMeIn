# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1288353761.716171
_template_filename='/home/will/Dropbox/src/DontCheckMe.In/dontcheckmein/templates/ignorefile/add.html'
_template_uri='/ignorefile/add.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n  <head>\n  </head>\n  <body>\n    ')
        # SOURCE LINE 5
        __M_writer(escape(h.form(url(controller='ignorefile',action='Add_processing'))))
        __M_writer(u'\n      <label>Your name: ')
        # SOURCE LINE 6
        __M_writer(escape(h.text('submitter')))
        __M_writer(u'</label> <br />\n      <label>Content: ')
        # SOURCE LINE 7
        __M_writer(escape(h.textarea('content')))
        __M_writer(u'</label> <br />\n      ')
        # SOURCE LINE 8
        __M_writer(escape(h.submit('submit','submit')))
        __M_writer(u' <br />\n    ')
        # SOURCE LINE 9
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


