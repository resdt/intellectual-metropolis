import os

import src.main.PATH as path
import src.windows.LoginPage as lp
import src.windows.AdminWindow as aw
import src.windows.UserWindow as uw


TMP_FOLD = path.TMP_FOLD

USER_DATA_FILE_PATH = path.USER_DATA_FILE_PATH
TMP_FILE_PATH = path.TMP_FILE_PATH


class MyWin(lp.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        lp.QtWidgets.QWidget.__init__(self, parent)

        self.ui = lp.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.checkUser)

    def checkUser(self):
        login_data = open(USER_DATA_FILE_PATH)
        cur_log = self.ui.lineEdit.text()
        cur_pwd = self.ui.lineEdit_2.text()

        for line in login_data:  # Убрал проверку if len(login) > 2
            login, password, numbers = line.split()

            if cur_log == login and cur_pwd == password:
                login_data.close()

                if "admin" in login:
                    # self.ui.label_17.setText(" ")
                    self.ui.lineEdit.setText(" ")
                    self.ui.lineEdit_2.setText(" ")
                    self.openAdmin()
                else:
                    os.makedirs(TMP_FOLD, exist_ok=True)

                    with open(TMP_FILE_PATH, "w") as temp_file:
                        temp_file.write(f"{login} {password} {numbers}")

                    # self.ui.label_17.setText(" ")
                    self.openUser()

                break
        else:
            pass
            # self.ui.label_17.setText("Неправильный логин или пароль")

        login_data.close()

    def openAdmin(self):
        self.adminWindow = lp.QtWidgets.QMainWindow()
        self.ui = aw.Ui_AdminWindow()

        self.ui.setupUi(self.adminWindow)
        self.adminWindow.show()

    def openUser(self):
        self.userWindow = lp.QtWidgets.QMainWindow()
        self.ui = uw.Ui_UserWindow()

        self.ui.setupUi(self.userWindow)
        self.userWindow.show()
