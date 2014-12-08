from twitter_util import *
from sentiment import *

#tweets = read_tweets("tweet_data/weather.txt")
tweets = read_tweets("tweet_data/weather.txt")

# Printing raw tweets (raw JSON data)
for t in tweets[1:5]:
	print (t)

# Read and print raw texts 
#texts = read_texts("tweet_data/apple.txt")
texts = read_texts("tweet_data/apple.txt")
for t in texts[1:5]:
	print(t)

# Get the usernames of the tweeters
for t in tweets:
	try:
		print(text(t, ['user', 'screen_name']))
	except:
		print("<Cannot Retrieve Screen Name>")


codes = get_sentiment_codes("data/AFINN-111.txt")
for i in codes.items()[0:5]:
	print(i)


for t in tweets[:20]:
	print(str(sentiment_score(codes, text(t), False)) + ": " + text(t))

happiest = top_n_tweets(tweets, codes, 10, 1)
saddest = top_n_tweets(tweets, codes, 10, -1)
print(' ')
print(' ')
print(' ')
print('HAPPIEST TWEETS: ')
for t in happiest:
	print(' ' + t)
print(' ')
print('SADDEST TWEETS: ')
for t in saddest:
	print(' ' + t)