
import matplotlib.pyplot as plt
from pandas import DataFrame

class generateTendance :
    def __init__(self , w :int , h:int , df:DataFrame ) -> None:
        self.w = w
        self.h = h
        self.df = df
    
    def generate(self) :
        
        plt.figure( figsize=(self.w , self.h) , dpi=200 )
        plt.plot(self.df.index, self.df["Close"] )

        plt.show()
        plt.savefig("images/tendance.png")



