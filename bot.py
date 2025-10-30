import tweepy
import random
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def load_tweets():
    with open('tweets.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

TWEETS = load_tweets()
posted_today = []

def post_tweet():
    try:
        client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET
        )
        
        available = [t for t in TWEETS if t not in posted_today]
        if not available:
            posted_today.clear()
            available = TWEETS
            
        tweet = random.choice(available)
        posted_today.append(tweet)
        
        response = client.create_tweet(text=tweet)
        print(f"✅ {datetime.now()} POSTED: {tweet[:60]}...")
        return True
        
    except Exception as e:
        print(f"❌ {datetime.now()} ERROR: {e}")
        return False

def main():
    print("🤖 AI42 Bot - 24/7 Mode")
    print(f"📝 {len(TWEETS)} tweets loaded")
    print("📅 Posts 3-5x per day")
    
    while True:
        now = datetime.now()
        hour = now.hour
        
        if hour in [7,8,9,10,12,13,14,16,17,18,20,21,22,23] and random.random() < 0.15:
            post_tweet()
            time.sleep(3600)
        
        time.sleep(600)

if __name__ == "__main__":
    main()
