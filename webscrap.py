import requests
from bs4 import BeautifulSoup
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data using BeautifulSoup methods
        # (This is a hypothetical example, adjust for the structure of the website you're working with)
        title = soup.title.text
        paragraphs = soup.find_all('p')

        # Print the extracted data
        print(f"Title: {title}\n")

        for i, paragraph in enumerate(paragraphs, 1):
            print(f"Paragraph {i}: {paragraph.text}\n")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage
url_to_scrape = 'https://example.com'
url_to_scrape='https://en.wikipedia.org/wiki/Sudha_Murty'
scrape_website(url_to_scrape)
