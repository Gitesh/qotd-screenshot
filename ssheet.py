import json
import gspread
import subprocess
from random import randint
from oauth2client.client import SignedJwtAssertionCredentials



##DEPENDENDCIES##
#set up new service account credentials at console.developers.google.com
#sudo apt-get install gspread
#sudo apt-get install pip
#sudo pip install --upgrade oauth2client

json_key = json.load(open('API Project-8bbb352bcc8c.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

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

print wks.acell('a'+strQotdRandomID)  #TimeStamp
print wks.acell('b'+strQotdRandomID)  #ID
print wks.acell('c'+strQotdRandomID)  #Author
print wks.acell('d'+strQotdRandomID)  #Quote
print wks.acell('e'+strQotdRandomID)  #Hashtag
print wks.acell('f'+strQotdRandomID)  #Usage counter
print wks.acell('g'+strQotdRandomID)  #Last used date
print wks.acell('h'+strQotdRandomID)  #Validated status


#Write code to increase the counter for the text

qotdLastUsedCounter = int(wks.acell('f'+strQotdRandomID).value)

qotdLastUsedCounter += 1

#qotdLastUsedCounterNow += int(qotdLastUsedCounter)

#Update usage counter and date
wks.update_acell('f'+strQotdRandomID,qotdLastUsedCounter) #update counter

qotdLastUsedDateNow = wks.updated
wks.update_acell('g'+strQotdRandomID,qotdLastUsedDateNow) #update date





# Call the bash script to create an image from the text

qotdShell = "bash"
qotdImageScript = "qotd_screenshot.sh"

qotdAuthor = str(wks.acell('c'+strQotdRandomID).value)
qotdQuote = str(wks.acell('d'+strQotdRandomID).value)


subprocess.call([qotdShell,qotdImageScript,qotdAuthor,qotdQuote])


#TODO
# 2015-05-20 Replace Random quote code with an algorithm using 'qotd_usage_counter' and 'qotd_last_used_date' to determine which qoute to use next
# 2015-05-20 Fix: qotd_screenshot.sh: line 3: [: missing `]'  in bash script
# 2015-05-20 Add tweet interface
# 2015-05-20 Create form to add new quotes
