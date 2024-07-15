from UI.lib import *

class homeFrame(SmoothScrollArea) :
    
    def __init__(self , parent=None) :
        super().__init__(parent=parent)
        self.setWidget(
        BodyLabel(("""
                   Bienvenue dans notre application dédiée aux investisseurs avisés ! 
Si vous êtes à la recherche d'outils puissants pour appliquer des stratégies de trading sophistiquées, vous êtes au 
bon endroit. Notre plateforme a été spécialement conçue pour vous permettre d'intégrer facilement les stratégies de 
moyennes mobiles ainsi que la stratégie combinée de l'Oscillateur stochastique et de la MACD.  Nous comprenons que 
chaque investisseur a des besoins et des préférences uniques. C'est pourquoi notre application vous offre la possib-
ilité de personnaliser les paramètres de chaque stratégie selon votre vision et votre style de trading. Vous pouvez 
ajuster les seuils, les périodes et d'autres variables cruciales pour chaque stratégie, afin de les aligner parfaitement 
avec vos objectifs.

Mais ce n'est pas tout. Nous allons au-delà de la simple personnalisation en vous permettant de simuler les performances 
de ces stratégies en fonction de votre profil d'investisseur. Grâce à des simulations basées sur des données historiques, 
vous pouvez avoir un aperçu clair de comment ces stratégies se comporteraient dans différentes conditions de marché, vous 
aidant ainsi à prendre des décisions éclairées. 

L'une des caractéristiques les plus remarquables de notre application est la possibilité de déterminer les paramètres 
optimaux pour chaque stratégie. En utilisant des algorithmes avancés, notre plateforme peut analyser un large éventail 
de paramètres et identifier ceux qui maximisent potentiellement vos gains tout en maîtrisant les risques. Cela vous permet 
de trader en toute confiance, en sachant que vos décisions sont basées sur des données précises et une analyse approfondie.

Que vous soyez un trader expérimenté à la recherche de nouveaux moyens d'optimiser vos stratégies ou un débutant 
souhaitant explorer le monde passionnant du trading, notre application est là pour vous accompagner. Préparez-vous 
à exploiter le pouvoir des moyennes mobiles, de l'Oscillateur stochastique et de la MACD d'une manière qui vous est 
entièrement adaptée. Bienvenue dans une nouvelle ère de trading stratégique et personnalisé !""")))
        self.setScrollAnimation(Qt.Vertical, 400, QEasingCurve.OutQuint)
        self.setScrollAnimation(Qt.Horizontal, 400, QEasingCurve.OutQuint)
        self.horizontalScrollBar().setValue(6000)
            
        


