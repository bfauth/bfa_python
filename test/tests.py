import os
import sys
import unittest

from django.core.handlers.wsgi import WSGIRequest
from django.template import TemplateSyntaxError
from django.test.client import FakePayload

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))
from bfa.fingerprint import get


class FingerprintGetTestMethods(unittest.TestCase):
    def setUp(self):
        self.request = WSGIRequest(
            environ={'REQUEST_METHOD': 'POST',
                     'wsgi.input': FakePayload('')})

    def test_wrong_argument(self):
        with self.assertRaises(TypeError):
            get(dict)

    def test_empty_fingerprint(self):
        self.request.POST = {'fp': ''}
        with self.assertRaises(ConnectionError):
            get(self.request)

    def test_wrong_fingerprint_length(self):
        self.request.POST = {'fp': 'qwerty'}
        with self.assertRaises(ValueError):
            get(self.request)

    def test_missing_fingerprint_field(self):
        with self.assertRaises(TemplateSyntaxError):
            get(self.request)


if __name__ == '__main__':
    unittest.main()
