import tweepy
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timezone, date

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

def get_api_v1():
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    return tweepy.API(auth)

def get_client_v2():
    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )


def get_last_ferrari_win():
    today = date.today()
    
    for year in range(today.year, 1949, -1):
        url = f"https://api.jolpi.ca/ergast/f1/{year}/constructors/ferrari/results/1.json?limit=300"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            races = data["MRData"]["RaceTable"]["Races"]
            
            if races:
                last_race = races[-1]
                win_date = datetime.strptime(last_race["date"], "%Y-%m-%d").date()
                return win_date
    return None

def build_tweet_and_image(last_win_date):
    today = date.today()
    
    days_since = (today - last_win_date).days
    
    if days_since ==0:
        text= "FERRARI WON WE ARE SO BACK"
        image_path = "so-back.png"
    
    else:
       text = f"It has been {days_since} days since Ferrari last won an F1 race it is SO OVER"
       image_path = "so-over.png"
       
    return text,image_path

def tweet_with_image(text, image_path):
    api_v1 = get_api_v1()
    client_v2 = get_client_v2()
    
    media = api_v1.media_upload(filename=image_path)
    media_id = media.media_id
    client_v2.create_tweet(text = text, media_ids = [media_id])

if __name__ == "__main__":
    last_win = get_last_ferrari_win()
    if not last_win:
        text = "ferrari has never won an F1 race it is so over time to kms"
        image_path = "so-over.png"
    else:
        text, image_path = build_tweet_and_image(last_win)

    print("Tweeting...:", text, "with", image_path)
    tweet_with_image(text, image_path)

 
