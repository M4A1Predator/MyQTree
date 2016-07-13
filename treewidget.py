from PyQt4 import QtGui, QtCore


class CustomTreeItemWidget(QtGui.QTreeWidgetItem):
    def __init__(self, parent, data):
        QtGui.QTreeWidgetItem.__init__(self, parent)

        # Set display data
        self.image_label = QtGui.QLabel()
        self.image_pixmap = QtGui.QPixmap("ico.png")
        self.image = self.image_pixmap.scaledToHeight(70)
        self.image_label.setPixmap(self.image_pixmap)

        self.setText(1, data[0])
        self.setText(2, data[1])
        self.setText(3, data[2])
        self.setText(4, data[3])
        self.setText(5, data[4])


class CustomTreeWidget(QtGui.QTreeWidget):
    def __init__(self):
        QtGui.QTreeWidget.__init__(self)

        # Setup tree
        self.setColumnCount(6)
        self.setColumnWidth(0, 125)
        self.header = QtGui.QTreeWidgetItem(['image', 'nickname', 'full name', 'position', 'department', 'login name'])
        self.setHeaderItem(self.header)

    def add_items(self, data_list):
        for data in data_list:
            item = CustomTreeItemWidget(self, data)
            image_label = QtGui.QLabel()
            image_pixmap = QtGui.QPixmap("ico.png")
            image = image_pixmap.scaledToHeight(70)
            image_label.setPixmap(image)
            self.setItemWidget(item, 0, image_label)
