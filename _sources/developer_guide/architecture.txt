Architecture
============
.. image:: /_static/stack_diagram.png

As you can see from the architecture stack diagram above, ViCE's core is
composed of the plugin framework and database layer [#]_. Item, Action, and other,
yet to be developed plugin types sit directly on these components. While not
yet started, other features and abstractions suitable for designers and
players will then be built on top of these.

.. note::
    The opacity of each box represents an approximation of how complete the
    represented component is.

Plugin Framework
----------------
ViCE's plugin framework is based on the simpole fact that all new-style
classes [#]_ in python know about their subclasses. All plugins [#]_ must
be given a name by assigning the class attribute NAME. It is through this
name that plugins are identified, and without it, a plugin won't be
discoverable. 

For information on the different plugin types and their roles, please 
refer to the :doc:`/designer_guide/designer_index`.

Database Layer
--------------
.. note::
    Not all of SQLAlchemy's API has been abstracted, so some things are 
    not yet possible. For more information, consult the :doc:`/api_reference`.    

The database layer is an abstraction ontop of 
the already excellent abstraction layer `SQLAlchemy <http://sqlalchemy.org>`_.
While this might seem excessive, it is necessary for three reasons:

#. Flexibility: Tucking the implementation details behind a simple API allows 
   us to not only change the underlying module used if we ever decide to, but 
   also selectivelly reimplement features that we feel aren't covered well by
   the underlying module.

#. Brevity: ViCE's database API is much more concise than SQLAlchemy alone,
   serves to simplify code, as well as the learning of the API itself. 

#. Seemless Integration: Since the database layer sits next to the plugin
   framework and beneath all other components, it's tightly integrated [#]_ 
   with the rest of the framework. 

Currently, the database layer is not implemented as a plugin because
SQLAlchemy provides a unified API on top of many 
:abbr:`RDBMSs (Relational Database Management Systems)`.

.. seealso::

    * :ref:`api.vice`    

 .. [#] Custom data types such as the PropertyDict are also part of ViCE's
         core, but they were left out of the chart for the sake of simplicity.

 .. [#] http://www.python.org/doc/newstyle/

 .. [#] Only plugins which are meant to be instanciated need assign the NAME 
         class attribute. That is, plugin base classes should *not* assign
         this attribute.

 .. [#] Note that we did not say "tightly coupled". As such, it is possible 
        for alternate implementations to be used.
