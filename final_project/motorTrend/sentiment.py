from twitter_util import *

# For a file of sentiment-coded words, get 
# into a {<word> : <code>} form

def get_sentiment_codes(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		words = line.lower().strip().replace("\t", " ").split(' ')
		words = filter(lambda x: x != '', words)
		if len(words) == 2:
			codes[words[0]] = float(words[1])
	return codes

# For a give passage of text, build a tuple of (<total word count>, <sentiment_word_count>, <sentiment_score_total).
def sentiment_tuple(codes, text, punct = ['.', '?', '!', ',', '-', "'", ';', ':', '/', "\n", "\t", '"']):
	clean_text = ''.join(map(lambda x: remove_punct(x, punct), text)).lower()
	words = filter(lambda x: x != '', clean_text.split(' '))
	total_word_count = 0
	sentiment_word_count = 0
	sentiment_score_total = 0
	for word in words:
		total_word_count += 1
		if codes.has_key(word):
			sentiment_word_count += 1
			sentiment_score_total += codes[word]
	return (total_word_count, sentiment_word_count, sentiment_score_total)

# For a given punctuation list and character, return a white-space if char is in list.
def remove_punct(char, punct):
	if char in punct:
		return ' '
	else:
		return char
		
# Get the sentiment score for the given text passage.
def sentiment_score(codes, text, avg_total_words = True, punct = ['.', '?', '!', ',', '-', "'", ';', ':', '/', "\n", "\t", '"']):
	total_word_count, sent_word_count, total_score = sentiment_tuple(codes, text, punct)
	denom = total_word_count
	if not(avg_total_words):
		denom = sent_word_count
	if denom == 0:
		return 0
	return float (total_score)/(denom)


# Get top N tweets. Tweets is a list of dict objects, direction = 1 if happy or -1 if sad.
def top_n_tweets(tweets, codes, n, direction = 1):
	scored_text = map(lambda x: (text(x), sentiment_score(codes, text(x))), tweets)
	sorted_text = sorted(scored_text, key = lambda ts: ts[1])
	if direction > 0:
		sorted_text.reverse()
	return map(lambda x: x[0], sorted_text[:n])


# Get states dict {code:name} from CSV file of form Name,Code per line
def read_states(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		name, code = line.upper().strip().split(',')
		codes[name] = code
		codes[code] = code
	return codes

# Check a location text and extract the state code, if it has one.
def extract_states(coded_states, loc_text, punct = ['.', '?', '!', ',', '-', "'", ';', ':', '/', "\n", "\t", '"']):
	clean_string = ''
	if loc_text != None:
		clean_string = remove_punct(loc_text.strip(), punct).upper()
	words = filter(lambda x: x != '', clean_string.split(' '))
	# print(words)
	for word in words:
		if coded_states.has_key(word):
			return coded_states[word]
	return None




def top_n_states(coded_states, sentiment_codes, tweets, direction=0):

	state_sentiments = {}
	
	for t in tweets:
		try:
			state = (extract_state(coded_states, text(t,['user','location'])))
			if type(state) !=  type(None):
				score = sentiment_score(sentiment_codes, text(t, ['text']))
				if state_sentiments.has_key(state):
					state_sentiments[state][0] += score # cumulative state score
					state_sentiments[state][1] += 1   # number of tweets from each state
				else:
					state_sentiments[state] = [score, 1]
								
		except:
			x = 1
		
	state_average = {}
	
	for key in state_sentiments:
		state_average[key] = (state_sentiments[key][0] / state_sentiments[key][1])

	if direction == 0:	
		return sorted(state_average.items(), key=itemgetter(1))	
	else:
		return sorted(state_average.items(), key=itemgetter(1), reverse = True)
