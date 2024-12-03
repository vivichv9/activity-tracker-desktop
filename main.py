import sys
from PySide6.QtWidgets import QApplication
from activity_tracker.service.ActivityTracker import ActivityTracker


def main():
    app = QApplication(sys.argv)
    window = ActivityTracker()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()