from WordChain import *

# takes in filename of world list as input and returns
# words in a python list
def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))
'''
print(one_off("abc", "abd"))
print(one_off("abc", "abc"))
print(one_off("abc", "ade"))
'''

#word_list = read_words("/Users/jordanwarnecke/Documents/SchoolWork/2014-2015/BUAD 400/util-data-files/words-1000.txt")
word_list = read_words("/Users/jordanwarnecke/Documents/SchoolWork/2014-2015/BUAD 400/util-data-files/words.txt")
g1 = build_graph(word_list, 4)
# print(g1)
# print(len(g1))

print(word_chain(g1, "meat", "peer", 5))