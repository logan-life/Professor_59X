import tweepy
from credentials import *
from time import sleep
import glob
import random
import os, sys

# setup OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# open the text file
my_file = open('AMND.txt', 'r')

# read line by line and store
file_lines = my_file.readlines()

# close the file
my_file.close()


# tweet_image(/images)


def from_image():
    path = "/Users/logan/code/src/Environments/twitter/Professor_59X/images"
    _files = os.listdir(path)
    number = random.randint(0, len(_files) - 1)
    file_ = _files[number]
    image_name = path+"/"+file_
    res = api.media_upload(image_name)
    media_id = []
    media_id.append(res.media_id)
    print(media_id)
    api.update_status(status = "Daily Penn Pic! #Penn", media_ids = media_id)
    sleep(86400)


def from_text():
    for line in file_lines:
        line = line.strip()
        # print("::"+line+"::")

        CHARACTERS = ('LYSANDER', 'DEMETRIUS', 'HERMIA', 'HELENA',
                      'OBERON', 'TITANIA', 'PUCK', 'ROBIN GOODFELLOW')
        ENDINGS = ('.', '!', '?')
        if line.startswith(CHARACTERS) and line.endswith(ENDINGS):

            try:
                print(line)
                # if line != '\n':
                #   api.update_status(line)
                # else:
                #   pass
            except tweepy.TweepError as e:
                print(e.reason)

        # sleep(2)

#@PennEngineers
#pennengineering

def from_hashtag():
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

            # wait for an hour before retweeting anything else
            sleep(3600)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

def from_user():
    for tweet in tweepy.Cursor(api.user_timeline, id=418824121).items(2):
        try:
            # Add \n escape character to print() to organize tweets
            print('\nTweet by: @' + tweet.user.screen_name)

            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')

            #sleep for 3 hours
            sleep(10800)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    

# from_text()
while True:
    #from_image()
    from_user()
