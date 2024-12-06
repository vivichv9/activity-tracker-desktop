import json

import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow
from activity_tracker.service import ActivityTracker
from activity_tracker.windows.login_window import Ui_login_window


class LoginForm(QMainWindow):
    login_success = Signal()

    def __init__(self, tracker):
        super().__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.tracker = tracker
        self.ui.login_button.clicked.connect(self.get_login_data)
        self.ui.cancel_button.clicked.connect(self.close)


    def get_login_data(self, main):
        email = self.ui.email_input.toPlainText()
        pwd = self.ui.pwd_input.toPlainText()

        params = {
            'email': email,
            'password': pwd
        }

        res = requests.post('http://127.0.0.1:8000/auth/login/', data=json.dumps(params))

        if res.status_code == 200:
            data = res.json()
            ActivityTracker.ACCESS_TOKEN = data['access_token']
            ActivityTracker.REFRESH_TOKEN = data['refresh_token']
            ActivityTracker.TOKEN = data['token_type']


        else:
            QtWidgets.QMessageBox.critical(self, "Error!", res.text)

        if res.status_code == 200:
            self.close()
            self.login_success.emit()
        else:
            QtWidgets.QMessageBox.critical(self, "Error!", res.text)
