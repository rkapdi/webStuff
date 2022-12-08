import requests
import email
import smtplib
import time

# URL of the website to check
url = "https://www.example.com"

# Interval (in seconds) to check for updates
interval = 60

# Email address to send notifications to
to_email = "user@example.com"

# Email server settings
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "user@example.com"
smtp_password = "password"

# Send a GET request to the website and save the response
response = requests.get(url)

# Check the date of the last modification of the website
last_modified = response.headers["Last-Modified"]

# Start a while loop to check for updates at regular intervals
while True:
    # Sleep for the specified interval
    time.sleep(interval)

    # Send a GET request to the website and save the response
    response = requests.get(url)

    # Check the date of the last modification of the website
    current_modified = response.headers["Last-Modified"]

    # If the website has been updated
    if current_modified != last_modified:
        # Update the date of the last modification
        last_modified = current_modified

        # Create an email message
        msg = email.message.EmailMessage()
        msg.set_content(f"The website {url} has been updated!"
