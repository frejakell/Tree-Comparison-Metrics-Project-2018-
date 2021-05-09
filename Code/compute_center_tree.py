from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import time,math,sys
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
import numpy as np
import matplotlib.pyplot as plt
class Ui_center(object):
    def setupUi(self, Form,Matrix,list_d, c):
        yourarray=Matrix
      

        center=yourarray.mean(axis=1)
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
        print(mean_tree)
           

        min=0
        first_row=yourarray[0]
        for i in range(0,len(first_row)):
                min+= math.sqrt((first_row[i]-center[i])**2)

        min_tree=[]
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
        text="----------------------------------------------------------------------------------------\n"
        #text+="Cluster ID:"+str(key)+"\n"
        #text+="Cluster tree set:"+ str(clusters[key])+"\n"
        text+="Center tree-approach #1:"+str(mean_tree)+"\n"
        text+="Center tree-approach #2:"+ str(min_tree)+"\n"  
        text+="----------------------------------------------------------------------------------------\n"
        if(c=="Y"):
            distances=Matrix
            distArray = ssd.squareform(distances)
            arr =list_d

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
        self.text=text
        Form.setObjectName("Form")
        Form.resize(587, 515)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 531, 391))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 480, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 480, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 460, 111, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit.setPlainText(text)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()
        self.pushButton_2.clicked.connect(self.write_to_file)
       
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Center tree Summary:"))
        
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.label_2.setText(_translate("Form", "Output to file"))

    def write_to_file(self):
        filename=self.lineEdit.text()
        thefile = open(filename, 'w')
        data=self.text
        thefile.write(data)
        thefile.close()
        self.lineEdit.setText("")
        return None  

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_center()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

