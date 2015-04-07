This is the AMIGOS pelican site. This is the source and pelican config. 
The site is hosted via GitHub. See the master_ branch for the pages that are 
served. 


Quickkstart - Suggest changes
-----------------------------

Something like this:

**1)** If you don't have one already, signup for a GitHub_ account

**2)** Head over to the `AMIGOS site REPO`_    

**3)** Find the page your interested in (content/pages). Use the schedule as an example. `Direct link`_.

**4)** Click the edit link (pencil icon, shown)

|
.. image:: https://raw.githubusercontent.com/The-AMIGOS/The-AMIGOS.github.io/pelican-source/instructions/edit.jpg
|

**5)** Edit, edit & edit (shown)

|
.. image:: https://raw.githubusercontent.com/The-AMIGOS/The-AMIGOS.github.io/pelican-source/instructions/editing.jpg
|

**6)** Scroll to the bottom. Fill in the info on your change. Click the Propose Change button.

**7)** Click the Create Pull Request button (shown), then click the next Create Pull Request button.

|
.. image:: https://raw.githubusercontent.com/The-AMIGOS/The-AMIGOS.github.io/pelican-source/instructions/pr.jpg
|

**8)** Wait for review and incorporation into the AMIGOS site...


Quickstart - Build & develop the site locally
---------------------------------------------

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


Notes
-----

ghp-import and custom domain setup instructions_.

I use a post-commit hook to publish the pages::

    make clean && make html && cp content/.nojekyll output/ && cp content/.CNAME output/CNAME && ghp-import -b master -p -m 'Site build' output &&

Note - you need to do some branch wrangling. Make master == pelican-source and gh-pages == master.

help: m.stantoncook--AT--gmail.com


.. _master: https://github.com/The-AMIGOS/The-AMIGOS.github.io/tree/master
.. _instructions: https://github.com/getpelican/pelican/blob/master/docs/tips.rst
.. _GitHub: https://github.com/
.. _`AMIGOS site REPO`: https://github.com/The-AMIGOS/The-AMIGOS.github.io
.. _`Direct link`: https://github.com/The-AMIGOS/The-AMIGOS.github.io/blob/pelican-source/content/pages/Schedule.rst
