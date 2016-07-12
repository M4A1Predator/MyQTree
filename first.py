import sys

from PyQt4 import QtGui

from MyQTree.mytree import MyTree, MyTreeItem


GAME_DATA = [("CSGO", "Valve", "FPS"), ("COD", "Activision", "FPS"), ("DOTA2", "Valve", "Moba")]


class MyWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Set containers
        self.box_layout = QtGui.QVBoxLayout()

        # init components
        self.tree = None
        self.root_item = None
        self.competitive_game_item = None
        self.fps_root = None
        self.moba_root = None

        # create gui
        self.create_gui()

        # add gui
        ok_button = QtGui.QPushButton("OK")
        self.box_layout.addWidget(ok_button)
        self.box_layout.addWidget(self.tree)

        # Show ui
        self.setLayout(self.box_layout)
        self.setWindowTitle("My QT Tree")
        self.setGeometry(100, 100, 1290, 800)

    def create_gui(self):
        self.tree = MyTree()
        self.setup_tree()

    def setup_tree(self):
        self.root_item = QtGui.QTreeWidgetItem(self.tree, ["STEAM GAMES", "-", "-"])
        self.root_item.setExpanded(True)
        self.competitive_game_item = QtGui.QTreeWidgetItem(self.root_item, ["Competitive", "-", "-"])
        self.fps_root = QtGui.QTreeWidgetItem(self.root_item, ["FPS", "", ""])
        self.fps_root.setExpanded(True)
        self.moba_root = QtGui.QTreeWidgetItem(self.root_item, ["MOBA", "", ""])
        self.moba_root .setExpanded(True)

    def add_item(self, items):
        for game in GAME_DATA:
            parent = self.root_item
            if game[2].lower() == 'fps':
                parent = self.fps_root
            elif game[2].lower() == 'moba':
                parent = self.moba_root
            # tree_item = QtGui.QTreeWidgetItem(parent, ['', game[0], game[1], game[2]])
            tree_item = MyTreeItem(parent, game)


def main():
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    window.add_item(GAME_DATA)

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

