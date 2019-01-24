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

from django.template import Library
from django.utils.safestring import mark_safe, SafeText

register = Library()


@register.simple_tag
def fingerprint_input() -> SafeText:
    """Load scripts and calculate the fingerprint

    :rtype: SafeText
    :return: raw html, which is embedded in the page
    """
    return mark_safe("<{1} src='{0}js-sha3' async></{1}><{1} src='{0}fingerpri\
ntjs2@2'></{1}><input type='hidden' name='fp'><{1}>window.onload=function(){{F\
ingerprint2.get(function(e){{document.getElementsByName('fp')[0].value=sha3_25\
6(e.map(function(e){{return e.value}}).join())}})}}</{1}>"
                     .format('https://cdn.jsdelivr.net/npm/', 'script'))
