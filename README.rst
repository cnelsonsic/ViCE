Vice is a portable, open source, modular framework for both creating and 
playing trading card games.

Getting ViCE
############
.. warning::
    The current version of ViCE is suitable for developers only. A version
    suitable for designers will be made available next, then finally, one
    that will cater to players. If you are unsure which category you belong
    to, read my blog post on `wtactics.org <http://wtactics.org/vice-versa/>`_.

Dependencies
============
In it's current state, ViCE has few dependencies:
    * `python >= 2.7 (including 3.x) <http://python.org>`_
    * `sqlalchemy >= 0.7 <http://www.sqlalchemy.org>`_
    * `sqlite >= 3.7.11 <http://www.sqlite.org>`_

In the future, the following depenencies will also be required:
    * `PySide >= 1.1.1 <http://www.pyside.org>`_
    * `gevent >= 1.0b2 <http://www.gevent.org>`_

Download
========

ViCE may downloaded from the command line::
    git clone git://github.com/aspidites/ViCE.git

If git isnt' installed, the repository is also available as a compresed archive:
    * https://github.com/aspidites/ViCE/zipball/master
    * https://github.com/aspidites/ViCE/tarball/master 
  
Install
=======
ViCE is installed like most other python packages::
    python setup.py install 

Testing
=======
ViCE's test suite can also be run using the setup.py script::
    python setup.py test

Documentation
#############
ViCE comes with extensive documentation. If it isn't documented, it isn't a
feature.

* Online documentation: http://aspidites.github.com/ViCE
* Offline documentation: (Coming Soon)

Community
#########
If you have any questions about ViCE, or would like to contribute, there are
plenty of options.

* Github: http://github.com/aspidites/ViCE
* IRC: `#wtactics on freenode.net <irc://freenode.net/%23wtactics>`_
* Forums: http://wtactics.org/forums
* email: mailto:aspidites@wtactics.org
