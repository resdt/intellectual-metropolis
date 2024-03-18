import sys

import src.main.WindowAction as ws
import src.windows.LoginPage as lp


def main():
    app = lp.QtWidgets.QApplication(sys.argv)
    window = ws.MyWin()

    window.show()
    app.exec_()
