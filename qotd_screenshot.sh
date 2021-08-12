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

AUTHOR="-- "$1
TEXT=$2


# LOAD THE FONTS - CHECK YOUR SYSTEM HAS THESE
QUOTE_FONT=/usr/share/fonts/truetype/tlwg/Purisa-BoldOblique.ttf
AUTHOR_FONT=/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf
TWITTER_HANDLE_FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf

QUOTE_COLOUR=#F1E577
AUTHOR_COLOUR=#76725F
TWITTER_HANDLE_COLOUR=#C71959

#echo $TEXT
#echo $AUTHOR
#echo $1

echo "--Creating image from quote"

#Twitter reccomended image size is 1024x512 


#---------------------------
#---THEME: SYNTHWAVE FLAT---
#---------------------------

# convert -size 1024x512 -fill dodgerblue -font $QUOTE_FONT -background black \
# 		       -gravity center caption:"\" $TEXT \"" \
# 		       \( +clone -blur 0x25 -level 0%,50% \) \
#                -compose screen -composite \
# 	    -pointsize 30 \
# 		       -font $AUTHOR_FONT \
# 		       -fill $AUTHOR_COLOUR \
# 			   -gravity southwest \
# 			   -annotate +1+1 "$AUTHOR" \
# 		-gravity southeast \
# 			   -font $TWITTER_HANDLE_FONT \
# 			   -fill $TWITTER_HANDLE_COLOUR -annotate 0 '\n\n\n\@QOTD_17'\
# 	-bordercolor black -border 40x40 \
# output.png


#-----------------------------
#---THEME: SYNTHWAVE TILTED---
#-----------------------------

# convert -size 1024x512 -fill dodgerblue -font $QUOTE_FONT -background black \
# 		       -gravity center caption:"\" $TEXT \"" \
# 		       \( +clone -blur 0x25 -level 0%,50% \) \
#                -compose screen -composite \
# 	    -pointsize 30 \
# 		       -font $AUTHOR_FONT \
# 		       -fill $AUTHOR_COLOUR \
# 			   -gravity southwest \
# 			   -annotate +1+1 "$AUTHOR" \
# 		-gravity southeast \
# 			   -font $TWITTER_HANDLE_FONT \
# 			   -fill $TWITTER_HANDLE_COLOUR -annotate 0 '\n\n\n\@QOTD_17'\
# 	-bordercolor black -border 40x40 \
#     -distort Perspective '0,0 0,0   213,0 213,0   213,160 213,140   0,140 0,140' -trim \
# 		-bordercolor black -border 40x40 \
# 	    +repage \
# output.png


# ----------------------------------------
# ---THEME: DEFAULT CLEAN YELLOW TILTED---
# ----------------------------------------

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
output.png




#echo
#echo "Displaying image"
#echo
#display output.png

echo "----Image created"
