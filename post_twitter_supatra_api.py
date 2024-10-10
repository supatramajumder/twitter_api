import tweepy
from tweepy.errors import TweepyException

# My API Credentials
API_KEY = 'fxMaAy8V2JylikyeiagBCflfP'
API_SECRET_KEY = 'lUp7h8yOxOWmUC8DKY70hBV8IhMzqNiZT4Y2HJrf0N9qcXi2vq'
ACCESS_TOKEN = '148007269-TKXtMqxjrx2xY7gUPNQVUgvgeIRngq3AoXq6pmaA'
ACCESS_TOKEN_SECRET = 'KTIFlTAFpzz11vqHKRhFI6kHyjGt1IrOQROQKmjOl9T2r'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAI9WwQEAAAAAZZE84Q8WaccLl6yREXVx43C6i7s%3DubRnwUTLnCSAegdyb29ipbZanNxDbZmHJAKDTd20Ko8CyZxmNN'

# Creating a Client object
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Post a new tweet using API
tweet_text = "Hello my friends, this is posted via TwitterAPI!! --by Supatra Majumder and Loyalist College in Toronto combined project"

try:
    # Posting the tweet
    response = client.create_tweet(text=tweet_text)
    print(f"Successfully posted tweet: {response.data}")
except TweepyException as e:
    print(f"Failed to post tweet: {e}")