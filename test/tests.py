import os
import sys
import unittest
from hashlib import sha3_256

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
        self.fp = sha3_256('bfa'.encode()).hexdigest()

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

    def test_good_fingerprint(self):
        self.request.POST = {'fp': self.fp}
        self.assertEqual(get(self.request), self.fp)

    def test_salted_fp_len(self):
        self.request.POST = {'fp': self.fp}
        fp_len = len(get(self.request, use_salt=True)['fp'])
        self.assertEqual(fp_len, 64)


if __name__ == '__main__':
    unittest.main()
