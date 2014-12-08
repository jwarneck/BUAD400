from twitter_util import *
filename = "/Users/jordanwarnecke/GitHub/BUAD400/twitter/HWassignment2/stopWords.txt" #stop_words file
text = "/Users/jordanwarnecke/GitHub/BUAD400/twitter/tweet_data/nov-12.txt" #raw tweet data
output_file = "/HWassignment2/output_file.txt"
tweets = read_tweets(text)


#get stop words
def get_stop_words(filename):
	lines = open(filename, 'r').readlines()
	stop_words = []
	print(lines)
	for line in lines:
		words = line.lower().strip().replace("\n", " ").split(' ')
		words = filter(lambda x: x != '', words)
		if len(words) == 2:
			stop_words[words[0]] = float(words[1])
	return stop_words


#
def infer_word_sentiments(codes, text):
	sentiment_coded_words = {}
	# check text against coded_words
	# assign a score to the words
	return sentiment_coded_words


#
def infer_tweet_word_sentiments(codes, tweets):
	sentiment_score_dict = {}
	text = read_tweets(tweets)
	sentiment_score_dict = infer_word_sentiments(codes, text)
	return sentiment_score_dict


#
def top_n_words(sentiment_score_dict, n, direction=1):
	score_list = []
	create_tuples(sentiment_score_dict, n)
	append tuples to score_list following magnitude order
	return score_list


#
def build_word_cloud_list(sentiment_score_dict, n, filename, direction=1):
	word_cloud_list = []
	# use nltk .freq() to determine frequency of words used
	# add these to word_cloud_list
	output_file.write(word_cloud_list)


def score_sentiments(codes, tweets, direction = 1, filename = False):
	if (filename = True):
		# prints word cloud to output file
		build_word_cloud_list(sentiment_score_dict, n, filename)
	else:
		# print tuples in order of magnitude, each on a new line
		while (sentiment_score_dict.hasNext()):
			print(sentiment_score_dict)
			print("\n")