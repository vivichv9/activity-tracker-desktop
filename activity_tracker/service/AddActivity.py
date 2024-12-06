import json

import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMainWindow

from activity_tracker.windows.add_activity import Ui_add_activity_form
from activity_tracker.service import ActivityTracker

class AddActivity(QWidget):
    is_added = Signal()

    def __init__(self):
       super().__init__()
       self.ui = Ui_add_activity_form()
       self.ui.setupUi(self)
       self.ui.add_activity_button.clicked.connect(self.add_activity)


    def add_activity(self):
        act_type = self.ui.comboBox.currentText()

        headers = {
            "Authorization": f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        print(act_type)
        data = {
            "activity_type": str(act_type),
        }

        res = requests.post('http://127.0.0.1:8000/activity/start/', headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            QtWidgets.QMessageBox.information(self, "Success!", f"Activity has been added. Start time: {res.json()['start_time']}")
            self.close()
            self.is_added.emit()
            self.destroy()

        else:
            QtWidgets.QMessageBox.critical(self, "Error!", res.text)