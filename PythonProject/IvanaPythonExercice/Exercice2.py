import numpy as np 
from math import pow , sqrt 
import matplotlib.pyplot as plt

## ramdom sample
variance =  5.3
moyenne = 12.3
size = 500

sample = np.random.normal(loc=moyenne,scale=sqrt(variance),size=size)
sample.var()
sample.mean()

moyenneListe = [] 
varianceList = []

for i in range(500) :
    sample = np.random.normal(loc=moyenne,scale=sqrt(variance),size=size)
    moyenneListe.append(sample.mean())
    varianceList.append(sample.var())

plt.plot(moyenneListe)
plt.show()

####
sampleMeanPopulation = np.mean(moyenneListe)
sampleVariancePooulation = np.mean(varianceList)

print(f"Mean = {moyenne} , Mean of sample Means = {sampleMeanPopulation}")
print(f"Variance = {variance} , Variance of sample Means = {sampleVariancePooulation}")


np.random.randint()
