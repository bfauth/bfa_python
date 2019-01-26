# Browser fingerprint authenticate
This package allows you to obtain and use a user browser fingerprint for your web application as an authenticator.

# In action
If you want to test this method by yourself, check our [demo site](https://bfa.pythonanywhere.com).

# Content
- [Install](#install)
- [Usage](#usage)
    - [Django](#django)
    - [Flask](#flask)
- [Salt](#also)
- [Dependences](#using)
- [Python versions](#supported-python)
- [License](#license)

# Install
You can install package by:

`pip install bfa`

# Usage
At the moment, django and flask support is provided, in the future it is planned to add other frameworks.

## Django
Add `'bfa'` to your list of `INSTALLED_APPS` in _settings.py_:
```python
INSTALLED_APPS = [
    ...
    'bfa'
]
```

- You can get user fingerprint by:

    `bfa.fingerprint.get(request)`

- In template paste inside `<form></form>`:

    `{% load bfa %}{% fingerprint_input %}`

**For example:**

_login.html_
```html
...
<form method="post">
    {% csrf_token %}
    
    <input name="username">
    
    {% load bfa %}
    {% fingerprint_input %}
    
    <button type="submit">Log in</button>
</form>
...
```

_views.py_
```python
import bfa
from django.http import HttpResponse
from django.shortcuts import render

...


def login(request):
    if request.method == 'POST':
        # Getting a username
        username = request.POST.get('username')
        
        # Getting a fingerprint
        try:
            fp = bfa.fingerprint.get(request)
        except (ConnectionError, ValueError):
            return HttpResponse("Can't get fingerprint")
        
        # Here is the part where you process the 
        # username and fingerprint, according to the database
        ...

        return HttpResponse("You're logged in")

    return render(request, 'login.html')


...
```

# Flask
Add bfa context processor to your _app.py_:
```python
...
import bfa
from flask import Flask

app = Flask(__name__)


@app.context_processor
def bfa():
    return bfa.templatetags.bfa.fingerprint_input()


...
```

- You can get user fingerprint by:

    `bfa.fingerprint.get(request)`

- In template paste inside `<form></form>`:

    `{{ fingerprint_input }}`

**For example:**

_login.html_
```html
...
<form method="post">
    <input name="username">

    {{ fingerprint_input }}
    
    <button type="submit">Log in</button>
</form>
...
```

_app.py_
```python
import bfa
from flask import Flask, request

app = Flask(__name__)

...


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Getting a username
        username = request.form['username']

        # Getting a fingerprint
        try:
            fp = bfa.fingerprint.get(request)
        except (ConnectionError, ValueError):
            return "Can't get fingerprint"
        
        # Here is the part where you process the 
        # username and fingerprint, according to the database
        ...

        return "You're logged in"

    else:
        return "Login page"


...
```

# Also
You can salt fingerprints by:

`bfa.fingerprint.get(request, use_salt=True)`

**For example:**

_views.py_
```python
import bfa
from django.http import HttpResponse
from django.shortcuts import render

...


def login(request):
    if request.method == 'POST':
        # Getting a username
        username = request.POST.get('username')
        
        # Getting a fingerprint
        try:
            fp_data = bfa.fingerprint.get(request, use_salt=True)
        except (ConnectionError, ValueError):
            return HttpResponse("Can't get fingerprint")

        fp = fp_data['fp']
        salt = fp_data['salt']
        
        # Here is the part where you process the 
        # username, fingerprint and salt, according to the database
        ...
        
        return HttpResponse("You're logged in")
        
    return render(request, 'login.html')


...
```

# Using
This project uses:
- [Django](https://github.com/django/django "Python")
- [Werkzeug](https://github.com/pallets/werkzeug "Python")
- [FingerprintJS2](https://github.com/Valve/fingerprintjs2 "JS")
- [JS-SHA3](https://github.com/emn178/js-sha3 "JS")

# Supported python
BFA working on python >=3.5 only.

# License
This project is under Apache 2.0 license.
