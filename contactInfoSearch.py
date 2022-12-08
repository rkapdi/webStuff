import requests
from bs4 import BeautifulSoup
import re

# URL of the website to scrape
url = "https://www.example.com"

# Download the HTML content of the website
response = requests.get(url)
html = response.text

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Initialize lists to store the scraped data
emails = []
phones = []
addresses = []

# Find all email addresses on the website
for email in soup.find_all(text=re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")):
    emails.append(email)

# Find all phone numbers on the website
for phone in soup.find_all(text=re.compile(r"\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}")):
    phones.append(phone)

# Find all addresses on the website
for address in soup.find_all(text=re.compile(r"\d{5}(?:[-\s]\d{4})?")):
    addresses.append(address)
    
# Open a text file for writing
with open("results.txt", "w") as file:
    # Write the scraped data to the file
    file.write("Email addresses:\n")
    for email in emails:
        file.write(f"- {email}\n")

    file.write("\nPhone numbers:\n")
    for phone in phones:
        file.write(f"- {phone}\n")

    file.write("\nAddresses:\n")
    for address in addresses:
        file.write(f"- {address}\n")
