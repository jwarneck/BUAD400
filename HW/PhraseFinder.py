# remember any number can potentially be a number in the end result
# find words that combine multiple numbers
# functions:
#		string.startswith(prefix) --> true/false
#		flatten(list) --> List


# Takes in a number, converts to a letter, and creates 
# a new list with words that start with that letter
def filter(phone_number, word_list):
	j = 0
	while(j < len(phone_number):
		number = phone_number[j]
		words = {}
		if (number == 0):
			break
		elif (number == 1):
			break
		elif (number == 2):
			# get words that start with a, b, c
			# append to words
		elif (number == 3):
			# get words that start with d, e, f
			# append to words
		elif (number == 4):
			# get words that start with g, h, i
			# append to words
		elif (number == 5):
			# get words that start with j, k, l
			# append to words
		elif (number == 6):
			# get words that start with m, n, o
			# append to words
		elif (number == 7):
			# get words that start with p, q, r, s
			# append to words
		elif (number == 8):
			# get words that start with t, u, v
			# append to words
		elif (number == 9):
			# get words that start with w, x, y, z
			# append to words
		j + 1
	flatten(words)
		
	
	
# Takes in a phone number, calls filter function
# returns phrase with words and max numbers
# to represent the phone number
def phrases(phone_number, word_list, max_numbers):
	i = 0
	while (i < len(phone_number):
		# treat phone number as a string
		filter(phone_number, word_list)
		i + 1
	
