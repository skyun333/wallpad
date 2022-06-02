import sys
import ctypes
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
import random
import webbrowser

myappid = 'slow_heart.png'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Step1Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()
        global UART_flag
        global RS_flag
        UART_flag = 0
        RS_flag = 0

        # 사용자가 버튼 누르면 선택됐다고 시각적으로 보여지는 부분
        self.pushButton_8.clicked.connect(self.button8)
        self.pushButton_9.clicked.connect(self.button9)
        self.pushButton_10.clicked.connect(self.button10)
        self.pushButton_11.clicked.connect(self.button11)

        self.pushButton.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.home)
        self.label_16.setHidden(True)
        self.label_17.setHidden(True)

        self.toolButton.clicked.connect(self.tool)
        self.toolButton_2.clicked.connect(self.tool2)

    def tool(self):
        global UART_flag

        if UART_flag == 0:
            self.label_16.setHidden(False)
            UART_flag = 1
        elif UART_flag == 1:
            self.label_16.setHidden(True)
            UART_flag = 0
        print(UART_flag)

    def tool2(self):
        global RS_flag

        if RS_flag == 0:
            self.label_17.setHidden(False)
            RS_flag = 1
        elif RS_flag == 1:
            self.label_17.setHidden(True)
            RS_flag = 0
        print(RS_flag)

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

        self.addItem()

    def addItem(self):
        
        QtTest.QTest.qWait(5000)
        self.listWidget.addItem('COM5')

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
        count = 0

        self.ui = uic.loadUi('step4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.movie = QMovie("spinner2.gif")
        self.movie.setScaledSize(QSize(115, 115))
        self.movie.start()
        self.label_41.setMovie(self.movie)
        self.label_42.setMovie(self.movie)
        self.label_43.setMovie(self.movie)
        self.label_44.setMovie(self.movie)
        self.label_45.setMovie(self.movie)
        self.label_46.setMovie(self.movie)
        self.label_47.setMovie(self.movie)
        self.label_48.setMovie(self.movie)
        self.label_49.setMovie(self.movie)
        self.label_50.setMovie(self.movie)
        self.label_51.setMovie(self.movie)
        self.label_52.setMovie(self.movie)
        self.label_53.setMovie(self.movie)
        self.label_54.setMovie(self.movie)

        self.label_68.setMovie(self.movie)
        self.label_69.setMovie(self.movie)
        self.label_70.setMovie(self.movie)

        self.label_73.setMovie(self.movie)
        self.label_74.setMovie(self.movie)
        self.label_75.setMovie(self.movie)

        while count < 100:
            count += 1
            QtTest.QTest.qWait(25)

        if count == 100:  # 점검 완료 시
            count = 0
            self.movie = QMovie("done.gif")
            self.movie.setScaledSize(QSize(100, 75))
            self.label_44.setMovie(self.movie)
            self.label_68.setMovie(self.movie)
            self.label_75.setMovie(self.movie)
            self.movie.start()

            self.movie = QMovie("no.gif")
            self.movie.setScaledSize(QSize(30, 30))

            self.label_54.setMovie(self.movie)
            self.label_53.setMovie(self.movie)
            self.label_52.setMovie(self.movie)
            self.label_51.setMovie(self.movie)
            self.label_50.setMovie(self.movie)
            self.label_49.setMovie(self.movie)
            self.label_48.setMovie(self.movie)
            self.label_47.setMovie(self.movie)
            self.label_46.setMovie(self.movie)
            self.label_45.setMovie(self.movie)
            self.label_43.setMovie(self.movie)
            self.label_42.setMovie(self.movie)
            self.label_41.setMovie(self.movie)

            self.label_70.setMovie(self.movie)
            self.label_69.setMovie(self.movie)

            self.label_73.setMovie(self.movie)
            self.label_74.setMovie(self.movie)

            for num in range(12, 33):
                #QtTest.QTest.qWait(random.randrange(1, 500))

                try:
                    label = getattr(self, 'label_{}'.format(num))
                    label.setStyleSheet("border: 1px solid rgb(223, 223, 223);"
                                        "border-radius: 6px;"
                                        "padding-left: 3px;"
                                        "background-color: rgb(223,223,223);"
                                        "color:rgb(161, 161, 161);"

                                        )
                except:
                    pass

            self.label_19.setStyleSheet(
                "border: 1px solid rgb(223, 223, 223);"
                "border-radius: 6px;"
                "padding-left: 3px;"
                "background-color:rgb(120, 179, 72);"
                "color:rgb(255,255,255);"
            )

            self.label_26.setStyleSheet(
                "border: 1px solid rgb(223, 223, 223);"
                "border-radius: 6px;"
                "padding-left: 3px;"
                "background-color:rgb(120, 179, 72);"
                "color:rgb(255,255,255);"
            )

            self.label_80.setStyleSheet(
                "border: 1px solid rgb(223, 223, 223);"
                "border-radius: 6px;"
                "padding-left: 3px;"
                "background-color:rgb(120, 179, 72);"
                "color:rgb(255,255,255);"
            )

            self.movie.start()

            while count < 100:
                count += 1
                QtTest.QTest.qWait(17)

            self.movie = QMovie("done_png.png")
            self.movie.setScaledSize(QSize(100, 75))

            self.label_44.setMovie(self.movie)
            self.label_68.setMovie(self.movie)
            self.label_75.setMovie(self.movie)

            self.movie.start()

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
        Step5Window()


class Step5Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('step5.ui', self)
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
        global mac
        mac = str(self.lineEdit.text())

        global admin_pw
        admin_pw = str(self.lineEdit_2.text())

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
            if count == random.randrange(1, 20):
                QtTest.QTest.qWait(400)
            if count == random.randrange(21, 60):
                QtTest.QTest.qWait(600)
            if count == random.randrange(61, 99):
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
        self.commandLinkButton.clicked.connect(lambda: webbrowser.open('https://url.kr/z3omh7'))

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
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5
        self.pushButton_58.clicked.connect(self.button58)  # 6
        self.pushButton_52.clicked.connect(self.button52)  # 7
        self.pushButton_59.clicked.connect(self.button59)  # 8
        self.pushButton_67.clicked.connect(self.button67)  # 9
        self.pushButton_66.clicked.connect(self.button66)  # 10
        self.pushButton_65.clicked.connect(self.button65)  # 11
        self.pushButton_70.clicked.connect(self.button70)  # 12
        self.pushButton_68.clicked.connect(self.button68)  # 13
        self.pushButton_69.clicked.connect(self.button69)  # 14
        self.pushButton_72.clicked.connect(self.button72)  # 15
        self.pushButton_71.clicked.connect(self.button71)  # 16
        self.pushButton_60.clicked.connect(self.button60)  # 17
        self.pushButton_61.clicked.connect(self.button61)  # 18
        self.pushButton_62.clicked.connect(self.button62)  # 19
        self.pushButton_63.clicked.connect(self.button63)  # 20
        self.pushButton_64.clicked.connect(self.button64)  # 21
        self.pushButton_73.clicked.connect(self.button73)  # 22

    def button55(self):
        feedback_wallpad_5()

    def button58(self):
        feedback_wallpad_6()

    def button52(self):
        feedback_wallpad_7()

    def button59(self):
        feedback_wallpad_8()

    def button67(self):
        feedback_wallpad_9()

    def button66(self):
        feedback_wallpad_10()

    def button65(self):
        feedback_wallpad_11()

    def button70(self):
        feedback_wallpad_12()

    def button68(self):
        feedback_wallpad_13()

    def button69(self):
        feedback_wallpad_14()

    def button72(self):
        feedback_wallpad_15()

    def button71(self):
        feedback_wallpad_16()

    def button60(self):
        feedback_wallpad_17()

    def button61(self):
        feedback_wallpad_18()

    def button62(self):
        feedback_wallpad_19()

    def button63(self):
        feedback_wallpad_20()

    def button64(self):
        feedback_wallpad_21()

    def button73(self):
        feedback_wallpad_22()

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
        self.pushButton_85.clicked.connect(self.button85)  # 1
        self.pushButton_86.clicked.connect(self.button86)  # 2
        self.pushButton_87.clicked.connect(self.button87)  # 3
        self.pushButton_83.clicked.connect(self.button83)  # 4
        self.pushButton_88.clicked.connect(self.button88)  # 5
        self.pushButton_84.clicked.connect(self.button84)  # 6

    def button85(self):
        feedback_app_1()

    def button86(self):
        feedback_app_2()

    def button87(self):
        feedback_app_3()

    def button83(self):
        feedback_app_4()

    def button88(self):
        feedback_app_5()

    def button84(self):
        feedback_app_6()

    def home(self):
        self.close()
        MainWindow()

    def button2(self):
        self.close()
        ProresultWindow()


class feedback_app_1(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_app_2(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_2.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_app_3(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_3.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_app_4(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_app_5(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_5.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_app_6(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_app_6.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class ResultWindow_server(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('result_server.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5
        self.pushButton_58.clicked.connect(self.button58)  # 6
        self.pushButton_59.clicked.connect(self.button59)  # 7

    def button56(self):
        feedback_server_1()

    def button57(self):
        feedback_server_2()

    def button54(self):
        feedback_server_3()

    def button53(self):
        feedback_server_4()

    def button55(self):
        feedback_server_5()

    def button58(self):
        feedback_server_6()

    def button59(self):
        feedback_server_7()

    def home(self):
        self.close()
        MainWindow()

    def button2(self):
        self.close()
        ProresultWindow()


class feedback_server_1(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_2(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_2.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_3(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_3.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_4(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_5(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_5.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_6(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_6.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_server_7(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_server_7.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class ResultWindow_internet(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('result_internet.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5

    def button56(self):
        feedback_internet_1()

    def button57(self):
        feedback_internet_2()

    def button54(self):
        feedback_internet_3()

    def button53(self):
        feedback_internet_4()

    def button55(self):
        feedback_internet_5()

    def home(self):
        self.close()
        MainWindow()

    def button2(self):
        self.close()
        ProresultWindow()


class feedback_internet_1(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_internet_1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_internet_2(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_internet_2.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_internet_3(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_internet_3.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_internet_4(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_internet_4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_internet_5(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_internet_5.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class ResultWindow_wallpad_after(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('result_wallpad.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('월패드 보안 점검 툴')
        self.show()

        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5
        self.pushButton_58.clicked.connect(self.button58)  # 6
        self.pushButton_52.clicked.connect(self.button52)  # 7
        self.pushButton_59.clicked.connect(self.button59)  # 8
        self.pushButton_67.clicked.connect(self.button67)  # 9
        self.pushButton_66.clicked.connect(self.button66)  # 10
        self.pushButton_65.clicked.connect(self.button65)  # 11
        self.pushButton_70.clicked.connect(self.button70)  # 12
        self.pushButton_68.clicked.connect(self.button68)  # 13
        self.pushButton_69.clicked.connect(self.button69)  # 14
        self.pushButton_72.clicked.connect(self.button72)  # 15
        self.pushButton_71.clicked.connect(self.button71)  # 16
        self.pushButton_60.clicked.connect(self.button60)  # 17
        self.pushButton_61.clicked.connect(self.button61)  # 18
        self.pushButton_62.clicked.connect(self.button62)  # 19
        self.pushButton_63.clicked.connect(self.button63)  # 20
        self.pushButton_64.clicked.connect(self.button64)  # 21
        self.pushButton_73.clicked.connect(self.button73)  # 22

    def button55(self):
        feedback_wallpad_5()

    def button58(self):
        feedback_wallpad_6()

    def button52(self):
        feedback_wallpad_7()

    def button59(self):
        feedback_wallpad_8()

    def button67(self):
        feedback_wallpad_9()

    def button66(self):
        feedback_wallpad_10()

    def button65(self):
        feedback_wallpad_11()

    def button70(self):
        feedback_wallpad_12()

    def button68(self):
        feedback_wallpad_13()

    def button69(self):
        feedback_wallpad_14()

    def button72(self):
        feedback_wallpad_15()

    def button71(self):
        feedback_wallpad_16()

    def button60(self):
        feedback_wallpad_17()

    def button61(self):
        feedback_wallpad_18()

    def button62(self):
        feedback_wallpad_19()

    def button63(self):
        feedback_wallpad_20()

    def button64(self):
        feedback_wallpad_21()

    def button73(self):
        feedback_wallpad_22()

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
        MainWindow()


class feedback_wallpad_1(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_1.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_2(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_2.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_3(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_3.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_4(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_4.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_5(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_5.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_6(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_6.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_7(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_7.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_8(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_8.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_9(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_9.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_10(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_10.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_11(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_11.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_12(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_12.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_13(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_13.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_14(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_14.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_15(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_15.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_16(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_16.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_17(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_17.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_18(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_18.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_19(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_19.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_20(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_20.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_21(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_21.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

        self.show()

        self.pushButton_4.clicked.connect(self.button4)

    def button4(self):
        self.close()


class feedback_wallpad_22(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('feedback/feedback_wallpad_22.ui', self)
        self.setWindowIcon(QIcon('slow_heart.png'))
        self.setWindowTitle('조치 방법')

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
        self.pushButton_85.clicked.connect(self.button85)  # 1
        self.pushButton_86.clicked.connect(self.button86)  # 2
        self.pushButton_87.clicked.connect(self.button87)  # 3
        self.pushButton_83.clicked.connect(self.button83)  # 4
        self.pushButton_88.clicked.connect(self.button88)  # 5
        self.pushButton_84.clicked.connect(self.button84)  # 6

    def button85(self):
        feedback_app_1()

    def button86(self):
        feedback_app_2()

    def button87(self):
        feedback_app_3()

    def button83(self):
        feedback_app_4()

    def button88(self):
        feedback_app_5()

    def button84(self):
        feedback_app_6()

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
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5
        self.pushButton_58.clicked.connect(self.button58)  # 6
        self.pushButton_59.clicked.connect(self.button59)  # 7

    def button56(self):
        feedback_server_1()

    def button57(self):
        feedback_server_2()

    def button54(self):
        feedback_server_3()

    def button53(self):
        feedback_server_4()

    def button55(self):
        feedback_server_5()

    def button58(self):
        feedback_server_6()

    def button59(self):
        feedback_server_7()

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
        self.pushButton_56.clicked.connect(self.button56)  # 1
        self.pushButton_57.clicked.connect(self.button57)  # 2
        self.pushButton_54.clicked.connect(self.button54)  # 3
        self.pushButton_53.clicked.connect(self.button53)  # 4
        self.pushButton_55.clicked.connect(self.button55)  # 5

    def button56(self):
        feedback_internet_1()

    def button57(self):
        feedback_internet_2()

    def button54(self):
        feedback_internet_3()

    def button53(self):
        feedback_internet_4()

    def button55(self):
        feedback_internet_5()

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

        self.ui = uic.loadUi('firstmain.ui', self)
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

    FirstWindow()

    sys.exit(app.exec_())
