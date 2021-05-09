
from PyQt5 import QtCore, QtGui, QtWidgets
from visual2 import Ui_Form_vs 
from plot_GUI import App
from compute_center_tree import Ui_center
import numpy as np
import time,math,sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
import math
import matplotlib
import pylab
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
import numpy as np
import matplotlib.pyplot as plt
class Visual_layout( Ui_Form_vs ):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.ui.FileFinder.clicked.connect(self.getfiles)
        self.show()
class Ui_Form(object):
    def OpenHM(self):
        D=self.Matrix
        distArray = ssd.squareform(D)
        print(len(D))
        labels=[]
        for x in range(len(D)):
            labels.append(x)
       
        if self.dendro.isChecked() is False:
            fig = plt.figure(figsize=(8,8))
        
            axmatrix = fig.add_axes([0.1,0.3,0.6,0.6])

            im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu,vmin=0, vmax=8,interpolation='nearest')


            axcolor = fig.add_axes([0.7,0.3,0.02,0.6])
            plt.colorbar(im, cax=axcolor)
            plt.show()

        else:
            # Compute and plot first dendrogram.
            fig = plt.figure(figsize=(8,8))
            ax1 = fig.add_axes([0.05,0.3,0.2,0.6])
            Y = ward(distArray)
            Z1 = sch.dendrogram(Y, orientation='left')
            ax1.set_xticks([])
            ax1.set_yticks([])

            # Compute and plot second dendrogram.

            # Plot distance matrix.
            axmatrix = fig.add_axes([0.3,0.3,0.6,0.6])
            idx1 = Z1['leaves']
           
            D = D[idx1,:]
            D = D[:,idx1]
            im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu,vmin=0, vmax=8)
            
         
            axcolor = fig.add_axes([0.91,0.3,0.02,0.6])
            plt.colorbar(im, cax=axcolor)
            plt.show()
            """self.window = QtWidgets.QMainWindow()
            self.ui = App()
            self.ui.initUI("hm",self.Matrix,self.dists,'n','n','n','n')"""
    def OpenCenter(self):
       
        self.window = QtWidgets.QMainWindow()
        if(self.center_clu.isChecked()):
            clus="Y"
        else: clus="N"
        self.ui = Ui_center()
        self.ui.setupUi(self.window,self.Matrix,self.dists,clus)
        
    def Open3D(self):
        c='n'
        l='n'
        self.window = QtWidgets.QMainWindow()
        self.ui = App()
        if self.MSD_clu.isChecked(): c='y'
        else: c='n'
        if self.MDS_Label.isChecked(): l='y'
        else: l='n'
        if self.ddd.isChecked(): Mode='3D'
        else: Mode='2D'
        
        self.ui.initUI(Mode,self.Matrix,self.dists,c,l,'n','n')
    def Hist(self):  
        #self.window = QtWidgets.QMainWindow()
        #self.ui = App()
        #A_scale="N"
        bins=8
        if self.Auto_scale.isChecked(): bins="auto"
        #self.ui.initUI("Hist",self.Matrix,self.dists,'n','n','n',A_scale)
        plt.clf()
        a =self.dists
        print(a)
        plt.hist(a, bins=bins,edgecolor='black', linewidth=1.2)  # arguments are passed to np.histogram
       
        plt.show()
    def setupUi(self, Form,num,dists):
        self.Matrix=num
        self.dists=dists
        Form.setObjectName("Form")
        Form.resize(722, 452)
        self.tableView = QtWidgets.QTableWidget(Form)
        self.tableView.setGeometry(QtCore.QRect(190, 40, 521, 351))
        self.tableView.setRowCount(len(num))
        self.tableView.setColumnCount(len(num[0]))
        for i,row in enumerate(num):
            for j,val in enumerate(row):
                self.tableView.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))
        '''
        
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        '''
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 141, 391))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.MSD_clu = QtWidgets.QCheckBox(self.groupBox)
        self.MSD_clu.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.MSD_clu.setObjectName("MSD_clu")
        self.MDS_Label = QtWidgets.QCheckBox(self.groupBox)
        self.MDS_Label.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.MDS_Label.setObjectName("MDS_Label")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 0, 46, 13))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 200, 141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.DD = QtWidgets.QRadioButton(self.groupBox)
        self.DD.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.DD.setObjectName("DD")
        self.ddd = QtWidgets.QRadioButton(self.groupBox)
        self.ddd.setGeometry(QtCore.QRect(60, 20, 82, 17))
        self.ddd.setObjectName("ddd")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 141, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_2.setObjectName("label_2")
        self.MDS_Plot = QtWidgets.QToolButton(self.groupBox)
        self.MDS_Plot.setGeometry(QtCore.QRect(10, 90, 91, 19))
        self.MDS_Plot.setObjectName("MDS_Plot")
        self.HM_Plot = QtWidgets.QToolButton(self.groupBox)
        self.HM_Plot.setGeometry(QtCore.QRect(10, 180, 91, 19))
        self.HM_Plot.setObjectName("HM_Plot")
        self.dendro = QtWidgets.QCheckBox(self.groupBox)
        self.dendro.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.dendro.setObjectName("dendro")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 81, 16))
        self.label_3.setObjectName("label_3")
        self.Auto_scale = QtWidgets.QCheckBox(self.groupBox)
        self.Auto_scale.setGeometry(QtCore.QRect(10, 260, 70, 17))
        self.Auto_scale.setObjectName("Auto_scale")
        self.hist_plot = QtWidgets.QToolButton(self.groupBox)
        self.hist_plot.setGeometry(QtCore.QRect(10, 280, 91, 19))
        self.hist_plot.setObjectName("hist_plot")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 300, 141, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.center_clu = QtWidgets.QCheckBox(self.groupBox)
        self.center_clu.setGeometry(QtCore.QRect(10, 340, 70, 17))
        self.center_clu.setObjectName("center_clu")
        self.Compute_cen = QtWidgets.QToolButton(self.groupBox)
        self.Compute_cen.setGeometry(QtCore.QRect(10, 370, 91, 19))
        self.Compute_cen.setObjectName("Compute_cen")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.HM_Plot.clicked.connect(self.OpenHM)
        self.MDS_Plot.clicked.connect(self.plot_MDS)
        self.hist_plot.clicked.connect(self.Hist)
        self.Compute_cen.clicked.connect(self.OpenCenter)
        '''
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BackToMain = QtWidgets.QPushButton(Form)
        self.BackToMain.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.BackToMain.setObjectName("BackToMain")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(384, 440, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        '''
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
      
        self.label.setText(_translate("Form", "Tree Distance Matrix"))
       
 
              
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MSD_clu.setText(_translate("Form", "Cluster"))
        self.MDS_Label.setText(_translate("Form", "Labels"))
        self.label.setText(_translate("Form", "MDS:"))
        self.DD.setText(_translate("Form", "2D"))
        self.ddd.setText(_translate("Form", "3D"))
        self.label_2.setText(_translate("Form", "Heat Map:"))
        self.MDS_Plot.setText(_translate("Form", "Plot "))
        self.HM_Plot.setText(_translate("Form", "Plot "))
        self.dendro.setText(_translate("Form", "Include Dendrogram"))
        self.label_3.setText(_translate("Form", "Distribution:"))
        self.Auto_scale.setText(_translate("Form", "Auto-scale"))
        self.hist_plot.setText(_translate("Form", "Plot "))
        self.center_clu.setText(_translate("Form", "Cluster"))
        self.Compute_cen.setText(_translate("Form", "Compute"))
        self.label_4.setText(_translate("Form", "Center trees:"))
        self.label_5.setText(_translate("Form", "TreeDistance Results"))
        self.label_6.setText(_translate("Form", "Options and analysis"))
    def plot_MDS(self):
        
 
        
        distances=self.Matrix
        distArray = ssd.squareform(distances)
        arr =np.array(self.dists)
        if(self.MSD_clu.isChecked()): 
            linkage_matrix = ward(distArray)
            
            fc= hier.fcluster(linkage_matrix, 6, criterion='maxclust')
          
         
        else: fc="b"
       
        if self.DD.isChecked(): 
            mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
            pos = mds.fit_transform(distances)
            xs, ys = pos[:, 0], pos[:, 1]
           
            plt.scatter(xs, ys, c=fc)
            Tree_count=1
            if(self.MDS_Label.isChecked()):
                for x, y in zip(xs, ys):
                        
                    plt.text(x, y, "tree" + str(Tree_count))
                    Tree_count+=1
            
            plt.show()
        else:
            fig = plt.figure()
            subpl = fig.add_subplot(111,projection='3d')
            mds = MDS(n_components=3,dissimilarity="precomputed", random_state=6)
            pos = mds.fit_transform(distances)
           
            xs, ys,zs = pos[:, 0], pos[:, 1], pos[:, 2]
            subpl.scatter(pos[:, 0], pos[:, 1], pos[:, 2],c=fc)
            Tree_count=1
            if(self.MDS_Label.isChecked()):
                for x, y,z in zip(xs, ys, zs):
                    subpl.text(x, y, z, "tree"+ str(Tree_count))
                    Tree_count+=1
            plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

