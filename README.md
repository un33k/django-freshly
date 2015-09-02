Django Freshly
====================

**A Django application that enables your server to remotely trigger a client-side asset reload**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![download-image]][download-link]


Overview
====================

A simple trigger of client-side asset reload.


How to install
====================

    1. easy_install django-freshly
    2. pip install django-freshly
    3. git clone http://github.com/un33k/django-freshly
        a. cd django-freshly
        b. run python setup.py
    4. wget https://github.com/un33k/django-freshly/zipball/master
        a. unzip the downloaded file
        b. cd into django-freshly-* directory
        c. run python setup.py


How to use
====================
Installed `django-freshly` using one of the methods outlined in the `How to install` section.

   ```python
    # Add `freshly.middleware.assets.AssetVersioningMiddleware` to your `MIDDLEWARE_CLASSES`.
    # Note: ensue the middleware is last item in your `MIDDLEWARE_CLASSES`.

    # If you want to limit your asset extension, then overwrite it in your settings file as follow:

    FRESHLY_ASSETS_EXTENTIONS = [
        'jpg', 'jpeg', 'gif', 'css', 'png', 'js', 'ico', 'txt'
    ]

    # Initialize your asset version by adding `FRESHLY_ASSETS_VERSION` to your setting file as follow:

    FRESHLY_ASSETS_VERSION = '001'

    # OR

    FRESHLY_ASSETS_VERSION = 'v001'

    # You may want to have a fresh copy of your .css, .js downloaded by your browser during the development
    # You can do so via ``FRESHLY_ASSETS_ALWAYS_FRESH`` in your settings file.
    # Examples:

    FRESHLY_ASSETS_ALWAYS_FRESH = True # OR
    FRESHLY_ASSETS_ALWAYS_FRESH = DEBUG
   ```

Performance:
=================
While this process may consumes some minimal CPU cycles, the fact that it's doing it without
any complications to your code-space should be a good reason for you to consider this app.

The application is a perfect tool for the front-end designers during the development.
It ensures that you see the result of your changes immediately without constantly
hitting the browser's refresh button or reseting the history.


Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-freshly.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-freshly?branch=master

[version-image]: https://img.shields.io/pypi/v/django-freshly.svg
[version-link]: https://pypi.python.org/pypi/django-freshly

[coverage-image]: https://coveralls.io/repos/un33k/django-freshly/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-freshly

[download-image]: https://img.shields.io/pypi/dm/django-freshly.svg
[download-link]: https://pypi.python.org/pypi/django-freshly
