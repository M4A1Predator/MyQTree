import sys
import os
from PyQt4 import QtGui, QtCore

from MyQTree.treewidget import CustomTreeWidget

DATA_LIST = [('Pred', 'Predator', 'Free style', 'CSGO', 'predator')]


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # init components
        self.tree_widget = None

        self.construct_ui()
        self.create_gui()

        self.draw_tree()

        # Set window
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.tree_widget)

        self.setWindowTitle("QTree")
        self.setGeometry(100, 100, 1290, 800)
        self.setCentralWidget(self.tree_widget)

    def construct_ui(self):
        pass

    def create_gui(self):
        self.tree_widget = CustomTreeWidget()

    def draw_tree(self):
        self.tree_widget.add_items(DATA_LIST)
