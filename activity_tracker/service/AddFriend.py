import json

import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from activity_tracker.service import ActivityTracker
from activity_tracker.windows.add_friend import Ui_add_friend_form


class AddFriend(QWidget):
    is_added = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_add_friend_form()
        self.ui.setupUi(self)
        self.ui.add_friend.clicked.connect(self.add_friend)

    def add_friend(self):
        username = self.ui.textEdit.toPlainText()

        headers = {
            'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}",
        }

        data = {
            'username': username
        }

        request = requests.post('http://127.0.0.1:8000/friend/add/', headers=headers, data=json.dumps(data))

        if request.status_code == 200:
            QtWidgets.QMessageBox.information(self, "Friend added", "Friend added successfully!")
            self.is_added.emit()
            self.close()

        else:
            QtWidgets.QMessageBox.critical(self, "Error", request.text)