.. toctree::
    :numbered:
    :hidden:

    player_guide/*
    designer_guide/*
    developer_guide/*
    api_reference

Introduction
============
:abbr:`ViCE (Virtual Card-game Engine)` is an open source, portable, modular 
framework for playing and creating :abbr:`TCGs (Trading Card Games)`. This 
manual outlines ViCE's design principles, describes its various features from 
three perspectives (which we refer to as roles), and even includes reference 
documentation for the public API.

.. note::
    While there are subtle differences between the Trading Card Games and
    Collectible Card Games, in the interest of simplicity, this manual refers
    to them collectively (no pun intended) as TCGs. 

User Roles
==========
ViCE is a framework suitable for use by users 
of varying interests and technical backgrounds. In an effort to help facilitate 
learning, three key user roles have been identified, as follows:

Players
    These are the individuals who aren't concerned with how 
    ViCE's internals work, and could care less 
    about creating new or porting existing :abbr:TCGs to 
    the framework. There sole reason for using 
    ViCE is to play whatever games *do* 
    exist for ViCE.

Designers
    These are the individuals who are not interested in the
    implementation details of ViCE's internals, 
    but would like to learn enough to enable them to either create new TCGs or 
    port existing ones to ViCE.
 
Developers
    These are the individuals who are interested in *how* 
    ViCE works, for the sake of implementing 
    new features not possible through the currently available API or fixing bugs.

While we have defined three distinct roles, these roles are not mutually
exclusive, and can be viewed as somewhat hierarchical. That is, an individual
who categorizes himself as a developer may also categorize himself as a
designer and player.

How This Manual is Organized
============================
This book is organized into four parts, the first three of which being guides
modeled after their respective roles:

* :doc:`player_guide/player_index`

* :doc:`designer_guide/designer_index`

* :doc:`developer_guide/developer_index`

* :doc:`api_reference`


Design Principles
=================
In this section, we'll talk about the core principles that we adhere to when
developing, designing, and playing ViCE.

Openness
--------
ViCE is open source software licensed under 
the `Affero General Public License <http://www.gnu.org/licenses/agpl-3.0.html>`_,
which means that you can use it, redistribute it, and even modify it without
any legal ramifications, so long as you abide by the terms of the license. 
This also guarantees that as improvements are made, whether it be to 
ViCE's upstream code base or to a fork, that 
if those improvements are made public, they are made without any monetary 
obligation. That is, you should never have to pay for new features or corrected defects.

Portability
-----------
ViCE is written using a variety of 
cross-platform technologies, and as such, every effort is made to ensure that 
ViCE runs *natively* on at least Linux, 
Mac OS, and Windows. 

Modularity
----------
Most of ViCE's features are implemented on top 
of its plugin architecture to allow for maximum extensibility. Not only does 
this imply that new features can be added rather easily, but also that features 
may be used a la carte: if a feature isn't required for you to finish a plugin, 
it doesn't need to be used.

