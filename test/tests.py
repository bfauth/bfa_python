"""Copyright 2019 Artjom Löbsack

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import unittest
from hashlib import sha3_256
from os import environ
from sys import path

from django.core.handlers.wsgi import WSGIRequest
from django.template import TemplateSyntaxError
from django.test.client import FakePayload

path.insert(0, '..')
from bfa.fingerprint import get

environ['DJANGO_SETTINGS_MODULE'] = 'settings'


class FingerprintGetTestMethods(unittest.TestCase):
    def setUp(self):
        """Tests set up

        Add variables to path and calculate test fingerprint
        """
        self.request = WSGIRequest(
            environ={'REQUEST_METHOD': 'POST',
                     'wsgi.input': FakePayload('')})
        self.fp = sha3_256('bfa'.encode()).hexdigest()

    # noinspection PyTypeChecker
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
