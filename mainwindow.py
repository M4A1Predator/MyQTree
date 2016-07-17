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


class MainLayout(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # Init attributes
        self.game_data = game_data[:len(game_data)]

        # Set widget
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)

        self.tree_widget = None
        self.search = QtGui.QLineEdit()

        # Construct gui
        self.create_gui()
        self.setup_search()

        # Add widget
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.tree_widget)

    def create_gui(self):
        self.tree_widget = CustomTreeWidget()
        self.tree_widget.add_games(self.game_data)
        # self.tree_widget.add_items(DATA_LIST)

    def setup_search(self):
        self.search.textEdited.connect(self.search_cb)

    # Back end region
    @staticmethod
    def search_game(game_name):
        results = []
        for g in game_data:
            if g[0].lower().find(game_name.lower()) != -1:
                results.append(g)

        return results

    # Cb region
    def search_cb(self, event):
        text = self.search.text()
        new_game_data = MainLayout.search_game(text)
        self.tree_widget.add_games(new_game_data)


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # init components

        # Set up layout
        self.main_widget = MainLayout()

        # Set window
        self.setWindowTitle("QTree")
        self.setGeometry(100, 100, 1290, 800)
        self.setCentralWidget(self.main_widget)

    def construct_ui(self):
        pass
