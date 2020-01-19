import tweepy
from time import sleep
import random
import os
import sys
import threading
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


# setup OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def from_image():
    while True:
        try:
            path = "images"
            _files = os.listdir(path)
            number = random.randint(0, len(_files) - 1)
            file_ = _files[number]
            image_name = path+"/"+file_
            res = api.media_upload(image_name)
            media_id = []
            media_id.append(res.media_id)
            print(media_id)
            api.update_status(status="Daily Penn Pic! #Penn", media_ids=media_id)
            # wait one day in between
            sleep(86400)

        except tweepy.TweepError as e:
            print(e.reason)
            sleep(10800)


def from_text():
    while True:
        # open the text file
        my_file = open('AMND.txt', 'r')

        # read line by line and store
        file_lines = my_file.readlines()

        # close the file
        my_file.close()

        for line in file_lines:
            line = line.strip()

            CHARACTERS = ('LYSANDER', 'DEMETRIUS', 'HERMIA', 'HELENA',
                        'OBERON', 'TITANIA', 'PUCK', 'ROBIN GOODFELLOW')
            ENDINGS = ('.', '!', '?')

            if line.startswith(CHARACTERS) and line.endswith(ENDINGS):
                try:
                    print(line)
                    if line != '\n':
                        api.update_status("A random line from A Midsummer Night's Dream:\n"+line)
                        # wait six hours before doing it again
                        sleep(21600)
                    else:
                        sleep(30)
                        pass

                except tweepy.TweepError as e:
                    print(e.reason)
                    sleep(10800)


def from_hashtag():
    while True:
        for tweet in tweepy.Cursor(api.search, q='#PennEngineering').items():
            try:
                print('\nTweet by: @' + tweet.user.screen_name)

                tweet.retweet()
                print('Retweeted the tweet')

                tweet.favorite()
                print('Favorited the tweet')

                if not tweet.user.following:
                    tweet.user.follow()
                    print('Followed the user')

                # wait for three hours before trying again
                sleep(10800)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(10800)

            except StopIteration:
                break


def from_user():
    while True:
        for tweet in tweepy.Cursor(api.user_timeline, id=418824121).items(2):
            try:
                # Add \n escape character to print() to organize tweets
                print('\nTweet by: @' + tweet.user.screen_name)

                # Retweet and favorite tweets as they are found
                tweet.retweet()
                print('Retweeted the tweet')

                tweet.favorite()
                print('Favorited the tweet')

                # wait three hours before trying again
                sleep(10800)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(10800)
            except StopIteration:
                break


t1 = threading.Thread(target=from_image)
t2 = threading.Thread(target=from_text)
t3 = threading.Thread(target=from_hashtag)
t4 = threading.Thread(target=from_user)
t1.start()
t2.start()
t3.start()
t4.start()
