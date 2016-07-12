from PyQt4 import QtGui, QtCore


class MyTree(QtGui.QTreeWidget):
    def __init__(self):
        QtGui.QTreeWidget.__init__(self)
        self.setColumnCount(4)
        self.setColumnWidth(0, 300 + 100)
        self.header = QtGui.QTreeWidgetItem(['logo', 'game', 'publisher', 'genre'])
        self.setHeaderItem(self.header)


class MyTreeItem(QtGui.QTreeWidgetItem):
    def __init__(self, parent, data):
        # QtGui.QTreeWidgetItem.__init__(self, parent)
        super(MyTreeItem, self).__init__(parent)

        self.label = QtGui.QLabel()
        # self.pixmap = QtGui.QPixmap('C:\\Users\\PredatorPy\\Pictures\\ico.png')
        self.pixmap = QtGui.QPixmap('ico.png')
        self.label.setPixmap(self.pixmap)

        self.treeWidget().setItemWidget(self, 0, self.label)

        self.setText(1, data[0])
        self.setText(2, data[1])
        self.setText(3, data[2])


# source : http://blog.asimation.com/37/
