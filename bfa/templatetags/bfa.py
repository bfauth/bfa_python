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

from inspect import stack
from typing import Dict

from django import template
from django.utils.safestring import mark_safe, SafeText

register = template.Library()


@register.simple_tag
def fingerprint_input() -> Dict[str, SafeText] or SafeText:
    """Load scripts and calculate the fingerprint

    :rtype: SafeText
    :return: raw html, which is embedded in the page
    """
    if stack()[1][3] == 'bfa_flask':
        # noinspection PyTypeChecker
        return {'fingerprint_input': fingerprint_input()}
    else:
        return mark_safe("<{1} src='{0}js-sha3' async></{1}><{1} src='{0}finge\
rprintjs2@2'></{1}><input type='hidden' name='fp'><{1}>window.onload=function(\
){{Fingerprint2.get(function(e){{document.getElementsByName('fp')[0].value=sha\
3_256(e.map(function(e){{return e.value}}).join())}})}}</{1}>"
                         .format('https://cdn.jsdelivr.net/npm/', 'script'))
