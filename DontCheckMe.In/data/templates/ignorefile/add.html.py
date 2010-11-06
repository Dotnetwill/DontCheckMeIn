# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1289082746.7464931
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
        __M_writer(u'\n\n<div class="content">\n    <h2>Add Ignore File</h2>\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.form(url(controller='ignorefile',action='Add_processing'))))
        __M_writer(u'\n      <label for="title">Title</label><br />  ')
        # SOURCE LINE 7
        __M_writer(escape(h.text('title', maxlength=135, class_='form-textbox')))
        __M_writer(u'</label> <br />\n      <label for="desc">Description</label><br /> ')
        # SOURCE LINE 8
        __M_writer(escape(h.textarea('desc', row=2, class_='desc-enter')))
        __M_writer(u'</label> <br />\n      <label for="tags">Tags</label><br />  ')
        # SOURCE LINE 9
        __M_writer(escape(h.text('tags', class_='form-textbox')))
        __M_writer(u'</label> <br />\n      <label for="content">Content</label><br /> ')
        # SOURCE LINE 10
        __M_writer(escape(h.textarea('content', rows=20, class_='ignore-enter')))
        __M_writer(u'</label> <br />\n      <label for="submitter" class="l-label">Your name</label> <label for="niceurl" class="r-label">Nice url</label><br />  ')
        # SOURCE LINE 11
        __M_writer(escape(h.text('submitter', value='anon', class_='form-l-textbox', maxlength=100)))
        __M_writer(u' ')
        __M_writer(escape(h.text('niceurl', class_='form-r-textbox', maxlength=100)))
        __M_writer(u'<br />\n      ')
        # SOURCE LINE 12
        __M_writer(escape(h.submit('submit','submit', class_='submit-button')))
        __M_writer(u' <br />\n    ')
        # SOURCE LINE 13
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


