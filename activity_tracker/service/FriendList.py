import requests
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QTableWidgetItem


from activity_tracker.service import ActivityTracker
from activity_tracker.windows.friend_table import Ui_Form


class FriendList(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        header = {
            'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        res = requests.get('http://127.0.0.1:8000/friend/list/', headers=header)

        res.raise_for_status()

        self.populate_table(res.json()['friends'])


    def populate_table(self, data):
        self.ui.tableWidget.setRowCount(0)

        for row_data in data:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            for column, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_position, column,
                                   QTableWidgetItem(str(value)))

