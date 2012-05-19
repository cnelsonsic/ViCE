#!/usr/bin/env sh
IMGDIR="source/images"

for SVG in ls $IMGDIR/*.svg
do
	inkscape -D -e $IMGDIR/`basename $SVG .svg`.png $SVG
done
