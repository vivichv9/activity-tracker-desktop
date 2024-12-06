import json
from PySide6.QtWidgets import QWidget
from PySide6 import QtWidgets
import requests
from activity_tracker.windows.delete_friend import Ui_Dialog
from activity_tracker.service import ActivityTracker

class DeleteFriend(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_friend.clicked.connect(self.delete)

    def delete(self):
        username = self.ui.textEdit.toPlainText()

        header = {
               'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}"
		}

        data = {
               'username': username
		}

        res = requests.post('http://127.0.0.1:8000/friend/delete/', headers=header, data=json.dumps(data))

        if res.status_code == 200:
            QtWidgets.QMessageBox.information(self, "Sucess!", "Friend deleted!")
            self.close()

        else:
            QtWidgets.QMessageBox.critical(self, "Error!", res.text)
            self.close()