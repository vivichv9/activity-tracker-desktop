# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_activity.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_add_activity_form(object):
    def __init__(self):
        self.add_activity_button = None

    def setupUi(self, add_activity_form):
        if not add_activity_form.objectName():
            add_activity_form.setObjectName(u"add_activity_form")
        add_activity_form.resize(400, 300)
        add_activity_form.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.comboBox = QComboBox(add_activity_form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 90, 241, 101))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(46)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"color: #000000")
        self.label = QLabel(add_activity_form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 341, 41))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #000000")
        self.add_activity_button = QPushButton(add_activity_form)
        self.add_activity_button.setObjectName(u"add_activity_button")
        self.add_activity_button.setGeometry(QRect(70, 230, 261, 51))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(14)
        self.add_activity_button.setFont(font2)
        self.add_activity_button.setStyleSheet(u"color: #000000")

        self.retranslateUi(add_activity_form)

        QMetaObject.connectSlotsByName(add_activity_form)
    # setupUi

    def retranslateUi(self, add_activity_form):
        add_activity_form.setWindowTitle(QCoreApplication.translate("add_activity_form", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("add_activity_form", u"run", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("add_activity_form", u"walk", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("add_activity_form", u"gym", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("add_activity_form", u"jump", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("add_activity_form", u"swim", None))

        self.label.setText(QCoreApplication.translate("add_activity_form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.add_activity_button.setText(QCoreApplication.translate("add_activity_form", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u0442\u044c \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
    # retranslateUi

