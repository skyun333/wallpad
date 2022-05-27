import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtTest
from sqlalchemy import false, func, true
from sympy import N
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, qApp, QAbstractButton, QVBoxLayout, QDialog
from PyQt5.QtCore import QCoreApplication
import time
from PyQt5.QtCore import Qt, QSize, QEventLoop
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer
import socket
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime


class Step1Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        # 사용자가 버튼 누르면 선택됐다고 시각적으로 보여지는 부분
        self.pushButton_8.clicked.connect(self.button8)
        self.pushButton_9.clicked.connect(self.button9)
        self.pushButton_10.clicked.connect(self.button10)
        self.pushButton_11.clicked.connect(self.button11)

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        FirstWindow()

    def button8(self):

        self.pushButton_8.setStyleSheet(
            'background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')

    def button9(self):

        self.pushButton_9.setStyleSheet(
            'background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')

    def button10(self):

        self.pushButton_10.setStyleSheet(
            'background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_11.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')

    def button11(self):

        self.pushButton_11.setStyleSheet(
            'background-color:rgb(56,67,162); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_8.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_10.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')
        self.pushButton_9.setStyleSheet(
            'background-color:rgb(108, 147, 246); color : rgb(255,255,255); border: 2px solid rgb(255,255,255)')

    def button(self):

        self.close()
        Step2Window()


class Step2Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step2.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.button2)
    
    def button2(self):
        self.close()
        Step1Window()
    
    def home(self):
        self.close()
        FirstWindow()

    def button(self):
        self.close()
        Step3Window()


class Step3Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step3.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.button2)
    
    def button2(self):
        self.close()
        Step2Window()
    
    def home(self):
        self.close()
        FirstWindow()

    def button(self):
        self.close()
        Step4Window()


class Step4Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        ip = socket.gethostbyname(socket.gethostname())

        self.label_11.setText("현재 장치의 ip주소\n\n" + ip)

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.button2)
    
    def button2(self):
        self.close()
        Step3Window()
    
    def home(self):
        self.close()
        FirstWindow()

    def button(self):
        self.close()
        ItemsWindow()


class ItemsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('items.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.button2)
    
    def button2(self):
        self.close()
        Step4Window()
    
    def home(self):
        self.close()
        FirstWindow()

    def button(self):
        self.close()
        ProgressWindow()


class ProgressWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('progress.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        count = 0

        self.movie = QMovie("spinner.gif")
        self.movie.setScaledSize(QSize(61, 61))
        self.label_3.setMovie(self.movie)
        self.movie.start()

        while count < 100:   
            count += 1
            QtTest.QTest.qWait(25)
            if count==17:
                QtTest.QTest.qWait(400)
            if count==55:
                QtTest.QTest.qWait(600)
            if count==88:
                QtTest.QTest.qWait(200)

            self.progressBar.setValue(count)
    
        if count == 100:
            self.label_3.setGeometry(QtCore.QRect(506, 265, 120, 90))
            self.movie = QMovie("done.gif")
            self.movie.setScaledSize(QSize(120, 90))
            self.label_3.setMovie(self.movie)
            self.movie.start()
            self.label_10.setText("점검이 완료되었습니다\n결과를 확인하세요")
            self.pushButton.setText("결과 확인")
        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        FirstWindow()

    def button(self):
        self.close()
        ProresultWindow()


class ProresultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('proresult.ui', self)
        self.pushButton.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_2.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_4.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_5.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.movie = QMovie("red.gif")
        self.movie.setScaledSize(QSize(81, 81))
        self.label_3.setMovie(self.movie)
        self.label_12.setMovie(self.movie)
        self.label_13.setMovie(self.movie)
        self.label_14.setMovie(self.movie)
        self.movie.start()

        self.pushButton.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_4.clicked.connect(self.button4)
        self.pushButton_5.clicked.connect(self.button5)
        self.pushButton_6.clicked.connect(self.button6)
    
    def home(self):
        self.close()
        MainWindow()

    def button(self):
        self.close()
        ResultWindow_wallpad()
    
    def button2(self):
        self.close()
        ResultWindow_app()

    def button4(self):
        self.close()
        ResultWindow_server()

    def button5(self):
        self.close()
        ResultWindow_internet()

    def button6(self):
        self.close()
        MainWindow()




class ResultWindow_wallpad(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_wallpad.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_56.clicked.connect(self.button56)
        self.pushButton_57.clicked.connect(self.button57)
        self.pushButton_54.clicked.connect(self.button54)
        self.pushButton_53.clicked.connect(self.button53)

    def button54(self):
        feedback_wallpad_3()
    
    def button53(self):
        feedback_wallpad_4()  
    
    def button56(self):
        feedback_wallpad_1()
    
    def button57(self):
        feedback_wallpad_2()  
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        ProresultWindow()

class ResultWindow_app(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_app.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        ProresultWindow()

class ResultWindow_server(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_server.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        ProresultWindow()

class ResultWindow_internet(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_internet.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        ProresultWindow()


class ResultWindow_wallpad_after(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_wallpad.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        MainWindow()

    

class feedback_wallpad_1(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('feedback/feedback_wallpad_1.ui', self)
        
        self.show()

        self.pushButton_4.clicked.connect(self.button4)
       
    def button4(self):
        self.close()

class feedback_wallpad_2(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('feedback/feedback_wallpad_2.ui', self)
        
        self.show()

        self.pushButton_4.clicked.connect(self.button4)
       
    def button4(self):
        self.close()

class feedback_wallpad_3(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('feedback/feedback_wallpad_3.ui', self)
        
        self.show()

        self.pushButton_4.clicked.connect(self.button4)
       
    def button4(self):
        self.close()

class feedback_wallpad_4(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('feedback/feedback_wallpad_4.ui', self)
        
        self.show()

        self.pushButton_4.clicked.connect(self.button4)
       
    def button4(self):
        self.close()

class ResultWindow_app_after(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_app.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        MainWindow()

class ResultWindow_server_after(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_server.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        MainWindow()

class ResultWindow_internet_after(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('result_internet.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
    
    def home(self):
        self.close()
        MainWindow()
    
    def button2(self):
        self.close()
        MainWindow()



class ScrollWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('scrollbar.ui', self)

        self.show()

        
class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('firstmain.ui',self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()
        self.pushButton_3.clicked.connect(self.button3)

    def button3(self):
        self.close()
        Step1Window()





    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('main.ui', self)
        

        self.pushButton.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_2.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_4.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.pushButton_5.setStyleSheet(
                        "background-color: #00ff0000;"
                        "selection-color: #00ff0000;"
                        "selection-background-color: #00ff0000;"
                        )
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()
        datetime = QDateTime.currentDateTime()
        self.label_6.setText(datetime.toString('yyyy.MM.dd, hh:mm'))
        self.pushButton_3.clicked.connect(self.button3)

        self.movie = QMovie("red.gif")
        self.movie.setScaledSize(QSize(81, 81))
        self.label_10.setMovie(self.movie)
        self.label_11.setMovie(self.movie)
        self.label_12.setMovie(self.movie)
        self.label_13.setMovie(self.movie)
        self.movie.start()

        self.pushButton.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_4.clicked.connect(self.button4)
        self.pushButton_5.clicked.connect(self.button5)

    def button3(self):
        self.close()
        Step1Window()

    def button(self):
        self.close()
        ResultWindow_wallpad_after()

    def button2(self):
        self.close()
        ResultWindow_app_after()
    
    def button4(self):
        self.close()
        ResultWindow_server_after()
    
    def button5(self):
        self.close()
        ResultWindow_internet_after()



        

class first(QDialog):
    def __init__(self):
            super().__init__()
            self.ui = uic.loadUi('feedback/feedback1.ui', self)
            self.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Result_exampleWindow()
    FirstWindow()
    #window =first()
    #window.show()

    sys.exit(app.exec_())


