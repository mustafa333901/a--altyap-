import requests
import tweepy
from bs4 import BeautifulSoup

# --------------------
# 7. Sosyal Medya Entegrasyonları
# --------------------
class WebScraping:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        """Web sayfasından içerik çeker."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()

    def fetch_headlines(self):
        """Web sayfasındaki başlıkları alır."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = [h.text for h in soup.find_all('h1')]
        return headlines

class InstagramIntegration:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://graph.instagram.com/'

    def fetch_posts(self, user_id, count=5):
        """Instagram'dan son paylaşımları alır."""
        url = f"{self.base_url}{user_id}/media?fields=id,caption,media_type,media_url,timestamp&limit={count}&access_token={self.access_token}"
        response = requests.get(url)
        posts = response.json()['data']
        post_data = []
        for post in posts:
            post_data.append({
                "caption": post.get("caption"),
                "media_url": post.get("media_url"),
                "timestamp": post.get("timestamp")
            })
        return post_data

class TwitterIntegration:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(consumer_key=api_key,
                                             consumer_secret=api_secret_key,
                                             access_token=access_token,
                                             access_token_secret=access_token_secret)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, hashtag, count=100):
        """Belirli bir hashtag ile ilgili tweet'leri alır."""
        tweets = tweepy.Cursor(self.api.search, q=hashtag, lang="en").items(count)
        tweet_data = []
        for tweet in tweets:
            tweet_data.append({
                "text": tweet.text,
                "created_at": tweet.created_at,
                "user": tweet.user.screen_name
            })
        return tweet_data
