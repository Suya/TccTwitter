import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'yMZ991XvPhjy9aqig3dC5a19R'
consumer_secret = 'BWeI0PvxZZRzkDLcoogOIlWVFJT9HQ4Ushl4YI8eJ2d116ahPU'
access_token = '191703012-1Ee2zfKEuVG06tdKkiWvAwAgfQsreZbSazKiDU6y'
access_secret = 'W5ANGYQ91hxeN47f2c6UG9ONwApMwq1N2L2IwDQ7RLgKP'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def get_all_tweets(screen_name):


	#initialize a list to hold all the tweepy Tweets
	alltweets = []	

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1	
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))
			
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
					
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("realdonaldtrump")
