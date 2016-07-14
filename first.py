import sys

from PyQt4 import QtGui

from MyQTree.mytree import MyTree, MyTreeItem


GAME_DATA = [("CSGO", "Valve", "FPS"), ("COD", "Activision", "FPS"), ("DOTA2", "Valve", "Moba")]

game_data = [
    ('Game', None),
    ('CSGO', 'FPS'),
    ('MOBA', 'Game'),
    ('FPS', 'Game'),
    ('BF', 'FPS'),
    ('COD', 'FPS'),
    ('DOTA2', 'MOBA'),
]


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
        self.hlayout = QtGui.QHBoxLayout()
        searchInput = QtGui.QLineEdit()
        searchInput.setFixedHeight(20)
        ok_button = QtGui.QPushButton("OK")
        # self.box_layout.addWidget(ok_button)
        # self.box_layout.addWidget(self.tree)
        self.hlayout.addWidget(searchInput)
        self.hlayout.addWidget(ok_button)
        # self.box_layout.addWidget(self.hlayout)
        self.box_layout.addLayout(self.hlayout)
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

    def get_node(self):
        pass

    def add_game_data(self, game_data):
        parent_nodes = []
        remove_list = []
        parent_texts = []
        add_list = []
        add_nodes = []

        # Add root node
        for g in game_data:
            if not g[1]:
                node = MyTreeItem(self.tree, (g[0], g[0], g[0]))
                node.setExpanded(True)
                parent_nodes.append(node)
                remove_list.append(g)
                parent_texts.append(g[0])

        # Remove parents level 1
        for rm in remove_list:
            print('remove ', rm[0])
            game_data.remove(rm)
        remove_list = []

        c = 0
        while game_data and c < 5:  # c < 5 prevent infinite loop if mistake
            print('data is ', game_data)
            for index, g in enumerate(game_data):
                if g[1] in parent_texts:
                    print(g[0], ' is child of ', parent_texts)
                    add_list.append(g)

            parent_texts = []

            print(len(parent_nodes), len(add_list))

            for p in parent_nodes:
                print("Enter loop")
                for g in add_list:
                    if g[1] == p.game_name:
                        # node = self.get_node(g[0])
                        # self.tree.add_node(node, parent=p)
                        print("Add to game ", type(p))
                        node = MyTreeItem(p, (g[0], g[0], g[0]))
                        add_nodes.append(node)
                        parent_texts.append(g[0])
                        remove_list.append(g)

            # Clear list
            parent_nodes = add_nodes
            add_nodes = []
            print(parent_nodes)

            # Remove
            for rm in remove_list:
                game_data.remove(rm)
                remove_list = []

            c += 1


def main():
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()

    #window.add_item(GAME_DATA)
    window.add_game_data(game_data)

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

