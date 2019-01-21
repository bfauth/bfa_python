Browser fingerprint authenticate
================================

This package allows you to obtain and use a user 
browser fingerprint for your web application as 
an authenticator.

Install
=======

You can install package by:

`pip install bfa`

Then add app in INSTALLED_APPS in your settings.py:

_settings.py_

```python
INSTALLED_APPS = [
    'bfa'
]
```

Usage
=====

You can get user fingerprint by:

`bfa.fingerprint.get(request)`

In templates it's simple

`{% load bfa %}{% fingerprint_input %}`

For example:

_views.py_

```python
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

        return HttpResponse("You're logged in")

    return render(request, 'login.html')
```


_login.html_

```html
<form method="post">
    {% csrf_token %}
    <input name="username">
    {% load bfa %}
    {% fingerprint_input %}
    <button type="submit">Log in</button>
</form>
```

Also
====
You can salt fingerprints by:

`bfa.fingerprint.get(request, use_salt=True)`

For example:

_views.py_

```python
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
        
        return HttpResponse("You're logged in")
        
    return render(request, 'login.html')
```

Using
=====

This project uses:

[Fingerprintjs2](https://github.com/Valve/fingerprintjs2 "Fingerprintjs2 repo")
and
[js-sha3](https://github.com/emn178/js-sha3 "js-sha3 repo")
