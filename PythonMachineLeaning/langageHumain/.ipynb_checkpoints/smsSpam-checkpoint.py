import pandas as pd
import numpy as np 
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


message = pd.read_csv("SMSSpamCollection",sep='\t',names=['labels','message'])

message.head(2)

message.describe()
"""
Le fichier de données contient un total de 5572 texte
étiquetter en spam et ham. il s'aggira de mettre en place un model 
d'apprentissage automatique, qui pourra predire si un message est un spam 
ou pas. 
1- DEscription des donnees. 

"""
# Varialbe Length
message['labels'].describe()
message['length'] = message['message'].apply(lambda x: len(x))
message.head(2)


# Description de la variable Lenght
message['length'].describe()

# message plus long 
long_text = message[message['length']== message['length'].max()]
long_text

# Tokenisation ;
def text_process(msg) :
    nopunc =[ char for char in msg if char not in string.punctuation ]
    nopunc = "".join(nopunc)
    tokens = [ word for word in nopunc.split() 
              if word.lower() not in stopwords.words("english")  ]
    
    return tokens

# Vectorisation ;
#1 - Calcul des termes de frequence
tf = CountVectorizer( analyzer=text_process ).fit(message['message'])

## Afichage des mots dans l'ensemble des textes
for e in tf.get_feature_names_out()[150:200] :
    print(e)

# indice de position de caque terme
print(tf.vocabulary_)

## Encdage des textes sous forme de matrice
tf2 = tf.transform(message['message'])
print(tf2)


## Affichage de la matrice creure (sparx matrices)
print(tf2.toarray())

## Etape 2 Calcul des ponderation TF-IDE
tfidf = TfidfTransformer()
tfidf.fit(tf2)
tfidf2 = tfidf.transform(tf2)
print(tfidf2)

## Separation en schatillon d'apprentissage 
X_train,X_test,y_train,y_test = train_test_split(tfidf2, message['labels']
                        ,test_size=0.2,random_state=8)

def model(classifer) :
    classifer.fit(X_train,y_train)

    y_pred = classifer.predict(X_test)
    print("Score de prediction : ",round(accuracy_score(y_test,y_pred)*100 , 2) , " %")


## Logistique
classifer2 = LogisticRegression()
model(classifer2)

## Classifieur naif de Bayes
classier3 = MultinomialNB()
model(classier3)

## suport vector machone
model(SVC())

## les K plus proche voisin
model( KNeighborsClassifier() )

## Arbre de decision 
model( DecisionTreeClassifier() )

# Data pipeline


