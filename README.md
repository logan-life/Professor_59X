# Professor_59X: UPenn MCIT Twitter Bot

[Follow the Professor on Twitter here.](https://twitter.com/59xProfessor)

This bot was initially developed during the inaugural hackathon event from the UPenn CIT59X student group by [Logan Ayliffe](https://twitter.com/logan_ayliffe) and Abdulla AlBadi AlDhaheri. The [MCIT program at UPenn](https://www.cis.upenn.edu/graduate/program-offerings/master-of-computer-and-information-technology/requirements/) has core courses which use the numbering convention 59(X), so that's why this bot has this name.

 This bot was written in python and uses [tweepy](http://docs.tweepy.org/en/v3.8.0/api.html#status-methods) to interact with the Twitter API and is hosted using Heroku. The initial build was created using [this tutorial from Digital Ocean.](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library) The Heroku deployment was helped along by [this post by Emily Cain](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39).

**Current features:**

- The bot can tweet lines from a text file.

- The bot can search for a particular hashtag and then interact with returned tweets, e.g. favorite / retweet / follow that user. The bot is currently monitoring [#PennEngineering.](https://twitter.com/hashtag/PennEngineering?src=hashtag_click&f=live)

- The bot can tweet a random image from a supplied directory of images. Currently tweeting images from the Penn flickr account - [the public fair use directory located here.](https://www.flickr.com/photos/universityofpennsylvania/albums/72157623638790070)

- The bot can retweet any specified user. Currently retweets stuff from [@PennEngineers.](https://twitter.com/PennEngineers)

**Future Improvements:**

- The **from_text** function could use a fair amount of improvement / expansion. Support grabbing multilines, format the text a bit better, range checking for length versus tweet constraint.

- It would be nice for **from_image** to be able to tweet an image from somewhere other than a local directory, e.g. [unsplash](https://unsplash.com/).

- For both **from_user** and **from_hashtag**, these could be expanded to include more stuff that is relevant to the MCIT student community.




