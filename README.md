Browser fingerprint authenticate
================================

This package allows you to obtain and use a user 
browser fingerprint for your web application as 
an authenticator.

Install
=======

You can install package by:

`pip install bfa`

Usage
=====

For example:

_views.py_
```python
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            fp = bfa.fingerprint.get(request)
        except (ConnectionError, ValueError):
            return HttpResponse("Can't get fingerprint")
        [...]
        return HttpResponse("You're logged in")
    return render(request, 'login.html',
                  {'fp_field': bfa.fingerprint.field})
```

_login.html_
```html
<form method="post">
    {% csrf_token %}
    <input name="username">
    {{ fp_field|safe }}
    <button type="submit">Log in</button>
</form>
```
