import src.LoginPage as lp
import src.AdminWindow as aw
import src.UserWindow as uw


class MyWin(lp.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        lp.QtWidgets.QWidget.__init__(self, parent)

        self.ui = lp.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.checkUser)

    def checkUser(self):
        login_data = open("lib/user-data.txt")
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
                    with open("tmp/temp.txt", "w") as temp_file:
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
