from PySide6 import QtWidgets
import requests

class Requester:
    def __init__(self, base_url = "http://127.0.0.1:8000/"):
        self.base_url = base_url


    def register_request(self, params):
        request = requests.post(self.base_url + "auth/register", params=params)

        if request.status_code == 200:
            QtWidgets.QMessageBox.information(None, "Success", "Registered successfully. You can login!")

        if request.status_code == 400:
            QtWidgets.QMessageBox.information(None, "Error", request.text)
            return False


