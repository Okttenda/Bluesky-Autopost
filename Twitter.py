import tweepy
import tweepy.client
from dotenv import load_dotenv
import os

def login():
    load_dotenv()
    apiKey = os.getenv("API_KEY")
    apiKeySecret = os.getenv("API_KEY_SECRET")
    bearerToken= os.getenv("BEARER_TOKEN")
    accessToken = os.getenv("ACCESS_TOKEN")
    accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")
    client = tweepy.Client(apiKey=apiKey, apiKeySecret=apiKeySecret, bearer_token=bearerToken, access_token=accessToken, access_token_secret=accessTokenSecret)
    return client
