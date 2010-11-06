# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1288999574.734832
_template_filename='/Users/Will/Dropbox/src/DontCheckMe.In/dontcheckmein/templates/ignorefile/add.html'
_template_uri='/ignorefile/add.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n<div class="content">\n    ')
        # SOURCE LINE 5
        __M_writer(escape(h.form(url(controller='ignorefile',action='Add_processing'))))
        __M_writer(u'\n      <label>Your name: ')
        # SOURCE LINE 6
        __M_writer(escape(h.text('submitter', value='anon', maxlength=100)))
        __M_writer(u'</label> <br />\n      <label>Title: ')
        # SOURCE LINE 7
        __M_writer(escape(h.text('title', maxlength=135)))
        __M_writer(u'</label> <br />\n      <label>Description: ')
        # SOURCE LINE 8
        __M_writer(escape(h.text('desc')))
        __M_writer(u'</label> <br />\n      <label>Content: ')
        # SOURCE LINE 9
        __M_writer(escape(h.textarea('content')))
        __M_writer(u'</label> <br />\n      ')
        # SOURCE LINE 10
        __M_writer(escape(h.submit('submit','submit')))
        __M_writer(u' <br />\n    ')
        # SOURCE LINE 11
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


