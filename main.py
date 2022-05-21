import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from sqlalchemy import false, func, true
from sympy import N
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, qApp
from PyQt5.QtCore import QCoreApplication
import time
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import socket

class Step1Window(QMainWindow):

    

    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('step1.ui',self)
        self.show()
        
        #사용자가 버튼 누르면 선택됐다고 시각적으로 보여지는 부분
        self.pushButton_8.clicked.connect(self.button8)
        self.pushButton_9.clicked.connect(self.button9)
        self.pushButton_10.clicked.connect(self.button10)
        self.pushButton_11.clicked.connect(self.button11)

        self.pushButton.clicked.connect(self.button)
    
    def button8(self):
        
        self.pushButton_8.setStyleSheet('background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        
       

    def button9(self):
       

        self.pushButton_9.setStyleSheet('background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        

    def button10(self):
        
        self.pushButton_10.setStyleSheet('background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')

    def button11(self):
        
        self.pushButton_11.setStyleSheet('background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet('background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        

    def button(self):
        
        self.close()
        Step2Window()  

class Step2Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step2.ui',self)
        self.show()
    
        self.pushButton.clicked.connect(self.button)

    def button(self):
        self.close()
        Step3Window()
        
class Step3Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step3.ui',self)
        self.show()
    
        self.pushButton.clicked.connect(self.button)

    def button(self):
        self.close()
        Step4Window()
        
class Step4Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step4.ui',self)
        self.show()
        
        ip=socket.gethostbyname(socket.gethostname())

        self.label_11.setText("현재 장치의 ip주소\n\n" + ip)
        
        self.pushButton.clicked.connect(self.button)
    

    def button(self):
        self.close()
        ListingWindow()

class ListingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('listing.ui',self)
        self.show()
    
       

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('main.ui',self)
        self.show()
        self.pushButton_3.clicked.connect(self.button3)

    def button3(self):
        self.close()
        Step1Window()
    
   

    
    

    


       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow()

    sys.exit(app.exec_())