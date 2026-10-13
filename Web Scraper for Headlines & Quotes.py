import json
import requests
from bs4 import BeautifulSoup

def scrape_tech_headlines():
    # Target website: Hacker News (publicly scrapeable tech headlines)
    url = "https://news.ycombinator.com/"
    
    # Add a User-Agent header to mimic a real browser request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return
        
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Inspect and extract headline tags (.titleline > a contains the article title and link)
    headline_tags = soup.select('.titleline > a')
    
    headlines = []
    # Extract top 10 headlines
    for index, tag in enumerate(headline_tags[:10], start=1):
        title = tag.get_text()
        link = tag.get('href')
        headlines.append({
            "rank": index,
            "title": title,
            "link": link
        })
        
    # Format and save data into a clean JSON file
    filename = "tech_headlines.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(headlines, file, indent=4)
        
    print(f"Successfully scraped {len(headlines)} headlines and saved them to '{filename}'!")
    
    # Display the results in the terminal
    print("\n--- Latest Tech Headlines Extracted ---")
    for item in headlines:
        print(f"{item['rank']}. {item['title']}")
        print(f"   Link: {item['link']}\n")

if __name__ == "__main__":
    scrape_tech_headlines()