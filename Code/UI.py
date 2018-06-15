import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib
import sklearn
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster import hierarchy as hier
from scipy.spatial import distance as ssd
from sklearn.manifold import MDS
from scipy.cluster.hierarchy import cut_tree
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import ward, dendrogram,complete,average
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import rf_dist 
import Random_tree
import trees_generator
import Q_dist
import T_dist
import KC_dist
import numpy as np
import scipy
import pylab
import time,math,sys
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
print("------------------------------------------------------")
print("Tree Comparison project")
print("Freja Kelleris,2018")
print("------------------------------------------------------")
Tree_set=[]
def write_to_file(filename, data):
    try:
        thefile = open(filename, 'w')
        for item in  data[:-1]:
            
            thefile.write("%s\n" % item)
        thefile.write("%s" %  data[-1])
        thefile.close()
    except: 
        print("coudn't write to file specified")
    return None
while True:    # infinite loop
    n = input("Please enter command: ")
    if n.upper() == "QUIT":
        break  # stops the loop
    elif n.upper() == "HELP":
       print("Metrics commands: ")
       print("  Robinson fould: RF <FileName> ")
       print("  Kendall-Colijn: KC <FileName> ")
       print("  Triplets: TD <FileName> ")
       print("  Quartets: QD <FileName> ")
       print("  Note: if no input file is included the distance matrix will used tree stored in memory ")
       print("Tree commands: ")
       print("  Bulid Rooted Trees: RT <Number_leaves> [output File]")
       print("  Bulid Unrooted Trees: UT <Number_leaves> [output File]")
       print("  Bulid Random Trees: RAN <Number_trees> <Number_leaves> <Rooted or Unrooted(R/U?)> [output File]")
       print("  Note: if no output file is included the tree lists will be stored in memory for futher use")
       print("Visualization commands: ")
       print("  MDS(2D): 2D  <Labels-(y/n?)> <clusters-(y/n?)> ")
       print("  MDS(3D): 3D  <Labels-(y/n?)> <clusters-(y/n?)> ")
       print("  Heatmap: HMap ]")
       print("  Distributiion: Hist ")
       print("  Note: the images will be displayed immediately")
       print("Tree Center commands: ")
       print("  Center Mean approach: CenterM ")
       print("  Center Vector approach: CenterV ")
       print("  Cluster Center Tree approaches: CenterClus")
    
       
  
  
    else: 
        command=n.split()
        if command[0].upper() == 'RF':
            try:
                if len(command)==2:
                    Tree_set=[]
                    with open(command[1]) as f:
                        for line in f:
                            Tree_set.append(line.replace('\n', ''))
                
                n_samples = len(Tree_set)
                yourarray = np.zeros([n_samples,n_samples ])

                
                trees=[]
                tempSim=[]
                for i in range(0,n_samples):
                    for j in range(i):
                         yourarray[i,j] = yourarray[j,i] = rf_dist.main(Tree_set[i], Tree_set[j])
                         tempSim.append(yourarray[i,j])
                if(len(command)>2):
                    a = yourarray
                    mat = np.matrix(a)
                    with open('outfile.txt','wb') as f:
                        for line in mat:
                            np.savetxt(f, line, fmt='%.2f')
                print(yourarray)
            except:
                print("failed to compute distances")
        elif command[0].upper() == 'QD':
            try:
                if len(command)==2:
                    Tree_set=[]
                    with open(command[1]) as f:
                        for line in f:
                            Tree_set.append(line.replace('\n', ''))
                
                n_samples = len(Tree_set)
                yourarray = np.zeros([n_samples,n_samples ])

        
                trees=[]
                tempSim=[]
                for i in range(0,n_samples):
                    for j in range(i):
                         yourarray[i,j] = yourarray[j,i] = Q_dist.main(Tree_set[i], Tree_set[j])
                         tempSim.append(yourarray[i,j])
                print(yourarray)
            except:
                 print("failed to compute distances")
        elif command[0].upper() == 'TD':
            try:
                if len(command)==2:
                    Tree_set=[]
                    with open(command[1]) as f:
                        for line in f:
                            Tree_set.append(line.replace('\n', ''))
                
                n_samples = len(Tree_set)
                yourarray = np.zeros([n_samples,n_samples ])

              
                trees=[]
                tempSim=[]
                for i in range(0,n_samples):
                    for j in range(i):
                         yourarray[i,j] = yourarray[j,i] =T_dist.main(Tree_set[i], Tree_set[j])
                         tempSim.append(yourarray[i,j])
                print(yourarray)
            except:
                print("failed to compute distances")
        elif command[0].upper() == 'KC':
            try:
                if len(command)==3:
                    Tree_set=[]
                    with open(command[2]) as f:
                        for line in f:
                            Tree_set.append(line.replace('\n', ''))
                
                n_samples = len(Tree_set)
                yourarray = np.zeros([n_samples,n_samples ])

               
                trees=[]
                tempSim=[]
                for i in range(0,n_samples):
                    for j in range(i):
                         yourarray[i,j] = yourarray[j,i] =KC_dist.main(Tree_set[i], Tree_set[j],int(command[1]))
                         tempSim.append(yourarray[i,j])
                print(yourarray)
            except: 
                print("Failed to compute distances")
        elif command[0].upper() == 'RAN':
            try:
                Tree_set=Random_tree.main(int(command[1]),int(command[2]),command[3])
                
            except:
                print("Failed to execute command: Please type Help for command list")
            else:
                if(len(command)==5):
                    write_to_file(command[4],Tree_set)
                print("done")
        elif command[0].upper() == 'RT':
            try:
                Tree_set=trees_generator.main(int(command[1]),"R")
            except:
                print("Failed to execute command: Please type Help for command list")
            else:
                if(len(command)==4):
                    write_to_file(command[3],Tree_set)
          
        elif command[0].upper()== 'UT':
            try:
                Tree_set=trees_generator.main(int(command[1]),"U")
            except:
                print("Failed to execute command: Please type Help for command list")
            else:
                if(len(command)==3):
                    write_to_file(command[2],Tree_set)
          
           
        elif command[0].upper() == 'CENTERM':
           try:  
               center=yourarray.mean(axis=1)
               tempSim=np.array(tempSim)
               min_mean=center[0]
               mean_tree=[0]
               for r in range(1,len(center)):
                    if(center[r]<min_mean):
                        mean_tree=[]
                        mean_tree.append(r+1)
                        min_mean=center[r]
                    elif(center[r]==min_mean):
                        mean_tree.append(r+1)
               print("")        
               print(mean_tree)
           except:
                print("Failed to execute command: Please type Help for command list")
          
        elif command[0].upper() == 'CENTERV':  
           try:  
               center=yourarray.mean(axis=1)
               tempSim=np.array(tempSim)
               min=0
               first_row=yourarray[0]
               for i in range(0,len(first_row)):
                        min+= math.sqrt((first_row[i]-center[i])**2)

               min_tree=[1]
               for r in range(len(yourarray)):
                    row=yourarray[r]
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
               print(min_tree)        
               
           except:
                print("Failed to execute command: Please type Help for command list")
          
         
     
        elif command[0].upper() == 'CENTERCLUS':
            try: 
                distances=yourarray
                distArray = ssd.squareform(distances)
                arr =np.array(tempSim)

                linkage_matrix = ward(distArray)
                R=dendrogram(linkage_matrix, orientation="left")

                max_d=len(set(R['color_list']))+1
                fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
                clusters = defaultdict(lambda:[])
                for pos in range(0,len(fc)-1):
                    clusters[fc[pos]].append(pos)
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

                    min_tree=[1]
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
                    print("----------------------------------------------------------------------------------------")
                    print("Cluster ID:", key)
                    print("Cluster tree set:",clusters[key])
                    print("Center tree-approach #1:",mean_tree)
                    print("Center tree-approach #2:",min_tree)     
                    print("----------------------------------------------------------------------------------------")
            except:
                    print("Failed to execute command: Please type Help for command list")
          
        elif command[0] == '2D':
            try:
                distances=yourarray
                distArray = ssd.squareform(distances)
                arr =np.array(tempSim)
                if(command[1]=='c'): 
                    linkage_matrix = ward(distArray)
                    R=dendrogram(linkage_matrix, orientation="left")
                    max_d=len(set(R['color_list']))+1
                    fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
                    plt.clf()
                 
                else: fc="b"
                plt.clf()
                mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
                pos = mds.fit_transform(distances)
                xs, ys = pos[:, 0], pos[:, 1]
                plt.scatter(xs, ys, c=fc)
                Tree_count=1
                if(command[2].lower()=='l' ):
                    for x, y in zip(xs, ys):
                            
                        plt.text(x, y, "tree" + str(Tree_count))
                        Tree_count+=1
                plt.show()
            except: 
                print("Error found, could not produce plots")
        elif command[0] == '3D':
            distances=yourarray
            distArray = ssd.squareform(distances)
            arr =np.array(tempSim)
            if(command[1]=='c'): 
                linkage_matrix = ward(distArray)
                R=dendrogram(linkage_matrix, orientation="left")
                max_d=len(set(R['color_list']))+1
                fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
               
             
            else: fc="b"  
            plt.clf()
            fig = plt.figure()
            fig = fig.add_subplot(111,projection='3d')
            mds = MDS(n_components=3,dissimilarity="precomputed", random_state=6)
            pos = mds.fit_transform(distances)
            xs, ys,zs = pos[:, 0], pos[:, 1], pos[:, 2]
            fig.scatter(pos[:, 0], pos[:, 1], pos[:, 2],c=fc)
            if(command[2]=='L'):
                Tree_count=1
                for x, y,z in zip(xs, ys, zs):
                    fig.text(x, y, z, "tree" +str(Tree_count))
                    Tree_count+=1
            plt.show()               
        elif command[0].upper() == 'HMAP':
            distances=yourarray
            distArray = ssd.squareform(distances)
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
            distances = distances[idx1,:]
            distances = distances[:,idx2]
            im = axmatrix.matshow(distances, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu,vmin=0, vmax=8)


            axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
            plt.colorbar(im, cax=axcolor)
            fig.show()
        else:  
            print("Unreconized Command: Type 'Help' for options")