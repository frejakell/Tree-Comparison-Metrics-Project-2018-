
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainPage_final import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.ui.FileFinder.clicked.connect(self.getfiles)
        self.show()
   
    
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
'''from PyQt4.QtGui import *

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      
      
      super(tabdemo, self).__init__(parent)
      self.left = 10
      self.top = 30
      self.width = 640
      self.height = 480
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
      
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"Tab 3")
      self.tab1UI()
      self.tab2UI()
      self.tab3UI()
      self.setWindowTitle("tab demo")
		
   def tab1UI(self):
      self.setGeometry(self.left, self.top, self.width, self.height)
      self.show()
      layout = QFormLayout()
      w = QWidget()

      w.resize(640, 480)

      textBox = QPlainTextEdit(w)
      textBox.move(250, 120)
      layout.addRow("Input text file",QLineEdit())
      layout.addRow("Tree2",QLineEdit())
      layout.addRow(QLabel("Input trees"),textBox)
      self.setTabText(0,"Setup")
      self.tab1.setLayout(layout)
		
   def tab2UI(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())
      self.setTabText(1,"Personal Details")
      self.tab2.setLayout(layout)
		
   def tab3UI(self):
      layout = QHBoxLayout()
      layout.addWidget(QLabel("subjects")) 
      layout.addWidget(QCheckBox("Physics"))
      layout.addWidget(QCheckBox("Maths"))
      self.setTabText(2,"Education Details")
      self.tab3.setLayout(layout)
		
def main():
   
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()'''