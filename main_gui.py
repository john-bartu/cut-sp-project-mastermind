import sys

from PyQt5 import QtWidgets

from graphical_interface.ui_main_window import UiMainWindow

if __name__ == "__main__":
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)


    sys.excepthook = except_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()

    sys.exit(app.exec_())
