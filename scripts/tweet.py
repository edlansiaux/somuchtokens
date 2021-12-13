import tweepy
import logging
import time
import os 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#Check mention and tweets extraction

def check_mentions(client, id, keywords, since_id, extracted):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    tweets = client.get_users_mentions(id=id, since_id=since_id)
    liked = client.get_liked_tweets(id=id, user_fields=['profile_image_url'])
    for tweet in tweets.data:
      if any(keyword in tweet.text.lower() for keyword in keywords):
        if all(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet in liked.data:
              client.like(tweet.id)
            else:
              extracted.append(tweet.text)
            

#Main
def main():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    bearer_token= os.getenv('BEARER_TOKEN')

    id = '1387440864889278465'
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, wait_on_rate_limit=True)
    
    extracted =[]

    since_id = 1
    while True:
        since_id = check_mentions(client, id, ["create", "name", "symbol", "address"], since_id, extracted)
        logger.info("Waiting...")
        time.sleep(20)

main()
