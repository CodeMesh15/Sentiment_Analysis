import tweepy
import pandas as pd

# Set up Twitter API (Get keys from developer.twitter.com)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def get_market_tweets(keyword="stock market", count=50):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(count)
    data = [[tweet.full_text] for tweet in tweets]
    return data

if __name__ == "__main__":
    tweets = get_market_tweets()
    df = pd.DataFrame(tweets, columns=["Tweet"])
    df.to_csv("market_tweets.csv", index=False)
    print("Market tweets saved to market_tweets.csv")
