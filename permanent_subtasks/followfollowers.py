import tweepy
import logging
import time
import os 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



id = '1387440864889278465'


def follow_followers(client):
    logger.info("Retrieving and following followers")
    for follower in client.get_users_followers(id=id, user_fields=['profile_image_url']):
        if follower not in client.get_users_following(id=id, user_fields=['profile_image_url']):
            i = 0
            length = str(len(follower))
            while i != length:
                print(follower[i].id)
                client.follow_user(follower[i].id)
                i = i + 1

def main():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    bearer_token= os.getenv('BEARER_TOKEN')
    
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, wait_on_rate_limit=False)
    
    while True:
        follow_followers(client)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
