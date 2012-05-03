Description
===========
The idea behind this folder is to compare ViCe's plugin framework to that of
LackeyCCG's. In doing so, it is hoped that ViCE not only gains feature
parity with LackeyCCG, but also ensure that creating plugins is as simple,
and optimally, simpler.

Files
=====
Files in the root directory are files that have yet to reach feature
parity. Those in the lackey subdirectory are simply the original
versions.

LackeyCCG
---------

* plugininfo.txt: Only required file. Defines how plugin works.
* CardData*.txt: Tab-delimited text file that lists all card data,
                 with the first row consisting of column headers.
* defaultchat.txt: Undocumented. Seems to be a list of default chat
                   commands.
* formats.txt: Defines different sets of cards to be displayed in the
               text editor, integral to different game formats (eg.
               tournament)
* packdefinitions*.xml: Defines virtual packs (boosters) of cards as
                        well as the distribution ratio of the contained
                        cards.
* version.txt: Used to check if a new version of the plugin is available.

ViCE
----

Rather than list what files come in a ViCE plugin (which is a task reserved
for the official documentaiton), the point of this section is to identify
analogs to the LackeyCCG files

* version.txt: This file seems redundant, considering plugin version
               is already stated in plugininfo.txt. Alternatively,
               versioned plugin names should be a simpler solution.

* plugininfo.txt: metadata can be implemented as module-level variables.

Plugin Size
===========
A comparison of each plugin's size in compressed zip format.

LackeyCCG
---------
Last Updated: 2/13/2012
* with card info: 288KB
* without card info: 4KB

ViCE
----
Last Updated 2/13/2012
* with card info: 0K
* without card info: 0K
