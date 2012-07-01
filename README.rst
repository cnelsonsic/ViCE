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

In the future, some or all of the following depenencies will also be required:

* `gevent = 0.13.7 <http://www.gevent.org>`_ (Networking)

* `PySide >= 1.1.1 <http://www.pyside.org>`_ (QML/QWidgets interface)

* `Urwid >= 1.0.1 <http://excess.org/urwid>`_ (Curses interface)

* `Pyparsing >= 1.5.5 <http://pyparsing.wikispaces.com/`_ 
  (declarative plugin creation and *maybe* card parsing)

Download
========
ViCE is made available through stable and unstable releases. For those wanting
to experiment with new features, feel free to try the unstable release with 
the understanding that things are expected to break. For those who are 
patient enough to wait until such features are complete, it is recommended
that you stick to the stable versions.

Stable Version
--------------
* zip: https://github.com/downloads/aspidites/ViCE/ViCE-0.0.1.zip 

* tar.gz: https://github.com/downloads/aspidites/ViCE/ViCE-0.0.1.tar.gz 

Unstable Version
----------------
The unstable version of ViCE may downloaded from the command line::

    git clone git://github.com/aspidites/ViCE.git

If git isn't installed, the repository is also available as a compresed archive:

* zip: https://github.com/aspidites/ViCE/zipball/master

* tar.gz: https://github.com/aspidites/ViCE/tarball/master 
  
Install
=======
ViCE is installed like most other python packages::
    python setup.py install 

If you'd like to have the ability to easily uninstall, we recommend using pip:
    pip install -e .

Later, you can then uninstall as follows:
    pip uninstall vice

Testing
=======
ViCE's test suite can also be run using the setup.py script::
    python setup.py test

Documentation
#############
ViCE comes with extensive documentation. If it isn't documented, it isn't a
feature.

* Online documentation: http://aspidites.github.com/ViCE
* Offline documentation: https://github.com/downloads/aspidites/ViCE/ViCE.pdf

.. note::
    The offline documentation is only updated after each release. If you are
    using an unstable version of ViCE, either consult the online documentation,
    or build a new pdf from souce by descending into the doc subdirectory and
    executing the appropriate make target::

        make latexpdf

Community
#########
If you have any questions about ViCE, or would like to contribute, there are
plenty of options.

* Github: http://github.com/aspidites/ViCE

* IRC: `#wtactics on freenode.net <irc://freenode.net/%23wtactics>`_

* Forums: http://wtactics.org/forums

* email: mailto:aspidites@wtactics.org
