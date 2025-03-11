import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_market_news():
    url = "https://finance.yahoo.com/news/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h3")
    headlines = [article.text for article in articles if article.text]

    return headlines

if __name__ == "__main__":
    news = get_market_news()
    df = pd.DataFrame(news, columns=["Headline"])
    df.to_csv("market_news.csv", index=False)
    print("Market news saved to market_news.csv")
