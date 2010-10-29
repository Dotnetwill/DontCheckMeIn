from dontcheckmein.tests import *

class TestIgnorefileController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='ignorefile', action='index'))
        # Test response...
