from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    header_labels = ['', '', '', '', 'C', 'P']

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def headerData(self, section: int, orientation, role=Qt.DisplayRole):

        if role == Qt.DecorationRole and orientation == Qt.Horizontal:
            if section == 4:
                return QtGui.QImage(f"icons/ok.png")
            if section == 5:
                return QtGui.QImage(f"icons/pos.png")
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]

    def data(self, index, role):

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.DecorationRole:
            if index.column() <= 3:
                return QtGui.QImage(f"icons/{self._data[index.row()][index.column()]}.png")

        if role == Qt.DisplayRole:
            if index.column() > 3:
                return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def flags(self, index):
        return Qt.ItemIsEnabled
