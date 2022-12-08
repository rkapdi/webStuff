import requests
import json

# API URL
api_url = "https://trends.google.com/trends/api/explore"

# Prompt the user for the keyword(s)
keywords = input("Enter the keyword(s) to check, separated by commas: ")

# Split the input string into a list of keywords
keywords = keywords.split(",")

# Loop through each keyword
for keyword in keywords:
    # Send a GET request to the API and save the response
    response = requests.get(api_url, params={"q": keyword})

    # Load the response data as JSON
    data = json.loads(response.text)

    # Get the past popularity data
    past_popularity = data["default"]["timelineData"][0]["value"][0]

    # Get the probabilistic popularity data
    probabilistic_popularity = data["default"]["averages"][0]

    # Print the keyword and the popularity scores
    print(f"Keyword: {keyword}")
    print(f"Past popularity: {past_popularity}/100")
    print(f"Probabilistic popularity: {probabilistic_popularity}/100")
    print()
