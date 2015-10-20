import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'yMZ991XvPhjy9aqig3dC5a19R'
consumer_secret = 'BWeI0PvxZZRzkDLcoogOIlWVFJT9HQ4Ushl4YI8eJ2d116ahPU'
access_token = '191703012-1Ee2zfKEuVG06tdKkiWvAwAgfQsreZbSazKiDU6y'
access_secret = 'W5ANGYQ91hxeN47f2c6UG9ONwApMwq1N2L2IwDQ7RLgKP'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#for status in tweepy.Cursor(api.user_timeline, id = "@suyapc").items(10):
#    print(status.text)


#### USANDO JSON 
##ESCRITA DE ARQUIVOS 

import json
import io

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need


# ESCRITA EM TXT
save_file = io.open('suyapc.txt','w', encoding='utf8')
for status in tweepy.Cursor(api.user_timeline, id = "@suyapc").items(100):
#    print(status.json)
	save_file.write(status.text +'\n')


