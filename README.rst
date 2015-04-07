This is the AMIGOS pelican site. The site is hosted via GitHub. See the 
gh-pages_ branch. 

.. _gh-pages: https://github.com/The-AMIGOS/The-AMIGOS.github.io/tree/gh-pages

Quickstart
----------

Something like::

    $ git https://github.com/The-AMIGOS/The-AMIGOS.github.io.git
    $ cd The-AMIGOS.github.io
    $ # make a virtualenv. Otherwise you end up with required deps system wide
    $ pip install -r requirements.txt
    $ ./develop_server.sh start
    $ # Webbrowser to 127.0.0.1:8000
    $ vi content/pages/ 
    $ # edit, edit & edit
    $ Webbrowser to 127.0.0.1:8000
    $ # Send me a pull request!
    $ # Profit

ghp-import and custom domain setup instructions_.

.. _instructions: https://github.com/getpelican/pelican/blob/master/docs/tips.rst

help: m.stantoncook_-AT-_gmail.com
