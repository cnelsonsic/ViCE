Preface
########

ViCE is an open source, modular framework for playing and creating Trading 
Card Games (TCGs). This manual describes the various parts of the framework from
three user perspectives (roles), and also includes reference material for 
ViCE's API.

.. note::
    While there are subtle differences between the Trading Card Games and
    Collectible Card Games, in the interest of simplicity, this manual refers
    to them collectively (no pun intended) as TCGs. 

User Roles
==========
ViCE is a framework suitable for use by users of varying interests and 
technical backgrounds. In an effort to help facilitate learning, three key
user roles have been identified, as follows:

* Players: These are the individuals who aren't concerned with how ViCE's 
  internals work, and could care less about creating new or porting existing 
  TCGs to the framework. There sole reason for using ViCE is to play these
  games. 

* Designers: These are the individuals who are not interested in the
  implementation details of ViCE's internals, but would like to learn
  enough to enable them to either create new TCGs or port existing ones to
  ViCE.
 
* Developers: These are the individuals who are interested in *how* ViCE works,
  for the sake of implementing new features not possible through the currently
  available API or fixing bugs.

While we have defined three distinct roles, these roles are not mutually
exclusive, and can be viewed as somewhat hierarchial. That is, an individual
who categorizes himself as a developer may also categorize himself as a
designer and player.

How This Manual is Organized
============================

This book is organized into four parts, the first three of which being guides
modelled after the roles identified above:

    * :doc:`player_guide/intro`
    * :doc:`designer_guide/intro`
    * :doc:`developer_guide/intro`
    * :doc:`api_reference`
