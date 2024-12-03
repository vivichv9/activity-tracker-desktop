import json
from datetime import date

import requests
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from activity_tracker.windows.register_window import Ui_reg_form


class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_reg_form()
        self.ui.setupUi(self)

        self.ui.reg_accept_button.clicked.connect(self.get_register_data)
        self.ui.reg_cancel_button.clicked.connect(self.close)

    def get_register_data(self):
        email = self.ui.reg_email_input.toPlainText()
        username = self.ui.reg_username_input.toPlainText()
        pwd = self.ui.reg_pwd_input.toPlainText()
        qdate = self.ui.reg_date_input.date()

        birth_date = str(date(qdate.year(), qdate.month(), qdate.day()))

        params = {
            "email": email,
            "password": pwd,
            "username": username,
            "birth_date": birth_date,
        }

        res = requests.post("http://127.0.0.1:8000/auth/reg/", data=json.dumps(params))

        if res.status_code == 200:
            QtWidgets.QMessageBox.information(self, "Success", "Registered successfully. You can login!")

        else:
            QtWidgets.QMessageBox.critical(self, "Error", res.text)