import tweepy
from credentials import *
from time import sleep

# setup OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def from_text():
    # open the text file
    my_file = open('verne.txt', 'r')

    # read line by line and store
    file_lines = my_file.readlines()

    # close the file
    my_file.close()

    for line in file_lines:
        try:
            print(line)

            if line != '\n':
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(3600)


for tweet in tweepy.Cursor(api.search, q='#PennEngineering', lang='en').items(10):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        tweet.favorite()
        print('Favorited the tweet')

        if not tweet.user.following():
            tweet.user.follow()
            print('Followed the user')

        # wait for an hour
        sleep(3600)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
