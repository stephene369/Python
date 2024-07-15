from UI.lib import * 

class Support:
    def __init__(self , df:DataFrame=None ,
        col:str=None) -> None:
        
        self.df = df
        self.col = col

    def support_resistance(self) :

        resistance = [[],[]]
        support = [[],[]]
        j=0
        for i in range(0, len(self.df) , int(len(self.df)/7) ) :
            try :
                
                max_ = self.df[j:i][self.col].max()
                min_ = self.df[j:i][self.col].min()

                date = self.df[j:i][self.df[j:i][self.col]==max_].index[0]
                date_ = self.df[j:i][self.df[j:i][self.col]==min_].index[0]

                resistance[0].append(date)
                resistance[1].append(max_)

                support[0].append(date_)
                support[1].append(min_)

                j=i

            except Exception as e: print(e)
        #####
        piqueP = [[],[]]
        piqueN = [[],[]]
        j=0
        for i in range(0, len(self.df) ,30) :
            try :
                max_ = self.df[j:i][self.col].max()
                min_ = self.df[j:i][self.col].min()

                date = self.df[j:i][self.df[j:i][self.col]==max_].index[0]
                date_ = self.df[j:i][self.df[j:i][self.col]==min_].index[0]

                piqueP[0].append(date)
                piqueP[1].append(max_)

                piqueN[0].append(date_)
                piqueN[1].append(min_)

                j=i
            except Exception as e: print(e)


        plt.figure(figsize=(16,10))
        plt.plot(self.df.index , self.df[self.col])
        position = []
        for i in range(0 , len(self.df) , int(len(self.df)/8)) : position.append(i)
        labels = [self.df.iloc[int(i)].name for i in position]
        plt.xticks(position,labels,rotation=45)

        plt.plot(resistance[0] , resistance[1] , marker='^',color='red',markersize=6,label = "Resistance",linewidth=0.5)
        plt.plot(support[0] , support[1] , marker='v',color='green',markersize=6,label = "Support",linewidth=0.5)

        plt.plot(piqueP[0] , piqueP[1] , marker='^',color='red',markersize=3,linewidth=0)
        plt.plot(piqueN[0] , piqueN[1] , marker='^',color='green',markersize=3,linewidth=0)

        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.subplots_adjust(top=0.2, bottom=0.1)
        plt.set_cmap("tab20c")
        plt.tight_layout()
        plt.xlabel("Date")
        plt.legend()
        plt.savefig(r"resource/MA_resistance.png")
        plt.close()
        
