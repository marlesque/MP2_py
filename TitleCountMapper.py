#!/usr/bin/env python

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopwords= ""
delimiters= ""
results1 = ()
with open(stopWordsPath) as f:
    stopwords = f(stopWordsPath)


with open(delimitersPath) as f:
    delimiters = f(delimitersPath)

for line in sys.stdin:
   results= line.split(delimiters)
   results= results.lower()
   for word in results:
       if (word==any(stopwords)):
           results.pop(word)
   results1= results1.append(results)

for w in results1:
    print('%s\t%s' % (w, 1))
      
    # TODO

