import sys
import os
from PyQt4 import QtGui, QtCore

from MyQTree.treewidget import CustomTreeWidget

DATA_LIST = [('Pred', 'Predator', 'Free style', 'CSGO', 'predator')]

game_data = [
    ('Game', None),
    ('CSGO', 'FPS'),
    ('MOBA', 'Game'),
    ('FPS', 'Game'),
    ('BF', 'FPS'),
    ('COD', 'FPS'),
    ('DOTA2', 'MOBA'),
]


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # init components
        self.tree_widget = None

        self.construct_ui()
        self.create_gui()

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
        self.tree_widget.add_games(game_data)
        # self.tree_widget.add_items(DATA_LIST)
