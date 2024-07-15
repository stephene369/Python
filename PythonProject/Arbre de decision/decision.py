#Importation des modules nécessaires
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
#importation du dataset Iris
iris= load_iris()

#Déclaration de l'arbre de décision
clf = DecisionTreeClassifier(max_depth=3)
#Entrainement de l'abre de décision 
clf.fit(iris.data, iris.target)
#Affichage de l'abre de décision obtenu après entraînement
plot_tree(clf, feature_names= ['sepal_length','sepal_width','petal_length','petal_width'], class_names=["Iris-setosa","Iris-versicolor","Iris-virginica"],filled=True)
plt.show()