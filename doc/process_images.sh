#!/usr/bin/env sh
# Depends on inkscape and pylint

IMGDIR="./doc/source/_static"

# create class and package diagrams
pyreverse -s1 -my -o svg -p ViCE vice
mv *ViCE.svg $IMGDIR

# convert svg's to png's
for SVG in ls $IMGDIR/*.svg
do
	inkscape -D -e $IMGDIR/`basename $SVG .svg`.png $SVG
done
