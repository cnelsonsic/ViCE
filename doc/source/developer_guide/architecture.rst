Architecture
============
.. image:: /_static/stack_diagram.png

As you can see from the architecture stack diagram above, ViCE's core is
composed of the plugin framework and database layer[#]_. Item, Action, and other,
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

.. todo::
    * defer to designer documentation for discussion of the differnt plugin
      types (this documentation being made available after 0.1.0 release

Database Layer
--------------
.. todo::
    * Discuss the database layer and why it wasn't implemented as a plugin.
    * Explain that some abstractions do not exist (such as a better select
      statement, joins, and edit/deletion facilities

.. todo::
    * link to relevant sections in the API documentation (perhaps as a 
      see also directive?)

 .. [#] Custom data types such as the PropertyDict are also part of ViCE's
         core, but they were left out of the chart for the sake of simplicity.

 .. [#] http://www.python.org/doc/newstyle/

 .. [#] Only plugins which are meant to be instanciated need assign the NAME 
         class attribute. That is, plugin base classes should *not* assign
         this attribute.
