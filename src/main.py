import sys

import src.WindowStruct as ws
import src.LoginPage as lp


def main():
    app = lp.QtWidgets.QApplication(sys.argv)
    window = ws.MyWin()

    window.show()
    app.exec_()
