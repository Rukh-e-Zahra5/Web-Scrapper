import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = "https://giki.edu.pk/news"  # Hypothetical news section URL

try:
    # Send a GET request to the website
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the news elements (update the class names based on actual website structure)
    # Example: Let's assume news articles are in 'div' tags with class 'news-item'
    news_items = soup.find_all('div', class_='news-item')

    # Create lists to store extracted data
    headlines = []
    dates = []

    for item in news_items:
        # Extract the headline and date (adjust selectors based on actual HTML structure)
        headline = item.find('h2', class_='headline').get_text(strip=True) if item.find('h2', class_='headline') else 'No headline'
        date = item.find('span', class_='date').get_text(strip=True) if item.find('span', class_='date') else 'No date'
        
        # Append to lists
        headlines.append(headline)
        dates.append(date)

    # Create a CSV file and write the data to it
    with open('news_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Headline", "Date"])  # Header row
        for headline, date in zip(headlines, dates):
            writer.writerow([headline, date])

    print("Data extracted and saved to news_output.csv")

except requests.RequestException as e:
    print(f"Error during requests to {url}: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
