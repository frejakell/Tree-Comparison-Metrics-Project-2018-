import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from scipy.cluster import hierarchy as hier
from scipy.spatial import distance as ssd
from sklearn.manifold import MDS
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import pylab
import rf_dist 
import T_dist
import pylab
import Q_dist
import KC_dist




def main(a,auto):
    bins=8
    if (auto.upper()=="Y"): bins="auto"
    plt.hist(a, bins=bins)  
    plt.show()
    
 

dist=[]
array=[]
with open("Random_200.txt") as f:
    for line in f:
         array.append(line.replace('\n', ''))

n_samples = len(array)



Histro=[]

for x in range (0,len(array)):
    
    for y in range (0,len(array)):
        dist=T_dist.main(array[x], array[y])
        Histro.append(dist)
  


main(Histro,"y")