"""Copyright 2018 Artjom Löbsack

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

from hashlib import sha3_256
from random import choices
from string import printable

from django.core.handlers.wsgi import WSGIRequest
from django.template import TemplateSyntaxError
from django.utils.datastructures import MultiValueDictKeyError


def _return_salted(string: str) -> tuple:
    """Make string salty

    :param string: your string to salt
    :return: salted string and salt for it
    """
    primary_salt = ''.join(choices(printable, k=1024))
    secondary_salt = sha3_256(primary_salt.encode()).hexdigest()
    string = sha3_256(
        ('%s%s' % (string, secondary_salt)).encode()
    ).hexdigest()
    return string, secondary_salt


def get(request: WSGIRequest, use_salt: bool = False) -> str or dict:
    """Return users browser fingerprint.

    :param request: django request from views.py
    :param use_salt: parameter indicating whether
                     to salt the fingerprint
    :return: 64-symbol SHA3-256 hash - browser fingerprint
             or dictionary, contains salted fingerprint and salt for
             it, if use_salt=True
    """
    request_type = type(request)
    if request_type != WSGIRequest:
        raise TypeError("get() argument must be WSGIRequest, not %s"
                        % request_type)
    try:
        fp = request.POST['fp']
    except MultiValueDictKeyError:
        raise TemplateSyntaxError("Missing fingerprint field in %s"
                                  % request.path)
    if not fp:
        raise ConnectionError("Failed to load JS on client")
    elif len(fp) != 64:
        raise ValueError("Fingerprint must be 64 symbols")
    else:
        if use_salt:
            fp, salt = _return_salted(fp)
            return {'fp': fp, 'salt': salt}
        return fp


field = """<script async src='https://cdnjs.cloudflare.com/ajax/libs/js-sha3/0\
.8.0/sha3.min.js'></script>
<script src='https://cdn.jsdelivr.net/npm/fingerprintjs2@2.0.3/dist/fingerprin\
t2.min.js'></script>
<input type='hidden' name='fp'>
<script>Fingerprint2.get(function(e){document.getElementsByName('fp')[0].value\
=sha3_256(e.map(function(e){return e.value}).join())})</script>
"""
