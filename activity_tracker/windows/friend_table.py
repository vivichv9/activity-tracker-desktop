# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'friend_table.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(690, 444)
        Form.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 211, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(14)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #000000;")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 50, 691, 391))
        self.tableWidget.setStyleSheet(u"    font-family: \"Noto Sans\", sans-serif;  /* \u0428\u0440\u0438\u0444\u0442 Noto Sans */\n"
"    color: black;                          /* \u0427\u0435\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: none;                          /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"\n"
"\n"
"\n"
"    text-align: center;                    /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 */\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    text-align: center;                    /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 */\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    section: header;\n"
"    font-weight: bol"
                        "d;                     /* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u044b \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"    height: 30px;                          /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    font-weight: normal;                   /* \u0411\u0435\u0437 \u0436\u0438\u0440\u043d\u043e\u0433\u043e \u0448\u0440\u0438\u0444\u0442\u0430 \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #d3d3d3;             /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0445 \u044f\u0447\u0435\u0435\u043a */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f5f5;             /* \u0426\u0432"
                        "\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QHeaderView {\n"
"    resizeMode: Interactive;               /* \u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u043a\u043e\u043b\u043e\u043d\u043e\u043a \u0438\u0437\u043c\u0435\u043d\u044f\u0435\u043c\u044b\u043c\u0438 \u043f\u043e \u0448\u0438\u0440\u0438\u043d\u0435 */\n"
"}\n"
"\n"
"column {\n"
"    width: 150px;                          /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043e\u043b\u043e\u043d\u043e\u043a \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u0430\u044f */\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u0414\u0440\u0443\u0437\u044c\u044f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0434\u0440\u0443\u0433\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u043a\u0438 \u0434\u0440\u0443\u0433\u0430", None));
    # retranslateUi

