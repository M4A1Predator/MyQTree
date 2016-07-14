from PyQt4 import QtGui, QtCore


class MyTree(QtGui.QTreeWidget):
    def __init__(self):
        QtGui.QTreeWidget.__init__(self)
        self.setColumnCount(4)
        self.setColumnWidth(0, 300 + 100)
        self.header = QtGui.QTreeWidgetItem(['logo', 'game', 'publisher', 'genre'])
        self.setHeaderItem(self.header)

        i = QtGui.QTreeWidgetItem(['WB'])
        self.addTopLevelItem(i)
        self.addTopLevelItem(QtGui.QTreeWidgetItem(i, ['TBD']))

    def add_games(self, game_data):
        print("Add item")

        parent_nodes = []
        remove_list = []
        parent_texts = []
        add_list = []
        add_nodes = []

        # Add root node
        for g in game_data:
            print(g)
            if not g[1]:
                node = MyTreeItem(None, (g[0], g[0], g[0]))
                node.setExpanded(True)
                self.addTopLevelItem(node)
                parent_nodes.append(node)
                remove_list.append(g)
                parent_texts.append(g[0])


class MyTreeItem(QtGui.QTreeWidgetItem):
    def __init__(self, parent, data):
        # QtGui.QTreeWidgetItem.__init__(self, parent)
        super(MyTreeItem, self).__init__(parent)
        self.game_name = data[0]

        #   Set up tree
        self.label = QtGui.QLabel()
        self.pixmap = QtGui.QPixmap('ico.png')
        self.pixmap = self.pixmap.scaledToHeight(70)
        self.label.setPixmap(self.pixmap)

        self.treeWidget().setItemWidget(self, 0, self.label)

        self.setText(1, data[0])
        self.setText(2, data[1])
        self.setText(3, data[2])


# source : http://blog.asimation.com/37/
