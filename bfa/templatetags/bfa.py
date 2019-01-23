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

from django import template
from django.utils.safestring import mark_safe, SafeText

register = template.Library()


@register.simple_tag
def fingerprint_input() -> SafeText:
    """Load scripts and calculate the fingerprint

    :rtype: SafeText
    :return: raw html, which is embedded in the page
    """
    html = mark_safe("<script src='https://cdnjs.cloudflare.com/ajax/libs/js-s\
ha3/0.8.0/sha3.min.js' async></script><script src='https://cdn.jsdelivr.net/np\
m/fingerprintjs2@2.0.3/dist/fingerprint2.min.js'></script><input type='hidden'\
name='fp'><script>Fingerprint2.get(function(e){document.getElementsByName('fp'\
)[0].value=sha3_256(e.map(function(e){return e.value}).join())})</script>")
    return html
