This is the AMIGOS pelican site. This is the source and pelican config. 
The site is hosted via GitHub. See the master_ branch. 

.. _master: https://github.com/The-AMIGOS/The-AMIGOS.github.io/tree/master

Quickstart - Build the site locally
-----------------------------------

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

I use a post-commit hook to publish the pages::

    make clean && make html && cp content/.nojekyll output/ && cp content/.CNAME output/CNAME && ghp-import -b master -p -m 'Site build' output &&

Note - you need to do some branch wrangling. Make master == pelican-source and gh-pages == master.


.. _instructions: https://github.com/getpelican/pelican/blob/master/docs/tips.rst

help: m.stantoncook--AT--gmail.com
