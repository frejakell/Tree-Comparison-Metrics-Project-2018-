import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster import hierarchy as hier
from scipy.spatial import distance as ssd
from sklearn.manifold import MDS
from sklearn.metrics import euclidean_distances
from scipy.cluster.hierarchy import cut_tree
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import ward, dendrogram,complete
from collections import defaultdict
import scipy
import pylab
import rf_dist 
import triplets
import quar_color
import quartets_co
import My_kenCo
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt


def main(D):
    distArray = ssd.squareform(D)
    # Compute and plot first dendrogram.
    fig = plt.figure(figsize=(8,8))
    ax1 = fig.add_axes([0.05,0.1,0.2,0.6])
    Y = ward(distArray)
    Z1 = sch.dendrogram(Y, orientation='left')
    ax1.set_xticks([])
    ax1.set_yticks([])

    # Compute and plot second dendrogram.
    ax2 = fig.add_axes([0.3,0.75,0.6,0.2])
    Y = ward(distArray)
    Z2 = sch.dendrogram(Y)
    ax2.set_xticks([])
    ax2.set_yticks([])

    # Plot distance matrix.
    axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
    idx1 = Z1['leaves']
    idx2 = Z2['leaves']
    D = D[idx1,:]
    D = D[:,idx2]
    im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu,vmin=0, vmax=8)


    axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
    plt.colorbar(im, cax=axcolor)
    fig.show()
    
#Example of how to run the code and obtain Heatmaps    
array = []
tree1=[]
tree2=[]
dist=[]
#Open and retrive trees in test file
with open("trees_newick_test.txt") as f:
    for line in f:
         array.append(line.replace('\n', ''))

n_samples = len(array)
seed = np.random.RandomState(seed=2)

#create a set of Gaussians in a grid of mean (-1.5,1.5) and standard devaition (0.2,5)
trees=[]
tempSim=[]



# Generate distance matrix.

D = scipy.zeros([len(array),len(array)])
names=[]
for i in range (0,len(array)):
    names.append(str(i))
    for j in range (len(array)):
        D[i,j] = triplets.main(array[i], array[j])
#Call main to print corresponding Heatmap
main(D)

