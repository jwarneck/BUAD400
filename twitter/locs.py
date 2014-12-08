from twitter_util import *
from sentiment import *

tweets = read_tweets("tweet_data/nov-10.txt")

for t in tweets:
	try:
		print(text(t, ['user', 'location']))
	except:
		print("UNREADABLES")