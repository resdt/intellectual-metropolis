import sys
from main1 import *
from AdminWindow import *
from UserWindow import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.checkUser)

    def checkUser(self):
        f = open("users.txt")
        login_now = self.ui.lineEdit.text()
        password_now = self.ui.lineEdit_2.text()
        for i in f:
            if len(i) > 2:
                login, password, numbers = i.split()
                if login == login_now and password_now == password:
                    if 'admin' in login:
                        # self.ui.label_17.setText(' ')
                        self.ui.lineEdit.setText(' ')
                        self.ui.lineEdit_2.setText(' ')
                        self.openAdmin()
                        f.close()
                        break
                    else:
                        # self.ui.label_17.setText(' ')
                        g = open("temp.txt", "w")
                        g.write(login + ' ' + password + ' ' + numbers)
                        g.close()
                        f.close()
                        self.openUser()
                        break
                print(id, login, password)
        else:
            pass
            # self.ui.label_17.setText("Неправильный логин или пароль")
        f.close()

    def openAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openUser(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()


app = QtWidgets.QApplication(sys.argv)
window = MyWin()
window.show()
app.exec_()
