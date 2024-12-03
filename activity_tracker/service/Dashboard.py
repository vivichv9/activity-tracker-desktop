import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from activity_tracker.service import ActivityTracker
from activity_tracker.service.AddActivity import AddActivity
from activity_tracker.windows.dashboard_window import Ui_dashboard


class Dashboard(QWidget):
    is_authenticated = Signal()

    def __init__(self):
        super().__init__()
        self.activity = None
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)

        self.ui.add_activity.clicked.connect(self.add_activity)
        self.ui.end_activity.clicked.connect(self.end_activity)

        self.set_data()


    def get_data(self):
        headers = {
            "Authorization": f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        return requests.get('http://127.0.0.1:8000/personal/dashboard/', headers=headers)

    def set_data(self):
        data = self.get_data()

        if data.status_code == 200:
            self.ui.username.setText(data.json()["username"])
            self.ui.points.setText(f"Points: {data.json()['bonuses']}")
            self.ui.list_last_activity.addItems(data.json()["last_activities"])
            self.ui.achievements_list.addItems(data.json()["achievements"])
            self.ui.friends_list.addItems(data.json()["friends"])

        else:
            self.is_authenticated.emit()


    def is_update(self):
        self.ui.list_last_activity.clear()
        self.ui.achievements_list.clear()
        self.ui.friends_list.clear()
        self.set_data()
        self.ui.add_activity.clicked.connect(self.add_activity)
        self.ui.end_activity.clicked.connect(self.end_activity)
        self.update()


    def end_activity(self):
        headers = {
            "Authorization": f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        res = requests.post('http://127.0.0.1:8000/activity/end/', headers=headers)
        if res.status_code == 200:
            self.is_update()
            QtWidgets.QMessageBox.information(None, "Succes!", f"You burned: {res.json()['burned']} cals!")

        else:
            QtWidgets.QMessageBox.critical(None, "Error!", res.text)


    def add_activity(self):
        self.activity = AddActivity()
        self.activity.show()
        self.activity.is_added.connect(self.is_update)
