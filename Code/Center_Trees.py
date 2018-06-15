
import numpy as np
import time,math,sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib
import sklearn
import T_dist
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.cluster import hierarchy as hier
from scipy.spatial import distance as ssd
from sklearn.manifold import MDS
from scipy.cluster.hierarchy import cut_tree
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import ward, dendrogram,complete,average
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def main(D,C):
    Mat_arr=D
      

    center=Mat_arr.mean(axis=1)
    min_mean=center[0]
    mean_tree=[]
    for r in range(0,len(center)):
        if(center[r]<min_mean):
            
            mean_tree=[]
            mean_tree.append(r+1)
            min_mean=center[r]
            #print(mean_tree,min_mean)
        elif(center[r]==min_mean):
            mean_tree.append(r+1)
            #print(mean_tree,min_mean)

       

    min=0
    first_row=Mat_arr[0]
    for i in range(0,len(first_row)):
            min+= math.sqrt((first_row[i]-center[i])**2)

    min_tree=[]
    for r in range(len(Mat_arr)):
        row=Mat_arr[r]
        sum=0
        for i in range(0,len(row)):
            sum+= math.sqrt((row[i]-center[i])**2) 
            
            if(sum>min):break
        if(sum<min):
            
            min_tree=[]
            min_tree.append(r+1)
            min=sum
        elif(sum==min):
            min_tree.append(r+1)
         
    text="----------------------------------------------------------------------------------------\n"
    #text+="Cluster ID:"+str(key)+"\n"
    #text+="Cluster tree set:"+ str(clusters[key])+"\n"
    text+="Center tree-approach #1:"+str(mean_tree)+"\n"
    text+="Center tree-approach #2:"+ str(min_tree)+"\n"  
    text+="----------------------------------------------------------------------------------------\n"
    if(C.upper()=="Y"):
        distances=D
        distArray = ssd.squareform(distances)
      
        linkage_matrix = average(distArray)
      
        fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
        clusters = defaultdict(lambda:[])
        for pos in range(0,len(fc)):
            clusters[fc[pos]].append(pos+1)
        for key in clusters:    
            Cluster_matrix=[]
            Cluster_distances=[]
            tempSim=[]
            array=clusters[key]
           
            for x in range (0,len(array)):
               
                temp=[]
                for y in range (0,len(array)):
                    temp.append(distances[x,y])
                    
                tempSim.append(temp)

            Cluster_distances=np.array(tempSim)
            center=Cluster_distances.mean(axis=1)
            min_mean= float("inf")
            mean_tree=[]
            for r in range(0,len(center)):
                if(center[r]<min_mean):
                    
                    mean_tree=[]
                    mean_tree.append(array[r])
                    min_mean=center[r]
                   
                elif(center[r]==min_mean):
                    mean_tree.append(array[r])
            
            min=0
            first_row=Cluster_distances[0]
            for i in range(0,len(first_row)):
                    min+= math.sqrt((first_row[i]-center[i])**2)

            min_tree=[]
            for r in range(len(Cluster_distances)):
                row=Cluster_distances[r]
                sum=0
                for i in range(0,len(row)):
                    sum+= math.sqrt((row[i]-center[i])**2) 
                    
                    if(sum>min):break
                if(sum<min):
                    
                    min_tree=[]
                    min_tree.append(array[r])
                    min=sum
                elif(sum==min):
                    min_tree.append(array[r])
            
            
            text+="Cluster ID:"+str(key)+"\n"
            text+="Cluster tree set:"+ str(clusters[key])+"\n"
            text+="Center tree-approach #1:"+str(mean_tree)+"\n"
            text+="Center tree-approach #2:"+ str(min_tree)+"\n"    
            text+="----------------------------------------------------------------------------------------\n"
    print(text)
            
array = []
tree1=[]
tree2=[]
dist=[]
#Open and retrive trees in test file
with open("Random_200.txt") as f:
    for line in f:
         array.append(line.replace('\n', ''))

n_samples = len(array)
seed = np.random.RandomState(seed=2)


trees=[]
tempSim=[]



D = scipy.zeros([len(array),len(array)])
names=[]
for i in range (0,len(array)):
    names.append(str(i))
    for j in range (len(array)):
        D[i,j] = T_dist.main(array[i], array[j])
#Example of how to run Center tree
main(D,"y")            
