import sys
import os
from MyQTree.mainwindow import MainWindow
from PyQt4 import QtGui, QtCore


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
