import tweepy
from time import sleep
import random
import os
import sys
import threading
from os import environ

# this grabs the secret twitter credentials from the heroku environmental variables
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# one hour interval, will be used for frequency of running different threads
# sleep() requires the time in seconds
HOUR = 60 * 60

# setup OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# looks in the supplied /images directory, grabs a random image, tweets it out


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
            api.update_status(status="Daily Penn Pic! #Penn",
                              media_ids=media_id)
            # wait one day in between
            sleep(HOUR * 24)

        except tweepy.TweepError as e:
            print(e.reason)
            sleep(HOUR)  # if hit an error, try again in an hour

# looks in the text file, grabs lines that satisfy conditions in order, tweets them out


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
                        api.update_status(
                            "A random line from A Midsummer Night's Dream:\n"+line)
                        # wait one hour before doing it again
                        sleep(HOUR)
                    else:
                        sleep(5)
                        pass

                except tweepy.TweepError as e:
                    print(e.reason)
                    sleep(HOUR)  # if error, try again in an hour

# searches twitter for recent usage of supplied hashtag, then RTs / favs / follows the user who tweeted something using the hashtag.


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
                sleep(HOUR * 3)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(HOUR)

            except StopIteration:
                break

# checks if there are any new tweets from the supplier user @PennEngineers and RTs them if so.


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
                sleep(HOUR * 3)

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(HOUR)
            except StopIteration:
                break

def wakeup_heroku():
    while True:
        print("Wake up!")
        sleep(600)

# multi-threaded so that each function can have different sleep times.
# This might be overkill but it was easy.
t1 = threading.Thread(target=from_image)
t2 = threading.Thread(target=from_text)
t3 = threading.Thread(target=from_hashtag)
t4 = threading.Thread(target=from_user)
t5 = threading.Thread(target=wakeup_heroku)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
