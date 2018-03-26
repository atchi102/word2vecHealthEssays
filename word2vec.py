from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()

print '\n-----\n'.join(tokenizer.tokenize(data))
