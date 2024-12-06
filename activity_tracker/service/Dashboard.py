import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidgetItem

from activity_tracker.service import ActivityTracker
from activity_tracker.service.AddActivity import AddActivity
from activity_tracker.service.AddFriend import AddFriend
from activity_tracker.service.FriendList import FriendList
from activity_tracker.windows.dashboard_window import Ui_dashboard
from activity_tracker.service.DeleteFriend import DeleteFriend
from activity_tracker.service.TrainList import TrainList
from activity_tracker.service.ListWidget import FriendRequestItem

class Dashboard(QWidget):
    is_authenticated = Signal()

    def __init__(self):
        super().__init__()
        self.friend_add = None
        self.activity = None
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)

        self.ui.add_activity.clicked.connect(self.add_activity)
        self.ui.end_activity.clicked.connect(self.end_activity)
        self.ui.add_friend.clicked.connect(self.add_friend)
        self.ui.friend_list_button.clicked.connect(self.show_friends)
        self.ui.delete_friend_button.clicked.connect(self.delete_friends)
        self.ui.list_activity.clicked.connect(self.activity_list)

        self.set_data()

    def get_data(self):
        headers = {
            "Authorization": f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        return requests.get('http://127.0.0.1:8000/personal/dashboard/', headers=headers), requests.get('http://127.0.0.1:8000/friend/orders/', headers=headers)

    def set_data(self):
        data, orders = self.get_data()

        if data.status_code == 200:
            self.ui.username.setText(data.json()["username"])
            self.ui.points.setText(str(data.json()['bonuses']))
            self.ui.list_last_activity.addItems(data.json()["last_activities"])
            self.ui.friends_list.addItems(data.json()["friends"])
            self.ui.active_train.setText(data.json()["active_train"])

            for i in orders.json()['orders']:
                self.add_friend_request(i)

        else:
            self.is_authenticated.emit()

    def is_update(self):
        self.ui.list_last_activity.clear()
        self.ui.achievements_list.clear()
        self.ui.friends_list.clear()
        self.set_data()
        self.update()

    def end_activity(self):
        headers = {
            "Authorization": f"bearer {ActivityTracker.ACCESS_TOKEN}"
        }

        res = requests.post('http://127.0.0.1:8000/activity/end/', headers=headers)

        if res.status_code == 200:
            QtWidgets.QMessageBox.information(self, "Succes!", f"You burned: {res.json()['burned']} cals!")
            return self.is_update()
        else:
            QtWidgets.QMessageBox.critical(self, "Error!", res.text)

    def add_activity(self):
        self.activity = AddActivity()
        self.activity.show()
        self.activity.is_added.connect(self.is_update)

    def add_friend(self):
        self.friend_add = AddFriend()
        self.friend_add.show()
        self.friend_add.is_added.connect(self.is_update)

    def show_friends(self):
        self.friends = FriendList()
        self.friends.show()

    def delete_friends(self):
        self.friends_delete = DeleteFriend()
        self.friends_delete.show()

    def activity_list(self):
        self.activities = TrainList()
        self.activities.show()

    def add_friend_request(self, name):
        def accept_request():
            headers = {
                'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}"
            }
            requests.post(f"http://127.0.0.1:8000/friend/confirm/{name}/", headers=headers)
            return self.is_update()

        def reject_request():
            headers = {
                'Authorization': f"bearer {ActivityTracker.ACCESS_TOKEN}"
            }
            requests.post(f"http://127.0.0.1:8000/friend/reject/{name}/", headers=headers)
            return self.is_update()

        request_item = FriendRequestItem(name, accept_request, reject_request)

        list_item = QListWidgetItem(self.ui.achievements_list)
        list_item.setSizeHint(request_item.sizeHint())
        self.ui.achievements_list.addItem(list_item)
        self.ui.achievements_list.setItemWidget(list_item, request_item)
