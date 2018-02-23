# Dependencies: requests, time, https://github.com/randomchars/pushbullet.py

import sys
import os
import requests
import time
from pushbullet import Pushbullet

# Pushbullet init using https://github.com/randomchars/pushbullet.py
bullet = Pushbullet('API_KEY')

# Start a session
print("Starting Scraper...")
site = requests.session()

# Create a dictionary with the login credentials, username and password are the names the website uses for these variables, if your website uses other variable names, change accordingly
login_data = dict(username='YOUR_USERNAME', password='YOUR_PASSWORD')

# Post the credentials through the website_url/loginActionName, use your web browser to find your loginActionName
print("Logging in...")
site.post('http://WEBSITE_URL/LOGIN_ACTION', data=login_data)

# Get the data we're interested in after logging in
print("Scraping...")
scrape1 = site.get('http://URL_TO_SCRAPE')
scrapeLength1 = scrape1.text.__sizeof__()
print("Scrape size: ", scrapeLength1)
print("Standing by for updates...")

# Loop indefinitely
while True:

    # Sleep for 300 seconds and then scrape again
    time.sleep(300)

    scrape2 = site.get('http://URL_TO_SCRAPE')
    scrapeLength2 = scrape1.text.__sizeof__()

    # Compare size of two scrapes, if the new scrape size is bigger, it means the site got updated
    if scrapeLength2 > scrapeLength1 :
        print("Update found, size: ", scrapeLength2)
        print("Pushing to devices")

        # Set the new scrape length as the new comparison length
        scrapeLength1 = scrapeLength2

        # Push notification to device
        push = bullet.push_link("Exam Site Updated", "http://UR_TO_SCRAPE")
