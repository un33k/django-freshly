Django Freshly
====================

A Django application that enables your server to remotely trigger a client-side asset reload.

**Author:** Val Neekman, [ info@neekware.com, @vneekman]


Overview
========

Django ``Freshly`` empowers your server in triggering assets reload (refresh) by
automatically versioning your assets as per your settings directives.

When you change an asset, whether be an .mpg, .png or a pdf file, simply up your
asset version number in your settings file and reload your server. ``Freshly`` will append a
new version number to all your assets which in turn triggers the client(s) to download a `fresh`
copy of your assets.

This application is a perfect companion to your stack specially if your static content is served from
a Content Delivery Network (CDN) such as CloudFront. You can just set the `Cache-Control` to its max and
manage your assets caching via `freshly`.


How to install
==================
    
    **Install**
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
=================

Include freshly middleware somewhere towards the end of your `MIDDLEWARE_CLASSES`.

   ```python
   MIDDLEWARE_CLASSES = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        '..............',

        # the last middleware perhaps
        'freshly.middleware.assets.AssetVersioningMiddleware',
   ] 
   ```


Decide which assets needs to be version controlled:

   ```python
   # Note that assets with the following extensions will be versioned by default:

   [
        'jpg','jpeg','gif','css','png','js','ico',
        'pdf','doc','docx','ppt','pptx','txt','mov',
        'mp4','mpeg','mp3','swf',
   ]
   ```
   
   ```python
   # You can overwrite the defaults via the ``FRESHLY_ASSETS_EXTENTIONS`` in your settings file.

    FRESHLY_ASSETS_EXTENTIONS = ['my', 'own', 'ext', 'over', 'write', 'the', 'default', 'ones',] # Example ONLY
   ```
   
   ```python
   # Or append your extensions to the default extensions via ``FRESHLY_ASSETS_EXTENTIONS_EXTRA`` in your settings file.
    FRESHLY_ASSETS_EXTENTIONS_EXTRA = ['my', 'own', 'ext', 'plus', 'the', 'default', 'ones',] # Example ONLY
   ```

Choose a versioning pattern:

   ```python
   # You can choose any pattern via ``FRESHLY_ASSETS_VERSION`` in your settings file.
   # Examples:

    FRESHLY_ASSETS_VERSION = 'v001' # OR
    FRESHLY_ASSETS_VERSION = 'ver1' # OR
    FRESHLY_ASSETS_VERSION = 'version_01' # Etc.
   ```

During the development:

   ```python
    # You may want to have a fresh copy of your .css, .js downloaded by your browser during the development
    # You can do so via ``FRESHLY_ASSETS_ALWAYS_FRESH`` in your settings file.
    # Examples:

    FRESHLY_ASSETS_ALWAYS_FRESH = True # OR
    FRESHLY_ASSETS_ALWAYS_FRESH = DEBUG
   ```



Performance:
=================
While this process may consumes some minimal CPU cycles, the fact that it's doing it without 
any complications to your code-space, should be a good reason for you to consider this app.

The application is a perfect tool for the front-end designers during the development.             
``Freshly`` ensures that designer sees the result of his/her changes immediately without constantly
hitting the browser's refresh button. 


Running the tests
=================

To run the tests against the current environment:

    python manage.py test freshly # ToDo


Changelog
=========


0.1.1
-----
* Ensure total freshness during debugging.

0.1.0
-----
* Initial release


License
=======

Copyright © Val Neekman

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Note: Django is a registered trademark of the Django Software Foundation.



