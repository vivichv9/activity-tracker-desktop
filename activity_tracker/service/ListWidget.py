import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QHBoxLayout,
    QLabel,
)

class FriendRequestItem(QWidget):
    def __init__(self, name, accept_callback, reject_callback):
        super().__init__()

        self.name = name
        layout = QHBoxLayout()

        self.name_label = QLabel(self.name)
        layout.addWidget(self.name_label)

        self.accept_button = QPushButton("Принять")
        self.accept_button.clicked.connect(accept_callback)
        layout.addWidget(self.accept_button)

        self.reject_button = QPushButton("Отклонить")
        self.reject_button.clicked.connect(reject_callback)
        layout.addWidget(self.reject_button)

        self.setLayout(layout)
