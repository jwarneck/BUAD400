def filter(phone_number, wordlist):
'''	
	Not sure whether the processes done here should've gone in the
	phraseFinder() function and kept this as a filter to check word
	length and max_numbers.
'''
	numberArray = []
	wordArray = []
	words = {}
	
	# breaks down the phone number into the different lengths
	r = 0
	length = len(phone_number)
	for x in range(0, length):
		number = phone_number[r:]
		r = r + 1
		numberArray.append([number])


'''
	The portion below is what I struggled the most with. I understand that 
	I needed to run through each string made in the above for loop, and then
	find words that worked for each section of the phone number, but I kept
	confusing myself on how to go about this and couldn't get it worked out.
'''

	# searches for words that go with the numbers for
	# length of number
	i = 0
	for y in range(0, 1):
		test = numberArray[i]
		print(test)
		i = i + 1
		# As each number is processed, check and see what letters are associated
		# with that number, and what words can be made.
		if (test[0] == "3"):
			wordArray.append([words])
		elif (test[0] == "3"):
			wordArray.append([words])
	# Array to store both the numbers and words created to be easily searchable
	ARRAY = [(numberArray), (wordArray)]
	print(ARRAY)

# This would be the meat of finding the words that worked for the length of the
# number lengths made. While using length of the phone number to bring up each
# one stored in the array, I didn't know how to attach them to that sub of the array.
'''
	i = 0
	while i < length:
		numberArray[i].append(words)
'''

		
	
	

def phraseFinder(phone_number, wordlist, max_numbers):
	filter(phone_number, wordlist)
	# Iterate through each column to make possible combinations
	# print possible combos