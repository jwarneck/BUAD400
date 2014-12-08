from operator import itemgetter
from sentiment import *
stop_words = "/Users/Administrator/Documents/GitHub/BUAD400/twitter/HWassignment2/stopWords.txt"
#stop_words = "/Users/jordanwarnecke/GitHub/BUAD400/twitter/HWassignment2/stopWords.txt" #stop_words file
filename2 = "/Users/Administrator/Documents/GitHub/BUAD400/twitter/HWassignment2/cloud_list.txt"
#filename2 = "/Users/jordanwarnecke/GitHub/BUAD400/twitter/HWassignment2/cloud_list.txt"
raw = "/Users/Administrator/Documents/GitHub/BUAD400/twitter/HWassignment2/TWEET_DATA.txt"
#raw = "/Users/Administrator/Documents/GitHub/BUAD400/twitter/tweet_data/nov-12.txt" #raw tweet data



#get stop words
def get_stop_words(stop_words):
	lines = open(stop_words, 'r').readlines()
	stop_words = []
	for line in lines:
		words = line.lower().strip().replace("\n", " ").split(' ')
		words = filter(lambda x: x != '', words)
		if len(words) == 2:
			stop_words[words[0]] = float(words[1])
	return stop_words


# Pulls any stop-words from passed-in text
# then removes any symbols from words and
# derives an average score for the passage.
# Returns dict object inferred_coded_words that
# contains sentiment scores for words in the text
# and a word count.

def infer_word_sentiments(codes, text):
	inferred_coded_words = {}
	stopwords = get_stop_words(stop_words)
	#print("TEXT = " )
	#print(text)
	#text.filter(t != None)
	
	for t in text:
		#print(t)
		#t.filter(None, x)
		if (t != None):
			words = t.split(' ')
			for w in words:
				if "http" in w or '@' in w or '#' in w or w == '' or w == '"':
					break
			
				if ((w not in stopwords) and (not codes.has_key(w))):
					if not inferred_coded_words.has_key(w):
						inferred_coded_words[w] = [sentiment_score(codes, t), 1]
					else:
						inferred_coded_words[w][0] += sentiment_score(codes, t)
						inferred_coded_words[w][0] /= 2
						inferred_coded_words[w][0] += 1
	
	return inferred_coded_words


# Takes in a sentiment coded words and JSON tweet data
# rips text from the tweets and passes this list of text
# to infer_word_sentiments.
# Returns inferred_coded_words

def infer_tweet_word_sentiments(codes, tweets):
	tweet_text = []
	for tweet in tweets:
		tweet_text.append(text(tweet, ['text']))
	inferred_coded_words = infer_word_sentiments(codes, tweet_text)
	return inferred_coded_words
	
	'''
	text = read_tweets(tweets)
	sentiment_score_dict = infer_word_sentiments(codes, text)
	return sentiment_score_dict
	'''


# Takes in sentiment_score_dict, number n, and direction, 1 being positive
# 0 being negative. Returns tuples in highest magnitude order.

def top_n_words(sentiment_score_dict, n, direction=1):
	if direction == 0:
		return sorted(sentiment_score_dict.items(), key = itemgetter(1))[:n]
	else:
		return sorted(sentiment_score_dict.items(), key = itemgetter(1), reverse = True)[:n]
	


# Uses top_n_words and then prints a list of words, one word per line
# adding each word to the list x number of times based on proportion
# of top_n score.

def build_word_cloud_list(sentiment_score_dict, n, filename, direction=1):
	
	top_n = top_n_words(sentiment_score_dict, n, direction)
	
	#wfile = open("./cloud_list.txt")
	wfile = open("/Users/Administrator/Documents/GitHub/BUAD400/twitter/HWassignment2/" + filename + ".txt", 'w')
	
	
	for t in top_n:
		#print("THIS IS T")
		print(t)
		num = (int)((abs(t[1][0])*10) + (t[1][0] * 10))
		print(num)
		for i in range(num):
			wfile.write(t[0] + "\n")
		wfile.write("\n")
	wfile.close()
	
	
	'''
	word_cloud_list = []
	# use nltk .freq() to determine frequency of words used
	# add these to word_cloud_list
	output_file.write(word_cloud_list)
	'''

# Uses above functions to print word proportions to screen and a list
# when directed by input.

def score_sentiments(codes, tweets, direction = 1, filename = None, n = 10):
	
	sentiment_codes = infer_tweet_word_sentiments(codes, tweets)
	
	print top_n_words(sentiment_codes, n, direction)
	
	if filename != None:
		build_word_cloud_list(sentiment_codes, n, filename, direction)
	
