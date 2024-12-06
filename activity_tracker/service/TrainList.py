import requests

from PySide6.QtWidgets import QWidget, QTableWidgetItem

from activity_tracker.windows.train_table import Ui_Form
from activity_tracker.service import ActivityTracker

class TrainList(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        header = {
            'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        res = requests.get('http://127.0.0.1:8000/activity/list/', headers=header)

        res.raise_for_status()

        self.populate_table(res.json()["activities"])

    def populate_table(self, data):
        self.ui.train_table.setRowCount(0)

        for row_data in data:
            row_position = self.ui.train_table.rowCount()
            self.ui.train_table.insertRow(row_position)

            for column, value in enumerate(row_data):
                self.ui.train_table.setItem(row_position, column,
                                   QTableWidgetItem(str(value)))
