import requests
from bs4 import BeautifulSoup

def fetch_headlines(url, tag="h2", class_name=None):
    try:
        # Send GET request
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines
        if class_name:
            headlines = [h.get_text(strip=True) for h in soup.find_all(tag, class_=class_name)]
        else:
            headlines = [h.get_text(strip=True) for h in soup.find_all(tag)]

        return headlines

    except Exception as e:
        print(f"Error: {e}")
        return []

def save_headlines(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")

if __name__ == "__main__":
    # Example: BBC News
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url, tag="h3")  # BBC uses <h3> for headlines
    save_headlines(headlines)
    print("✅ Headlines saved to headlines.txt")
