from twitter_util import *
from sentiment import *

tweets = read_tweets("tweet_data/nov-12.txt")
#coded_states
states = read_states("data/states.txt")

#

for t in tweets[:100]:
	try:
		print(extract_states(states, text(t, ['user', 'location'])))
	except:
		print("NONE")

print(top_n_states(states, codes, tweets))