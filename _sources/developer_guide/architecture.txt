Architecture
============
.. image:: /_static/stack_diagram.png

As can be seen from the architecture stack diagram above, ViCE's core is
composed of the plugin framework and database layer. Item, Action, and other,
yet to be developed plugin types sit directly on these components. While not
yet started, other features and abstractions suitable for designers and
players will then be built on top of these.

.. todo::
    * explain opacity's role in this chart

Plugin Framework
----------------
.. todo::
    * Explain the plugin framework, including the python features that make it
      possible, how NAME is used for registration, etc.
    * defer to designer documentation for discussion of the differnt plugin
      types (this documentation being made available after 0.1.0 release

Database Layer
--------------
.. todo::
    * Discuss the database layer and why it wasn't implemented as a plugin.
    * Explain that some abstractions do not exist (such as a better select
      statement, joins, and edit/deletion facilities

PropertyDict
------------
.. todo::
    * Explain why such a dictionary is needed
    * give credit for origin

.. todo::
    * link to relevant sections in the API documentation (perhaps as a 
      see also directive?)
