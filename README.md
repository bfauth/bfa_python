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
        username = request.get('username')
        fp = bfa.fingerprint.get(request)        
        [...]
        return HttpResponse("You're logged in!")
    else:
        fp_field = bfa.fingerprint.field
        return render_to_response('login.html', 
                                  {'fp_field': fp_field})
```

_login.html_
```html
<form method="post">
    <input name="username">
    {{ fp_field }}
    <button type="submit">Log in</button>
</form>
```