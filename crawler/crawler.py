# import requests
# from bs4 import BeautifulSoup

# def get_data_from_web():
#     url = "https://example.com"
#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Example: get page title
#     return soup.title.string.strip()



import requests
from bs4 import BeautifulSoup

def get_web_data():
    url = "https://example.com"   # replace later with real site
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Example: get title
    return soup.title.string.strip()