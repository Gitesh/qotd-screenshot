#   This work is part of the qotd-screenshot program, see https://twitter.com/qotd_17
#   The project source can be found at https://github.com/Gitesh/qotd-screenshot
#   Copyright 2015 Gitesh Khodiyar

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.




#!/bin/bash

if [ -z "$1" ]; then
	echo usage: $0 "<AUTHOR NAME>" "<QUOTE>" example: "\"Douglas Adams\"" "\"So long and thanks for all the fish\"",
        exit
fi


#convert -size 320x100 xc:darkgrey -font $FONT -tile pattern:checkerboard -pointsize 72 -tile $GRADIENT -gravity center -annotate +28+26 $QUOTE output.gif

#convert -background black -fill yellow -font $FONT -size 620x140 -gravity center caption:"\"test test setr lorum ipsum tomato lollipop roung the best is the rest\"\n\n" -fill grey -gravity east -annotate -3 ' -- Author OneTwo' -gravity west -fill purple -annotate -3 '\n\n\n\@QOTD_17' output.gif

#convert -size 620x140 -background black -font $FONT -fill yellow -gravity center caption:"\"test test setr lorum ipsum tomato lollipop roung the best is the rest\"\n\n" -fill grey -gravity east -annotate 0 ' -- Author OneTwo' -gravity west -fill purple -annotate 0 '\n\n\n\@QOTD_17' output3.gif

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

AUTHOR="-- "$1
TEXT=$2

QUOTE_FONT=/usr/share/fonts/truetype/tlwg/Purisa-BoldOblique.ttf
AUTHOR_FONT=/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf
TWITTER_HANDLE_FONT=/usr/share/fonts/truetype/droid/DejaVuSans-Bold.ttf

QUOTE_COLOUR=#F1E577
AUTHOR_COLOUR=#76725F
TWITTER_HANDLE_COLOUR=#C71959

#echo $TEXT
#echo $AUTHOR
#echo $1



#Twitter reccomended image size is 1024x512 

convert -size 1024x512 \
	-background black \
        -font $QUOTE_FONT \
        -fill $QUOTE_COLOUR \
        -gravity center caption:"\" $TEXT \"\n\n" \
  -background black \
	      -pointsize 30 \
				-font $AUTHOR_FONT \
				-fill $AUTHOR_COLOUR \
				-gravity southeast \
				-annotate +40+40 "$AUTHOR" \
	-background black \
				-gravity southeast \
				-font $TWITTER_HANDLE_FONT \
				-fill $TWITTER_HANDLE_COLOUR -annotate 0 '\n\n\n\@QOTD_17' \
  -distort Perspective '0,0 0,0   213,0 213,0   213,160 213,140   0,160 0,160' \
  -vignette '1000x60,0.5,0.1,1.5' \
	-trim \
	-bordercolor black -border 40x20 \
  -crop 1024x512 +repage \
output.gif




#echo
#echo "Displaying image"
#echo
display output.gif

echo "--quote image creation completed--"
