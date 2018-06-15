import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import numpy as np
from scipy.spatial import distance as ssd
from sklearn.manifold import MDS
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import euclidean_distances
from scipy.cluster.hierarchy import cut_tree
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import ward, dendrogram,complete
from collections import defaultdict 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import sys
import numpy as np
import math
import matplotlib
import sklearn
from matplotlib.collections import LineCollection
from scipy.cluster import hierarchy as hier
import matplotlib.pyplot as plt
import scipy
import random
import pylab
class App(QMainWindow):
 
    '''def __init__(self):
        super().__init__()
        
        self.initUI("3D")'''
 
    def initUI(self,mode,matrix,list,c,l,d,a):
        self.left = 200
        self.top = 40
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 650
        self.height = 650
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
      
        self.m = PlotCanvas(self, width=6, height=6,mode=mode,matrix=matrix,list=list,c=c,l=l,d=d,a=a)
        self.m.move(4,6)
      
 
        self.show()
    
 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=5,mode="2D", dpi=100, matrix=[], list=[],c='y',l='y',d='N',a='N'):
        self.matrix=matrix
        self.list=list
        self.c=c
        self.l=l
        self.a=a
        self.d=d
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        if mode=='2D':
            self.plot2D()
        elif mode=='3D': self.plot3D()
        elif mode=="Hist":self.plotHist()
        else: self.plot()
    def plotHist(self):
        dfn = 10
        dfd =1
        limit = 5
        print(self.list)
        x = np.array(self.list)
        if(self.a=='Y'): bins='auto'       
        else: bins = 8

        ax = self.figure.add_subplot(111)

        # the histogram of the data
        n, bins, patches = ax.hist(x, bins, edgecolor='black', normed=True)
     
    
       

        ax.set_xlabel('Smarts')
        ax.set_ylabel('Probability density')
       

  
        self.draw()
      
    def plot2D(self):
        
 
        ax = self.figure.add_subplot(111)
        distances=self.matrix
        distArray = ssd.squareform(distances)
        arr =np.array(self.list)
        if(self.c=='y'): 
            linkage_matrix = ward(distArray)
            R=dendrogram(linkage_matrix, orientation="left")
            
            fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
            #plt.clf()
         
        else: fc="b"
        #plt.clf()
        mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
        pos = mds.fit_transform(distances)
        xs, ys = pos[:, 0], pos[:, 1]
        print(xs,ys)
        ax.scatter(xs, ys, c=fc)
        Tree_count=1
        if(self.l=='y' ):
            for x, y in zip(xs, ys):
                    
                ax.text(x, y, "tree" + str(Tree_count))
                Tree_count+=1
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
    
        #print("Error found, could not produce plots")
   
       
       
    def plot3D(self):
        
        distances=self.matrix
        distArray = ssd.squareform(distances)
        arr =np.array(self.list)
        if(self.c=='y'): 
            linkage_matrix = ward(distArray)
            R=dendrogram(linkage_matrix, orientation="left")
            max_d=len(set(R['color_list']))+1
            fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
           
         
        else: fc="b"  
        ax = self.figure.add_subplot(111,projection='3d')
        
      
        mds = MDS(n_components=3,dissimilarity="precomputed", random_state=6)
        pos = mds.fit_transform(distances)
        xs, ys,zs = pos[:, 0], pos[:, 1], pos[:, 2]
        ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2],c=fc)
        if(self.l=='y' ):
            Tree_count=1
            for x, y,z in zip(xs, ys, zs):
                ax.text(x, y, z, "tree" +str(Tree_count))
                Tree_count+=1            

        ax.set_title('PyQt Matplotlib Example')
        self.draw()
    def plot(self):
        '''data = [random.random() for i in range(25)]
        D = scipy.zeros([len(data),len(data)])
        for i in range (0,len(data)):
            
            for j in range (i):
                D[i,j] = D[j,i] =int(i)
        print(D)


      
        # Compute and plot first dendrogram.
        fig = plt.figure(figsize=(8,8))
        ax1 = fig.add_axes([0.05,0.1,0.2,0.6])
        
        ax1.set_xticks([])
        ax1.set_yticks([])

        # Compute and plot second dendrogram.
        ax2 = fig.add_axes([0.3,0.75,0.6,0.2])
 
        ax2.set_xticks([])
        ax2.set_yticks([])

        # Plot distance matrix.
        axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
        idx1 = Z1['leaves']
        idx2 = Z2['leaves']
        D = D[idx1,:]
        D = D[:,idx2]
        plt2= self.figure.add_subplot(1,1,1)
        im = axmatrix.matshow


        axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
        plt2.colorbar(im, cax=axcolor)'''  
       
        image = self.matrix
        distArray = ssd.squareform(image)
        Y = ward(distArray)
        Z1 = sch.dendrogram(Y, orientation='left')      
        Y = ward(distArray)
        Z2 = sch.dendrogram(Y)
        
       
      
        self.figure.clear()
        
        self.axes=self.figure.add_subplot(1, 1, 1)
      
        im = self.axes.imshow(image, aspect='equal', origin='lower', cmap=pylab.cm.YlGnBu,vmin=0, vmax=8)
        self.figure.colorbar(im)
       
        self.axes.set_title('Loaded Matrix')
        self.draw()       
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())