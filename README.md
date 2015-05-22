![Alt Text](https://github.com/Gitesh/qotd-screenshot/raw/master/output.gif)


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
       bash qotd_screenshot.sh "\<AUTHOR_NAME\>" "\<QUOTE_TEXT\>"


Example: 

       bash qotd_screenshot.sh "Douglas Adams" "Thanks for all the fish"




----------------------------------------
#3. Spreadsheet hosted on Google Drive#
----------------------------------------


| Timestamp           | ID | Author Name             | Quote                                                                                                                  | Hashtags                   | Usage Counter | Last Used Date           | Validated status |
|---------------------|----|-------------------------|------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------|--------------------------|------------------|
| 21/05/2015 16:20:32 | 2  | Charles Orlando         | If they can leave you so easily, they were never really meant for you. Let them go.                                    | #Love                      | 0             | 0                        | 1                |
| 22/05/2015 16:20:32 | 3  | Anon                    | If you go for every opportunity you end up chasing everyone else's dreams except your own.                             | #opportunity #dreams       | 0             | 0                        | 1                |
| 23/05/2015 16:20:33 | 4  | Isaac Asimov            | To succeed, planning alone is insufficient. One must improvise as well.                                                | #pmChat #ProjectManagement | 0             | 0                        | 1                |
| 24/05/2015 16:20:34 | 5  | Thomas Edison           | The value of an idea lies in the using of it.                                                                          | #ideas                     | 0             | 0                        | 1                |
| 25/05/2015 16:20:35 | 6  | Niels Henrik David Bohr | No, no, you're not thinking, you're just being logical                                                                 | #logic #ideas              | 0             | 0                        | 1                |
| 26/05/2015 16:20:36 | 7  | Niels Henrik David Bohr | An expert is a man who has made all the mistakes which can be made, in a narrow field                                  | #pmChat #ProjectManagement | 0             | 0                        | 1                |
| 27/05/2015 16:20:37 | 8  | Douglas Adams           | If you have a flood, you need to plug the leak before mopping the floor                                                | #pmChat #ProjectManagement | 0             | 0                        | 1                |
| 28/05/2015 16:20:38 | 9  | Douglas Adams           | When trying to make something completely fool proof, it is easy to underestimate the ingenuity of complete fools       | #pmChat #ProjectManagement | 1             | 2015-05-22T21:54:17.367Z | 1                |
| 29/05/2015 16:20:32 | 10 | Dylan Thomas            | When one burns one's bridges, what a very nice fire it makes.                                                          | #MoveForward               | 0             | 0                        | 1                |
| 30/05/2015 16:20:32 | 11 | Eagleson's Law          | Any code of your own that you haven't looked at for six or more monthsmight as well have been written by someone else. | #code #dev                 | 0             | 0                        | 1                |
| 10/06/2015 16:20:32 | 12 | Anon                    | 43rd Law of Computing: Anything that can go wrfortune: Segmentation fault ― core dumped                                | #code #dev                 | 0             | 0                        | 1                |
| 11/06/2015 16:20:32 | 13 | Anon                    | A LISP programmer knows the value of everything, but the cost of nothing.                                              | #code #lisp                | 0             | 0                        | 1                |
| 12/06/2015 16:20:32 | 14 | Oliver Wendell Holmes   | A child's education should begin at least 100 years before he is born.                                                 | #education #poverty        | 3             | 2015-05-21T00:34:06.275Z | 1                |
| 13/06/2015 16:20:32 | 15 | William James           | A great many people think they are thinking when they are merely rearranging their prejudices.                         | #pmChat #stakeholders      | 0             | 0                        | 1                |

AppsScript added to spreadsheet to auto populate ID, Usage Counter, Last Published Date,  Validated Status rows with default values. Triggered on form submission (https://docs.google.com/forms/d/1eYcmD0qVtt4_qMLKH2_Hmh7Jp7JiQzhfQTTHWtQI5Ns/viewform)

    function onFormSubmit(e) {
    
           var sheet = SpreadsheetApp.getActiveSheet();
           var row =  SpreadsheetApp.getActiveSheet().getLastRow();
           
           sheet.getRange(row,2).setValue(row);
           sheet.getRange(row,6).setValue(0);
           sheet.getRange(row,7).setValue(0);
           sheet.getRange(row,8).setValue(0);
           
    }



@gitesh
