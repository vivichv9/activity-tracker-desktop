from PySide6.QtWidgets import QMainWindow

from activity_tracker.service.Dashboard import Dashboard
from activity_tracker.service.LoginForm import LoginForm
from activity_tracker.service.RegisterForm import RegisterForm
from activity_tracker.windows.dashboard_window import Ui_dashboard
from activity_tracker.windows.main_window import Ui_MainWindow


ACCESS_TOKEN = ''
REFRESH_TOKEN = ''
TOKEN_TYPE = ''


class ActivityTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dashboard = None
        self.register_form = None
        self.login_form = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.reg_button.clicked.connect(self.open_reg_form)
        self.ui.login_button.clicked.connect(self.open_login_form)

    def open_reg_form(self):
        self.register_form = RegisterForm()
        self.register_form.show()


    def open_login_form(self):
        self.login_form = LoginForm(self)
        self.login_form.show()
        self.login_form.login_success.connect(self.on_login_success)


    def on_login_success(self):
        self.hide()
        self.dashboard = Dashboard()
        self.dashboard.show()
        self.dashboard.is_authenticated.connect(self.show)