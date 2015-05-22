![Alt Text](https://github.com/Gitesh/qotd-screenshot/raw/master/output.gif)

![Alt Text](https://raw.githubusercontent.com/Gitesh/qotd-screenshot/master/output.gif)


----------------------------------------
#1. ssheet.py#
----------------------------------------
- Reads the Google Drive hosted spreadsheet table
- Selects a random quote (algorithm using last publish date and usage counter TBC)
- Passes the Author name and their Quote to a Bash script which in turn launches ImageMagick to create a text screenshot



----------------------------------------
#2. qotd_screenshot.sh#
----------------------------------------

Bash script to create a screenshot from the quote of the day, ready to attach to the tweet.

Dependencies:
       Imagemagick (see www.imagemagick.org) is used to create the screenshot and manipulate the image.


Useage:
       bash qotd_screenshot.sh "<AUTHOR_NAME>" "<QUOTE_TEXT>"


Example: 

       bash qotd_screenshot.sh "Douglas Adams" "Thanks for all the fish"




----------------------------------------
#3. Spreadsheet hosted on Google Drive#
----------------------------------------


qotd_id	qotd_author	qotd_quote	qotd_hashtags	qotd_usage_counter	qotd_last_used_date
1	Anon	If you go for every opportunity you end up chasing everyone else's dreams except your own.	#opportunity #dreams	1	2015-05-20T22:56:47.073Z
2	Isaac Asimov	To succeed, planning alone is insufficient. One must improvise as well.	#pmChat #ProjectManagement	2	2015-05-20T23:00:27.184Z
3	Thomas Edison	The value of an idea lies in the using of it.	#ideas	0	0
4	Niels Henrik David Bohr	No, no, you're not thinking, you're just being logical	#logic #ideas	0	0
5	Niels Henrik David Bohr	An expert is a man who has made all the mistakes which can be made, in a narrow field	#pmChat #ProjectManagement	1	2015-05-20T22:59:11.607Z
6	Douglas Adams	If you have a flood, you need to plug the leak before mopping the floor	#pmChat #ProjectManagement	1	2015-05-20T23:00:01.558Z
7	Douglas Adams	When trying to make something completely fool proof, it is easy to underestimate the ingenuity of complete fools	#pmChat #ProjectManagement	1	2015-05-20T23:00:57.268Z




@gitesh
