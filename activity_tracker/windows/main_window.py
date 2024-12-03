# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(60, 20, 681, 131))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel {\n"
"    color: #4A90E2;           /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u2014 \u043a\u0440\u0430\u0441\u0438\u0432\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"/* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 \u043e\u0442 \u0431\u0435\u043b\u043e\u0433\u043e \u043a \u0441\u0432\u0435\u0442\u043b\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u043c\u0443 */\n"
"    padding: 10px;            /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);  /* \u0422\u0435\u043d\u044c \u0434\u043b\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #1A73E8;  /* \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438"
                        " \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 2px solid #4A90E2;  /* \u041f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u0430 \u0441\u0438\u043d\u0435\u0439 \u0440\u0430\u043c\u043a\u043e\u0439 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}\n"
"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 340, 490, 91))
        self.auth_layout = QHBoxLayout(self.widget)
        self.auth_layout.setObjectName(u"auth_layout")
        self.auth_layout.setContentsMargins(0, 0, 0, 0)
        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.login_button.setFont(font1)
        self.login_button.setStyleSheet(u"QPushButton {\n"
"    color: #000000;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #333333;  /* \u0422\u043e\u043d\u043a\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0442\u0451\u043c\u043d\u043e\u0433\u043e \u0446\u0432\u0435\u0442\u0430 */\n"
"    padding: 10px;              /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430 */\n"
"    border-radius: 5px;         /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444444;  /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0447\u0451\u0440\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222222;  /* \u041e\u0447\u0435\u043d\u044c \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438"
                        " \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.auth_layout.addWidget(self.login_button)

        self.reg_button = QPushButton(self.widget)
        self.reg_button.setObjectName(u"reg_button")
        self.reg_button.setFont(font1)
        self.reg_button.setAutoFillBackground(False)
        self.reg_button.setStyleSheet(u"QPushButton {\n"
"    color: #000000;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #333333;  /* \u0422\u043e\u043d\u043a\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0442\u0451\u043c\u043d\u043e\u0433\u043e \u0446\u0432\u0435\u0442\u0430 */\n"
"    padding: 10px;              /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430 */\n"
"    border-radius: 5px;         /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444444;  /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0447\u0451\u0440\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222222;  /* \u041e\u0447\u0435\u043d\u044c \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438"
                        " \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.auth_layout.addWidget(self.reg_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Activity tracker", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043a\u0435\u0440 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.reg_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

