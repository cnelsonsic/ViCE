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

* `sqlalchemy >= 0.7 <http://www.sqlalchemy.org>`_ : `vice.database`

* `sqlite >= 3.7.11 <http://www.sqlite.org>`_ : `vice.database`

In the future, some or all of the following depenencies will also be required:

* `gevent = 0.13.7 <http://www.gevent.org>`_ : `vice.client` and `vice.server`

* `PySide >= 1.1.1 <http://www.pyside.org>`_ : `vice.ui.qt`

* `Kivy >= 1.4.0 <http://www.kivy.org`_ : `vice.ui.kviy`

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

        python setup.py doc --formats latexpdf

    To avoid havingto type the --formats option repeatedly, you may modify
    setup.cfg. For example::

        [doc]
        formats = latexpdf,htl

    Will generate pdf and html documentation by default::

        python setup.py doc

    For other configurable options, type::

        python setup.py doc --help


Community
#########
If you have any questions about ViCE, or would like to contribute, there are
plenty of options.

* Github: http://github.com/aspidites/ViCE

* IRC: `#wtactics on freenode.net <irc://freenode.net/%23wtactics>`_

* Forums: http://wtactics.org/forums

* email: mailto:aspidites@wtactics.org

Branches
========
This section identifies the different branches of development and their
purpose. In cases where this file doesn't document a branch, the general rule
of thumb is that the master branch represents the main development branch of
development, where as the others are feature branches[2] where experimental
concepts are worked on.

master
    As stated already, this is where a majority of work on ViCE happens.
    When concepts developed in other branches are completed, they are
    merged here. It should be noted that already agreed upon concepts are
    developed directly within this branch, so at no given point is it
    guaranteed to be stable. If you want to ensure that a checkout is
    stable, you should checkout a tag instead.

cli
    This is where the cli frontent is being developed. At present, I'm
    experimenting with an interface similar to what a lot of web frameworks
    provide which generate code stubs for you by passing relevant commands.
    I would also like to experiment with a REPL-style interface for ViCE.
    The interface is mostly geared toward developers and designers. If time
    permits (or there is a demand), I might try and develop an ncurses
    (through urwid) interface for players. Vim bindings +TCG = PWNAGE?
    Maybe...

qml
    This is where the qml frontend is being developed. While Kivy seemed
    better suited to touch interfaces as well as android development
    initially, it seems that QML is more mature and less buggy. That said,
    I'm an infrequent contributor to Kivy, so don't be surprised if work
    here ceases and a kivy branch appears.

gh-pages
    This is where the generated documentation goes. Changes to
    documentation should occur in other branches, not here! At present, it
    is necessary to first delete the doc and vice directories and check
    them out again before running `make gh-pages`, but once issue #12 is
    resolved, this will not be so. 

packaging
    This is not a branch for packaging for different operating systems, but
    rather a branch that maintains distutils2 (or in python 3.3
    "packaging") scripts. The result is far less clumbsy than distribute,
    so I'm hoping to merge this branch as a drop-in replacement for the current
    setup.py script.
