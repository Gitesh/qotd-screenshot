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

##DEPENDENDCIES##
#set up new service account credentials at http://console.developers.google.com
#give the account access to two api scopes: 1. Drive and 2. Spreadsheet
#set up a new twitter application at https://apps.twitter.com and note credentials
#install the following local dependencies:
#sudo apt-get install gspread 
#sudo apt-get install pip
#sudo pip install --upgrade oauth2client
#sudo apt install imagemagick



#!/usr/bin/python

import json
import gspread
import subprocess
from random import randint
from google.oauth2.service_account import Credentials
from pyasn1.type.univ import Null
from twython import Twython
from token917354 import *


def tweetme(text, hashtag, image):

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    text = str(text)+str(hashtag)
    photo = open(image, 'rb')

    twitter.update_status_with_media(status=text, media=photo)
    return


json_key = json.load(open('qotd-17-6cfc9e0e9808.json'))

scopes = [
	'https://www.googleapis.com/auth/spreadsheets',
	'https://www.googleapis.com/auth/drive'
	]


credentials = Credentials.from_service_account_file('qotd-17-6cfc9e0e9808.json', scopes=scopes)
gc = gspread.authorize(credentials)

print("--Connecting to quotes database--")

wks = gc.open("qotd_source").sheet1


#UPDATE A CELL
#wks.update_acell('B2', "it's down there somewhere, let me take another look.")
# Fetch a cell range
#cell_list = wks.range('A1:B7')
#print cell_list
#print wks.acell("a1").value
#print wks.row_count

qotdQotdIDLength = len(wks.col_values(1))

qotdRandomID = randint(2,qotdQotdIDLength)

strQotdRandomID = str(qotdRandomID)

#--check that the validated status of the quote is set to 1--

intValidatedStatus = Null

intValidatedStatus = int(wks.acell('h'+strQotdRandomID).value)  #Read the Validated Status column from a random row 

print("----Random row selected: " + strQotdRandomID)
print("----Random row validated status is: " + str(intValidatedStatus))

while intValidatedStatus < 1:     # 0 is do not use the quote, 1 is use the row
  if intValidatedStatus == 0:
    print ("----Oh no! the selected row is set to 0 ")
    print("-----So selecting another random row..." + (str(intValidatedStatus)))
    qotdRandomID = randint(2,qotdQotdIDLength)    #Start at row 2 because row 1 is the heading
    strQotdRandomID = str(qotdRandomID)
    strValidatedStatus = wks.acell('h'+strQotdRandomID).value  #Read the Validated Status column from a random row again 
    intValidatedStatus = (int(str(strValidatedStatus)))
    print("----New validated status: " + (str(strValidatedStatus)))
    continue
print ("--A valid row was selected so exiting selection loop...")

#----------validated status checked and a random valid quote selected

# print (wks.acell('a'+strQotdRandomID))  #TimeStamp
# print (wks.acell('b'+strQotdRandomID))  #ID
# print (wks.acell('c'+strQotdRandomID))  #Author
# print (wks.acell('d'+strQotdRandomID))  #Quote
# print (wks.acell('e'+strQotdRandomID))  #Hashtag
# print (wks.acell('f'+strQotdRandomID))  #Usage counter
# print (wks.acell('g'+strQotdRandomID))  #Last used date
# print (wks.acell('h'+strQotdRandomID))  #Validated status


#Get the length of the hashtag below and truncate the quote length for the text ONLY (but not alter the image)
qotdHashtag = wks.acell('e'+strQotdRandomID).value #Quote
qotdHashtag = str(" " + qotdHashtag) #add a space before the quote end and hashtag, looks neater, 




#Write code to increase the counter for the text

qotdLastUsedCounter = int(wks.acell('f'+strQotdRandomID).value)

print ("----Last Used Counter: " + str(qotdLastUsedCounter))

qotdLastUsedCounter += 1

print ("----Last Used Counter+1: " + str(qotdLastUsedCounter))

#qotdLastUsedCounterNow += int(qotdLastUsedCounter)

#Update usage counter and date
wks.update_acell('f'+strQotdRandomID,qotdLastUsedCounter) #update counter

print("----Last used counter incremented and added to selected row")

#qotdLastUsedDateNow = wks.updated #updated has been deprecated in google sheets v4
#print("DEPRECATED SPREADSHEET UPDATE VALE: " + str(wks.updated))


#---------------

from datetime import datetime

# Current date time in local system

qotdLastUsedDateNow = str(datetime.now())

print("--New Last Used date: " + str(qotdLastUsedDateNow))

#---------------

wks.update_acell('g'+strQotdRandomID,qotdLastUsedDateNow) #update date

print("--Last Used Date column updated")



# Call the bash script to create an image from the text

qotdShell = "bash"
qotdImageScript = "qotd_screenshot.sh"

qotdAuthor = str(wks.acell('c'+strQotdRandomID).value)
qotdQuote = str(wks.acell('d'+strQotdRandomID).value)


subprocess.call([qotdShell,qotdImageScript,qotdAuthor,qotdQuote])

#tweetme(qotdQuote, qotdHashtag, "output.png")


#TODO
# [ ] 2015-05-20 Replace Random quote code with an algorithm using 'qotd_usage_counter' and 'qotd_last_used_date' to determine which qoute to use next
# [x] 2015-05-20 Fix: qotd_screenshot.sh: line 3: [: missing `]'  in bash script
# [ ] 2015-05-20 Add tweet interface
# [x] 2015-05-20 Create form to add new quotes
# [x] 2015-05-23 Import Twython and add function to take tweet text and gif and upload. Need to edit bash script so it doesn't display picture 2021-07-26 done
# [x] 2015-05-24 Change font in bash imagemagick script
# [-] 2015-05-24 Add hashtags to bash imagemagick script
# [ ] 2015-05-24 Randomise theme to predefined styles in bash imagemagick script
# [ ] 2015-05-24 Code to truncate longer quotes taking into account hashtags
# [ ] 2021-07-26 Move app and dependencies into a docker container
# [x] 2021-07-27 Tag authors with a twitter account in the tweet