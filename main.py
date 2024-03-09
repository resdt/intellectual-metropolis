import sys
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
        login_now = self.ui.lineEdit.text()
        password_now = self.ui.lineEdit_2.text()

        for line in login_data:  # Убрал проверку if len(login) > 2
            login, password, numbers = line.split()

            if login_now == login and password_now == password:
                if "admin" in login:
                    login_data.close()

                    # self.ui.label_17.setText(" ")
                    self.ui.lineEdit.setText(" ")
                    self.ui.lineEdit_2.setText(" ")
                    self.openAdmin()

                    break
                else:
                    login_data.close()

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
        self.window = lp.QtWidgets.QMainWindow()
        self.ui = aw.Ui_AdminWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openUser(self):
        self.window2 = lp.QtWidgets.QMainWindow()
        self.ui = uw.Ui_UserWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()


if __name__ == "__main__":
    app = lp.QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    app.exec_()
