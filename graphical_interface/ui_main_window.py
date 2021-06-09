from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from game.controller import GameController
from game.states import GameState
from graphical_interface.icon_delegate import IconDelegate
from graphical_interface.table_model import TableModel


def show_win_dialog():
    msg = QMessageBox()
    msg.setWindowTitle("Game Won!")
    msg.setText("You Win!")
    msg.setInformativeText("Congratulations you guess the code.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def show_loose_dialog():
    msg = QMessageBox()
    msg.setWindowTitle("Game Lost!")
    msg.setText("You Lose!")
    msg.setInformativeText("Unfortunately you haven't guess the code in 12 tries.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def show_cheat_dialog(is_computer_cheating):
    msg = QMessageBox()
    msg.setWindowTitle("Computer cheating test")

    if is_computer_cheating:
        msg.setText("Correct!")
        msg.setInformativeText("Oh no! You got me!")
    else:
        msg.setText("Tere fere!")
        msg.setInformativeText("You are wrong! I am not cheating!")

    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def show_dialog():
    msg = QMessageBox()
    msg.setWindowTitle("Window Tittle")
    msg.setText("Header")
    msg.setInformativeText("Some text")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(message_button)
    return_value = msg.exec_()
    print("value of pressed message box button:", return_value)


def message_button(i):
    print("Button pressed is:", i.text())


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = GameController()
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
        self.table_board.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_board.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        delegate = IconDelegate(self.table_board)
        self.table_board.setItemDelegate(delegate)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.table_board.setFont(font)
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
        self.input_code.setObjectName("input_digit")

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
        self.button_check.clicked.connect(self.action_check)

        self.button_cheater = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.button_cheater.setFont(font)
        self.button_cheater.setObjectName("button_cheater")
        self.horizontalLayout.addWidget(self.button_cheater)
        self.button_cheater.clicked.connect(self.action_cheater)

        self.button_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.button_reset.setFont(font)
        self.button_reset.setObjectName("button_reset")
        self.horizontalLayout.addWidget(self.button_reset)
        self.button_reset.clicked.connect(self.action_reset)

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
        self.input_code.setText(_translate("MainWindow", "1111"))
        self.button_check.setText(_translate("MainWindow", "Check"))
        self.button_cheater.setText(_translate("MainWindow", "Cheater"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))

    def action_reset(self):
        self.controller.game_logic.reset_round_count()

    def action_cheater(self):
        show_cheat_dialog(self.controller.check_if_cheating())

    def action_check(self):
        self.controller.game_logic.interact(self.input_code.text())

        new_state = self.controller.game_logic.get_game_state()
        if new_state == GameState.WON:
            show_win_dialog()
            self.controller.game_logic.setup_game()
            self.clear_table()
        elif new_state == GameState.LOST:
            show_loose_dialog()
            self.controller.game_logic.setup_game()
            self.clear_table()
        else:
            self.update_table()

    def update_table(self):
        data = [
            [*self.controller.game_logic.history_game[step], *(self.controller.game_logic.history_result[step])] for
            step in
            range(len(self.controller.game_logic.history_game))
        ]
        data.reverse()
        model = TableModel(data)
        self.table_board.setModel(model)
        for i in range(len(data[0])):
            self.table_board.setColumnWidth(i, 5)

    def clear_table(self):
        data = [[]]
        model = TableModel(data)
        self.table_board.setModel(model)
