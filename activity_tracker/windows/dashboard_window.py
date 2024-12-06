# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSplitter,
    QWidget)

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(805, 501)
        dashboard.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 1, \n"
"    stop: 0 #A8D8FF, stop: 1 #F0E1FF\n"
");\n"
"font-family: \"Noto Sans\";")
        self.dashboard_title = QLabel(dashboard)
        self.dashboard_title.setObjectName(u"dashboard_title")
        self.dashboard_title.setGeometry(QRect(0, 0, 321, 101))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.dashboard_title.setFont(font)
        self.dashboard_title.setStyleSheet(u"QLabel {\n"
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
        self.points_label = QLabel(dashboard)
        self.points_label.setObjectName(u"points_label")
        self.points_label.setGeometry(QRect(340, 60, 131, 21))
        self.points_label.setStyleSheet(u"color: #000000;")
        self.username_label = QLabel(dashboard)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(340, 20, 131, 21))
        self.username_label.setStyleSheet(u"color: #000000;")
        self.splitter_2 = QSplitter(dashboard)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 450, 641, 25))
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.add_activity = QPushButton(self.splitter_2)
        self.add_activity.setObjectName(u"add_activity")
        self.add_activity.setStyleSheet(u"color: #000000")
        self.splitter_2.addWidget(self.add_activity)
        self.list_activity = QPushButton(self.splitter_2)
        self.list_activity.setObjectName(u"list_activity")
        self.list_activity.setStyleSheet(u"color: #000000")
        self.splitter_2.addWidget(self.list_activity)
        self.add_friend = QPushButton(self.splitter_2)
        self.add_friend.setObjectName(u"add_friend")
        self.add_friend.setStyleSheet(u"color: #000000")
        self.splitter_2.addWidget(self.add_friend)
        self.friend_list_button = QPushButton(self.splitter_2)
        self.friend_list_button.setObjectName(u"friend_list_button")
        self.friend_list_button.setStyleSheet(u"color: #000000")
        self.splitter_2.addWidget(self.friend_list_button)
        self.achievements_button = QPushButton(self.splitter_2)
        self.achievements_button.setObjectName(u"achievements_button")
        self.achievements_button.setStyleSheet(u"color: #000000")
        self.splitter_2.addWidget(self.achievements_button)
        self.end_activity = QPushButton(dashboard)
        self.end_activity.setObjectName(u"end_activity")
        self.end_activity.setGeometry(QRect(10, 420, 158, 25))
        self.end_activity.setStyleSheet(u"color: #000000")
        self.current_train_label = QLabel(dashboard)
        self.current_train_label.setObjectName(u"current_train_label")
        self.current_train_label.setGeometry(QRect(340, 100, 131, 21))
        self.current_train_label.setStyleSheet(u"color: #000000;")
        self.delete_friend_button = QPushButton(dashboard)
        self.delete_friend_button.setObjectName(u"delete_friend_button")
        self.delete_friend_button.setGeometry(QRect(320, 420, 117, 25))
        self.delete_friend_button.setStyleSheet(u"color: #000000")
        self.username = QLabel(dashboard)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(490, 20, 131, 21))
        self.username.setStyleSheet(u"color: #000000;")
        self.points = QLabel(dashboard)
        self.points.setObjectName(u"points")
        self.points.setGeometry(QRect(490, 60, 131, 21))
        self.points.setStyleSheet(u"color: #000000;")
        self.active_train = QLabel(dashboard)
        self.active_train.setObjectName(u"active_train")
        self.active_train.setGeometry(QRect(490, 100, 131, 21))
        self.active_train.setStyleSheet(u"color: #000000;")
        self.widget = QWidget(dashboard)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 184, 782, 194))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_last_activity = QListWidget(self.widget)
        self.list_last_activity.setObjectName(u"list_last_activity")
        self.list_last_activity.setStyleSheet(u"color: #000000")

        self.horizontalLayout.addWidget(self.list_last_activity)

        self.achievements_list = QListWidget(self.widget)
        self.achievements_list.setObjectName(u"achievements_list")
        self.achievements_list.setStyleSheet(u"color: #000000;")

        self.horizontalLayout.addWidget(self.achievements_list)

        self.friends_list = QListWidget(self.widget)
        self.friends_list.setObjectName(u"friends_list")
        self.friends_list.setStyleSheet(u"color: #000000;")

        self.horizontalLayout.addWidget(self.friends_list)

        self.widget1 = QWidget(dashboard)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 161, 781, 19))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.last_activity_label = QLabel(self.widget1)
        self.last_activity_label.setObjectName(u"last_activity_label")
        self.last_activity_label.setStyleSheet(u"color: #000000;")

        self.horizontalLayout_2.addWidget(self.last_activity_label)

        self.achievements_label = QLabel(self.widget1)
        self.achievements_label.setObjectName(u"achievements_label")
        self.achievements_label.setStyleSheet(u"color: #000000;")

        self.horizontalLayout_2.addWidget(self.achievements_label)

        self.friends_label = QLabel(self.widget1)
        self.friends_label.setObjectName(u"friends_label")
        self.friends_label.setStyleSheet(u"color: #000000;")

        self.horizontalLayout_2.addWidget(self.friends_label)


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.dashboard_title.setText(QCoreApplication.translate("dashboard", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.points_label.setText(QCoreApplication.translate("dashboard", u"\u0411\u0430\u043b\u043b\u044b", None))
        self.username_label.setText(QCoreApplication.translate("dashboard", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.add_activity.setText(QCoreApplication.translate("dashboard", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0443", None))
        self.list_activity.setText(QCoreApplication.translate("dashboard", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043e\u043a", None))
        self.add_friend.setText(QCoreApplication.translate("dashboard", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0440\u0443\u0433\u0430", None))
        self.friend_list_button.setText(QCoreApplication.translate("dashboard", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u0440\u0443\u0437\u0435\u0439", None))
        self.achievements_button.setText(QCoreApplication.translate("dashboard", u"\u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.end_activity.setText(QCoreApplication.translate("dashboard", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0443", None))
        self.current_train_label.setText(QCoreApplication.translate("dashboard", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.delete_friend_button.setText(QCoreApplication.translate("dashboard", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0440\u0443\u0433\u0430", None))
        self.username.setText(QCoreApplication.translate("dashboard", u"username", None))
        self.points.setText(QCoreApplication.translate("dashboard", u"points", None))
        self.active_train.setText(QCoreApplication.translate("dashboard", u"active_train", None))
        self.last_activity_label.setText(QCoreApplication.translate("dashboard", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.achievements_label.setText(QCoreApplication.translate("dashboard", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.friends_label.setText(QCoreApplication.translate("dashboard", u"                   \u0414\u0440\u0443\u0437\u044c\u044f", None))
    # retranslateUi

