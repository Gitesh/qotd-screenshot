#!/bin/bash

if [ -z "$1" "$2"]; then
	echo usage: $0 "<AUTHOR NAME>" "<QUOTE>" examlpe: "\"Douglas Addams\"" "\"Thanks for all the fish\"",
        exit
fi


#convert -size 320x100 xc:darkgrey -font $FONT -tile pattern:checkerboard -pointsize 72 -tile $GRADIENT -gravity center -annotate +28+26 $QUOTE output.gif

#convert -background black -fill yellow -font $FONT -size 620x140 -gravity center caption:"\"test test setr lorum ipsum tomato lollipop roung the best is the rest\"\n\n" -fill grey -gravity east -annotate -3 ' -- Author OneTwo' -gravity west -fill purple -annotate -3 '\n\n\n\@QOTD_17' output.gif

#convert -size 620x140 -background black -font $FONT -fill yellow -gravity center caption:"\"test test setr lorum ipsum tomato lollipop roung the best is the rest\"\n\n" -fill grey -gravity east -annotate 0 ' -- Author OneTwo' -gravity west -fill purple -annotate 0 '\n\n\n\@QOTD_17' output.gif

#CIRCULAR BLUR
#	-alpha set -virtual-pixel transparent \
#	      -channel A -radial-blur 0x10 +channel \


#TRANSALTE
#-matte    -virtual-pixel transparent \
#				-distort Perspective '0,0,0,0  0,90,0,90  90,0,90,25  90,90,90,65' \


#ROTATE
#-affine 1,0.2,0,1,1,0 -transform +repage \

#BLUR TOP AND BOTTOM
# convert output.gif -sparse-color Barycentric '0,0 black 0,%h white' -function polynomial 4,-4,1 output_blurmap.gif
# convert output.gif output_blurmap.gif -compose Blur -set option:compose:args 10 -composite output_blurrey.gif




GRADIENT=gradient
AUTHOR="-- "$1
TEXT=$2
FONT=/usr/share/fonts/truetype/tlwg/Waree-Bold.ttf
QUOTE_COLOUR=#F1E577
AUTHOR_COLOUR=#76725F
TWITTER_HANDLE_COLOUR=#C71959

echo $TEXT
echo $AUTHOR
echo $1


convert -size 600x240 \
	-background black \
        -font $FONT \
        -fill $QUOTE_COLOUR \
        -gravity center caption:"\" $TEXT \"\n\n" \
  -background black \
	      -pointsize 15 \
				-fill $AUTHOR_COLOUR \
				-gravity west\
				-annotate +40+40 "$AUTHOR" \
	-background black \
				-gravity southeast \
				-fill $TWITTER_HANDLE_COLOUR -annotate 0 '\n\n\n\@QOTD_17' \
				-bordercolor black -border 10x0 \
	-distort Perspective '0,0 0,0   213,0 213,0   213,160 213,140   0,160 0,160' \
  output.gif


echo
echo "Displaying image"
echo

display output.gif

echo "done"

pan=45
tilt=45
auto=zc
