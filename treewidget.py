from PyQt4 import QtGui, QtCore


class CustomTreeItemWidget(QtGui.QTreeWidgetItem):
    def __init__(self, parent, data):
        QtGui.QTreeWidgetItem.__init__(self, parent)

        # Set display data
        self.image_label = QtGui.QLabel()
        self.image_pixmap = QtGui.QPixmap("ico.png")
        self.image = self.image_pixmap.scaledToHeight(70)
        self.image_label.setPixmap(self.image_pixmap)

        # self.setText(2, data[0])
        # self.setText(3, data[1])
        # self.setText(4, data[2])
        # self.setText(5, data[3])
        # self.setText(6, data[4])


class CustomTreeWidget(QtGui.QTreeWidget):
    def __init__(self):
        QtGui.QTreeWidget.__init__(self)

        # Setup tree
        self.setColumnCount(6)
        self.setColumnWidth(1, 125)
        self.header = QtGui.QTreeWidgetItem(['', 'image', 'nickname', 'full name', 'position', 'department', 'login name'])
        self.setHeaderItem(self.header)

        # Setup menu
        self.r_menu = None

        # self.itemActivated.connect(self.cb)
        self.itemClicked.connect(self.cb)

    def add_items(self, data_list):
        for data in data_list:
            item = CustomTreeItemWidget(self, data)
            image_label = QtGui.QLabel()
            image_pixmap = QtGui.QPixmap("ico.png")
            image = image_pixmap.scaledToHeight(70)
            image_label.setPixmap(image)
            self.setItemWidget(item, 1, image_label)

    def add_games(self, game_data):
        # Clear first
        self.clear()

        parent_nodes = []
        remove_list = []
        parent_texts = []
        add_list = []
        add_nodes = []

        # Add root node
        # for g in game_data:
        #     if not g[1]:
        #         # Add tree item
        #         node = GameItemWidget(g)
        #         self.addTopLevelItem(node)
        #         self.setItemExpanded(node, True)
        #
        #         # Add image add the first col
        #         image_label = QtGui.QLabel()
        #         image_pixmap = QtGui.QPixmap("ico.png")
        #         image = image_pixmap.scaledToHeight(70)
        #         image_label.setPixmap(image)
        #         self.setItemWidget(node, 0, image_label)
        #         self.setItemWidget(node, 2, node.label)
        #         # self.connect(self, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.cb)
        #
        #         # Add list
        #         parent_nodes.append(node)
        #         remove_list.append(g)
        #         parent_texts.append(g[0])

        # all parent
        all_parents = []
        for g in game_data:
            all_parents.append(g[0])

        for g in game_data:
            if not g[1] in all_parents:
                # Add tree item
                node = GameItemWidget(g)
                self.addTopLevelItem(node)
                self.setItemExpanded(node, True)

                # Add image add the first col
                image_label = QtGui.QLabel()
                image_pixmap = QtGui.QPixmap("ico.png")
                image = image_pixmap.scaledToHeight(70)
                image_label.setPixmap(image)
                self.setItemWidget(node, 1, image_label)
                # self.setItemWidget(node, 2, node.label)
                # self.connect(self, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.cb)

                # Add list
                parent_nodes.append(node)
                remove_list.append(g)
                parent_texts.append(g[0])

        while game_data:
            for index, g in enumerate(game_data):
                if g[1] in parent_texts:
                    add_list.append(g)
            parent_texts = []

            for p in parent_nodes:
                for g in add_list:
                    if g[1] == p.game_data[0]:
                        # Add tree item
                        node = GameItemWidget(g, parent=p)
                        self.addTopLevelItem(node)

                        # Add image add the first col
                        image_label = QtGui.QLabel()
                        image_pixmap = QtGui.QPixmap("ico.png")
                        image = image_pixmap.scaledToHeight(70)
                        image_label.setPixmap(image)
                        self.setItemWidget(node, 1, image_label)

                        add_nodes.append(node)
                        parent_texts.append(g[0])
                        remove_list.append(g)

            # Clear list
            parent_nodes = add_nodes
            add_nodes = []

            # Remove
            for rm in remove_list:
                game_data.remove(rm)
                remove_list = []

    def contextMenuEvent(self, event):
        self.r_menu = QtGui.QMenu()
        expand_menu = QtGui.QAction('Expand', self)
        expand_menu.triggered.connect(self.expand_cb)
        self.r_menu.addAction(expand_menu)
        # add other required actions
        self.r_menu.popup(QtGui.QCursor.pos())

    def cb(self, e):
        item = self.selectedItems()
        try:
            print(item[0].game_data, 'Child of', item[0].parent().game_data)
            parent_item = item[0].parent()
            if parent_item:
                # set color
                parent_item.setBackground(0, QtGui.QBrush(QtCore.Qt.cyan))
                parent_item.setBackground(1, QtGui.QBrush(QtCore.Qt.cyan))
                parent_item.setBackground(2, QtGui.QBrush(QtCore.Qt.cyan))
        except AttributeError:
            pass

    def expand_cb(self, event):
        print(event)


class GameItemWidget(QtGui.QTreeWidgetItem):
    def __init__(self, data, parent=None):
        QtGui.QTreeWidgetItem.__init__(self, parent)

        self.game_data = data

        # Set display data
        self.image_label = QtGui.QLabel()
        self.image_pixmap = QtGui.QPixmap("ico.png")
        self.image = self.image_pixmap.scaledToHeight(70)
        self.image_label.setPixmap(self.image_pixmap)

        self.label = QtGui.QLabel()
        self.label.setText(data[0])
        self.label.mousePressEvent = lambda e: self.m_cb(e)

        self.setText(2, data[0])

    def m_cb(self, event):
        print("Mouse click item", event.__dict__)


# https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable
