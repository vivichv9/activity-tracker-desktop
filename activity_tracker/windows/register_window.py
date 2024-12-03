# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QWidget)

class Ui_reg_form(object):
    def setupUi(self, reg_form):
        if not reg_form.objectName():
            reg_form.setObjectName(u"reg_form")
        reg_form.resize(400, 300)
        reg_form.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.reg_frame = QFrame(reg_form)
        self.reg_frame.setObjectName(u"reg_frame")
        self.reg_frame.setGeometry(QRect(10, 0, 381, 291))
        self.reg_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.reg_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.reg_email_input = QTextEdit(self.reg_frame)
        self.reg_email_input.setObjectName(u"reg_email_input")
        self.reg_email_input.setGeometry(QRect(110, 40, 221, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        font.setBold(True)
        self.reg_email_input.setFont(font)
        self.reg_email_input.setStyleSheet(u"color: #000000;")
        self.reg_username_input = QTextEdit(self.reg_frame)
        self.reg_username_input.setObjectName(u"reg_username_input")
        self.reg_username_input.setGeometry(QRect(110, 80, 231, 31))
        self.reg_username_input.setFont(font)
        self.reg_username_input.setStyleSheet(u"color: #000000;")
        self.reg_pwd_input = QTextEdit(self.reg_frame)
        self.reg_pwd_input.setObjectName(u"reg_pwd_input")
        self.reg_pwd_input.setGeometry(QRect(110, 120, 231, 31))
        self.reg_pwd_input.setFont(font)
        self.reg_pwd_input.setStyleSheet(u"color: #000000;")
        self.reg_date_input = QDateEdit(self.reg_frame)
        self.reg_date_input.setObjectName(u"reg_date_input")
        self.reg_date_input.setGeometry(QRect(110, 170, 211, 31))
        self.reg_date_input.setFont(font)
        self.reg_date_input.setStyleSheet(u"color: #000000")
        self.reg_email_label = QLabel(self.reg_frame)
        self.reg_email_label.setObjectName(u"reg_email_label")
        self.reg_email_label.setGeometry(QRect(10, 40, 61, 16))
        self.reg_email_label.setStyleSheet(u"color: #000000;")
        self.reg_username_label = QLabel(self.reg_frame)
        self.reg_username_label.setObjectName(u"reg_username_label")
        self.reg_username_label.setGeometry(QRect(10, 80, 61, 16))
        self.reg_username_label.setStyleSheet(u"color: #000000;")
        self.reg_pwd_label = QLabel(self.reg_frame)
        self.reg_pwd_label.setObjectName(u"reg_pwd_label")
        self.reg_pwd_label.setGeometry(QRect(10, 120, 61, 16))
        self.reg_pwd_label.setStyleSheet(u"color: #000000;")
        self.reg_date_label = QLabel(self.reg_frame)
        self.reg_date_label.setObjectName(u"reg_date_label")
        self.reg_date_label.setGeometry(QRect(10, 170, 71, 16))
        self.reg_date_label.setStyleSheet(u"color: #000000;")
        self.reg_button_split = QSplitter(self.reg_frame)
        self.reg_button_split.setObjectName(u"reg_button_split")
        self.reg_button_split.setGeometry(QRect(130, 240, 221, 25))
        self.reg_button_split.setOrientation(Qt.Orientation.Horizontal)
        self.reg_accept_button = QPushButton(self.reg_button_split)
        self.reg_accept_button.setObjectName(u"reg_accept_button")
        self.reg_accept_button.setStyleSheet(u"color: #000000")
        self.reg_button_split.addWidget(self.reg_accept_button)
        self.reg_cancel_button = QPushButton(self.reg_button_split)
        self.reg_cancel_button.setObjectName(u"reg_cancel_button")
        self.reg_cancel_button.setStyleSheet(u"color: #000000")
        self.reg_button_split.addWidget(self.reg_cancel_button)

        self.retranslateUi(reg_form)

        QMetaObject.connectSlotsByName(reg_form)
    # setupUi

    def retranslateUi(self, reg_form):
        reg_form.setWindowTitle(QCoreApplication.translate("reg_form", u"Dialog", None))
        self.reg_email_input.setHtml(QCoreApplication.translate("reg_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.reg_username_input.setHtml(QCoreApplication.translate("reg_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.reg_pwd_input.setHtml(QCoreApplication.translate("reg_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.reg_email_label.setText(QCoreApplication.translate("reg_form", u"Email", None))
        self.reg_username_label.setText(QCoreApplication.translate("reg_form", u"Username", None))
        self.reg_pwd_label.setText(QCoreApplication.translate("reg_form", u"password", None))
        self.reg_date_label.setText(QCoreApplication.translate("reg_form", u"birth date", None))
        self.reg_accept_button.setText(QCoreApplication.translate("reg_form", u"\u0436\u0435\u0441\u0442\u043a\u043e \u0437\u0430\u0440\u0435\u0433\u0430\u0442\u044c\u0441\u044f", None))
        self.reg_cancel_button.setText(QCoreApplication.translate("reg_form", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

