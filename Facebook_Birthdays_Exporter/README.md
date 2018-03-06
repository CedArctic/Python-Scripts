# Facebook Birthdays Calendar to CSV
I needed to export my friends birthdays from facebook to a file for a project but found out that it's not directly possible. I could have used the API, but that was unreliable and not worth the trouble, hence this python script was born.

# Requirements:
csv & openpyxl for python.

# How to use:
1. Go to your facebook calendar page and export your calendar to a mail client as described here: https://www.facebook.com/help/152652248136178/ I used Outlook but it can be done with various other applications.
2. Through your mail client try to share or send the calendar, this will create a .ics file - we need this. In Outlook you can get this file by "Sharing" the calendar with someone else, this will create a mail draft with the .ics file attached - right click and save it somewhere.
3. Open the ics file with a spreadsheet editor. I used Excel with the default import settings, only changed encoding from ANSI to UTF8.
4. Save the file as an Excel compatible document (I saved mine as an .xlsx)
5. Run the Python Script in my repository (csv and openpyxl must be installed) and drag n drop the Excel file at the prompt and hit enter.

Results will appear in a Birthdays.csv file in the script's directory.
