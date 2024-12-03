# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.resize(400, 317)
        login_window.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.login_frame = QFrame(login_window)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setGeometry(QRect(0, 10, 391, 281))
        self.login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login_button = QPushButton(self.login_frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(150, 240, 141, 25))
        self.login_button.setStyleSheet(u"color: #000000")
        self.cancel_button = QPushButton(self.login_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(300, 240, 75, 25))
        self.cancel_button.setStyleSheet(u"color: #000000")
        self.login_email_label = QLabel(self.login_frame)
        self.login_email_label.setObjectName(u"login_email_label")
        self.login_email_label.setGeometry(QRect(50, 50, 61, 21))
        self.login_email_label.setStyleSheet(u"color: #000000;")
        self.login_pwd_label = QLabel(self.login_frame)
        self.login_pwd_label.setObjectName(u"login_pwd_label")
        self.login_pwd_label.setGeometry(QRect(50, 100, 71, 21))
        self.login_pwd_label.setStyleSheet(u"color: #000000;")
        self.email_input = QTextEdit(self.login_frame)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(150, 40, 231, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        font.setBold(True)
        self.email_input.setFont(font)
        self.email_input.setStyleSheet(u"color: #000000;")
        self.pwd_input = QTextEdit(self.login_frame)
        self.pwd_input.setObjectName(u"pwd_input")
        self.pwd_input.setGeometry(QRect(150, 90, 231, 31))
        self.pwd_input.setFont(font)
        self.pwd_input.setStyleSheet(u"color: #000000;")

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"Dialog", None))
        self.login_button.setText(QCoreApplication.translate("login_window", u"\u0432\u043e\u0439\u0442\u0438", None))
        self.cancel_button.setText(QCoreApplication.translate("login_window", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
        self.login_email_label.setText(QCoreApplication.translate("login_window", u"Email", None))
        self.login_pwd_label.setText(QCoreApplication.translate("login_window", u"password", None))
        self.email_input.setHtml(QCoreApplication.translate("login_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pwd_input.setHtml(QCoreApplication.translate("login_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

