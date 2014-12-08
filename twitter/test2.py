from twitter_util import *

text = read_texts("tweet_data/apple.txt")

for t in tweets:
	print(text(t, ['user', 'screen_name']))