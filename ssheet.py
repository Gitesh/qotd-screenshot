#!/usr/bin/python

import json
import gspread
import subprocess
from random import randint
#from oauth2client.client import SignedJwtAssertionCredentials
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



##DEPENDENDCIES##
#set up new service account credentials at http://console.developers.google.com
#give the account access to two api scopes: drive and spreadsheet
#set up a new twitter application at https://apps.twitter.com and note credentials
#install the following local dependencies (ubuntu):
#sudo apt-get install gspread 
#sudo apt-get install pip
#sudo pip install --upgrade oauth2client
#sudo apt install imagemagick


# json_key = json.load(open('API Project-8bbb352bcc8c.json'))

json_key = json.load(open('qotd-17-6cfc9e0e9808.json'))

#scope = ['https://spreadsheets.google.com/feeds']
scopes = [
	'https://www.googleapis.com/auth/spreadsheets',
	'https://www.googleapis.com/auth/drive'
	]

#credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
#gc = gspread.authorize(credentials)

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

#-----------check the validated status--------------------------

intValidatedStatus = Null

intValidatedStatus = int(wks.acell('h'+strQotdRandomID).value)  #Read Validated status column from google sheet

print("----------------validatedStatusRow " + strQotdRandomID)
print("----------------validatedStatus " + str(intValidatedStatus))

while intValidatedStatus < 1:
  if intValidatedStatus == 0:
    print ("----validated 00000000000000000000")
    print("-----re reading " + (str(intValidatedStatus))) #re read
    qotdRandomID = randint(2,qotdQotdIDLength)
    strQotdRandomID = str(qotdRandomID)
    strValidatedStatus = wks.acell('h'+strQotdRandomID).value  #Read Validated status column from google sheet  
    intValidatedStatus = (int(str(strValidatedStatus)))
    print("new validated status " + (str(strValidatedStatus)))
    continue
print ("eXited continutes")

#----------validated status checked and a random valid quote selected

print (wks.acell('a'+strQotdRandomID))  #TimeStamp
print (wks.acell('b'+strQotdRandomID))  #ID
print (wks.acell('c'+strQotdRandomID))  #Author
print (wks.acell('d'+strQotdRandomID))  #Quote
print (wks.acell('e'+strQotdRandomID))  #Hashtag
print (wks.acell('f'+strQotdRandomID))  #Usage counter
print (wks.acell('g'+strQotdRandomID))  #Last used date
print (wks.acell('h'+strQotdRandomID))  #Validated status


#Get the length of the hashtag below and truncate the quote length for the text ONLY (but not alter the image)
qotdHashtag = wks.acell('e'+strQotdRandomID).value #Quote
qotdHashtag = str(" " + qotdHashtag) #add a space before the quote end and hashtag, looks neater, 




#Write code to increase the counter for the text

qotdLastUsedCounter = int(wks.acell('f'+strQotdRandomID).value)

print ("Last Used Counter: " + str(qotdLastUsedCounter))

qotdLastUsedCounter += 1

print ("Last Used Counter+1: " + str(qotdLastUsedCounter))

#qotdLastUsedCounterNow += int(qotdLastUsedCounter)

#Update usage counter and date
wks.update_acell('f'+strQotdRandomID,qotdLastUsedCounter) #update counter

print("Last used counter added to column f")

#qotdLastUsedDateNow = wks.updated #updated has been deprecated in google sheets v4
#print("DEPRECATED SPREADSHEET UPDATE VALE: " + str(wks.updated))


#---------------

from datetime import datetime

# Current date time in local system
print(datetime.now())
qotdLastUsedDateNow = str(datetime.now())


#---------------



print("New Last Used Date: " + str(qotdLastUsedDateNow))

wks.update_acell('g'+strQotdRandomID,qotdLastUsedDateNow) #update date

print("Last Used Date Updated")



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
# [ ] 2015-05-24 Change font in bash imagemagick script
# [ ] 2015-05-24 Add hashtags to bash imagemagick script
# [ ] 2015-05-24 Randomise viginette and tilt to predefined styles in bash imagemagick script
# [ ] 2015-05-24 Code to truncate longer quotes taking into account hashtags
# [ ] 2021-07-26 Move app and dependencies into a docker containerg
# [ ] 2021-07-27 Tag authors with a twitter account in the tweet