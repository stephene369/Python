import nltk 
import random


nltk.download('stopwords')
mots = nltk.corpus.stopwords.words

francais = mots("french")
random.choices(francais,k=5)


