# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_friend.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(492, 375)
        Dialog.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.add_friend = QPushButton(Dialog)
        self.add_friend.setObjectName(u"add_friend")
        self.add_friend.setGeometry(QRect(140, 290, 181, 51))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(16)
        self.add_friend.setFont(font)
        self.add_friend.setStyleSheet(u"color: #000000")
        self.username_label = QLabel(Dialog)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(20, 170, 121, 69))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(18)
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"color: #000000;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 331, 121))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(23)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
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
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 170, 262, 69))
        self.textEdit.setStyleSheet(u"color: #000000")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_friend.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0440\u0443\u0433\u0430", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u0434\u0440\u0443\u0433\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0434\u0440\u0443\u0433\u0430", None))
    # retranslateUi

