import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(398, 562)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(398, 562))
        self.setMaximumSize(QtCore.QSize(398, 562))
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_board = QtWidgets.QTableView(self.centralwidget)
        self.table_board.setGeometry(QtCore.QRect(10, 10, 381, 481))
        self.table_board.setObjectName("table_board")
        self.input_code = QtWidgets.QLineEdit(self.centralwidget)
        self.input_code.setGeometry(QtCore.QRect(10, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_code.setFont(font)
        self.input_code.setMaxLength(10)
        self.input_code.setFrame(True)
        self.input_code.setAlignment(QtCore.Qt.AlignCenter)
        self.input_code.setObjectName("input_code")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 500, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_check = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.button_check.setFont(font)
        self.button_check.setObjectName("button_check")
        self.horizontalLayout.addWidget(self.button_check)
        self.button_cheater = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.button_cheater.setFont(font)
        self.button_cheater.setObjectName("button_cheater")
        self.horizontalLayout.addWidget(self.button_cheater)
        self.button_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.button_reset.setFont(font)
        self.button_reset.setObjectName("button_reset")
        self.horizontalLayout.addWidget(self.button_reset)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.input_code.setText(_translate("MainWindow", "2221"))
        self.button_check.setText(_translate("MainWindow", "Sprawdź"))
        self.button_cheater.setText(_translate("MainWindow", "Oszust"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)


    sys.excepthook = except_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()

    sys.exit(app.exec_())
