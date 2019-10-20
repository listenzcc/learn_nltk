
# filename: analysis.py

from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
import nltk
from pprint import pprint


with open('article.txt', 'rb') as f:
    x = f.readlines()

lines = []
for j, e in enumerate(x):
    if j % 3 == 1:
        lines.append(e.decode('utf-8'))

line = lines[0]
print(line)

ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer(language='english')

words_tokens = nltk.tokenize.word_tokenize(line)
words = {e: [ps.stem(e), ls.stem(e), ss.stem(e)] for e in words_tokens}
pprint(words)
