from NEWhw2 import *
from sentiment import *
#from twitter_util import *

#print(get_stop_words(filename))

codes = get_sentiment_codes("/Users/Administrator/Documents/GitHub/BUAD400/twitter/AFINN-111.txt")
#codes = get_sentiment_codes("/Users/jordanwarnecke/GitHub/BUAD400/twitter/data/AFINN-111.txt")
tweets = read_tweets("/Users/Administrator/Documents/GitHub/BUAD400/twitter/TWEET_DATA.txt")
#tweets = read_tweets("/Users/Administrator/Documents/GitHub/BUAD400/twitter/HWassignment2/TWEET_DATA.txt")
#tweets = read_tweets("/Users/jordanwarnecke/GitHub/BUAD400/twitter/nov-12.txt")

score_sentiments(codes, tweets, direction = 1, filename = "cloud_list", n = 10)