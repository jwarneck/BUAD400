'''
T = "Halloween is scary and fun"

W = set of all sentiment of coded words

Treated as a bag, not a set
T' can have duplicates
T' = W intersect T (meaning everything that is in both W and T)

score(T) = summation: 1/|T'| , w = T', score(W)
sentiment_tuple(Text, codes) ---returns--> (|T'|, W intersect T & score(w))

'''