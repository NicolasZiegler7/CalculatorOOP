from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__result = 0

        button_9 = QPushButton("9")
        button_9.released.connect(self.add_9)
        button_8 = QPushButton("8")
        button_8.released.connect(self.add_8)
        button_7 = QPushButton("7")
        button_7.released.connect(self.add_7)
        button_6 = QPushButton("6")
        button_6.released.connect(self.add_6)
        button_5 = QPushButton("5")
        button_5.released.connect(self.add_5)
        button_4 = QPushButton("4")
        button_4.released.connect(self.add_4)
        button_3 = QPushButton("3")
        button_3.released.connect(self.add_3)
        button_2 = QPushButton("2")
        button_2.released.connect(self.add_2)
        button_1 = QPushButton("1")
        button_1.released.connect(self.add_1)
        button_0 = QPushButton("0")
        button_0.released.connect(self.add_0)

        button_calculate = QPushButton("=")
        button_calculate.released.connect(self.result)
        button_add = QPushButton("+")
        button_add.released.connect(self.result)
        button_sub = QPushButton("-")
        button_sub.released.connect(self.result)
        button_multiply = QPushButton("*")
        button_multiply.released.connect(self.result)
        button_divide = QPushButton("/")
        button_divide.released.connect(self.result)
        button_colon = QPushButton(",")
        button_colon.released.connect(self.result)

        self.__display = QTextBrowser()

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.__display, 1, 1, 1, 4)

        grid_layout.addWidget(button_9, 3, 3)
        grid_layout.addWidget(button_8, 3, 2)
        grid_layout.addWidget(button_7, 3, 1)
        grid_layout.addWidget(button_6, 4, 3)
        grid_layout.addWidget(button_5, 4, 2)
        grid_layout.addWidget(button_4, 4, 1)
        grid_layout.addWidget(button_3, 5, 3)
        grid_layout.addWidget(button_2, 5, 2)
        grid_layout.addWidget(button_1, 5, 1)
        grid_layout.addWidget(button_0, 6, 1)

        grid_layout.addWidget(button_calculate, 6, 3)
        grid_layout.addWidget(button_add, 3, 4)
        grid_layout.addWidget(button_sub, 4, 4)
        grid_layout.addWidget(button_multiply, 5, 4)
        grid_layout.addWidget(button_colon, 6, 2)
        grid_layout.addWidget(button_divide, 6, 4)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def result(self):
        string = str(self.__result)
        string += " + "

        text = self.__display.text()
        string += text
        string += " = "

        self.__result += int(text)
        string += str(self.__result)

        self.__display.append(string)

    @pyqtSlot()
    def add_9(self):
        self.__result += 9
        self.__display.append('9')

    @pyqtSlot()
    def add_8(self):
        self.__result += 8
        self.__display.append('8')

    @pyqtSlot()
    def add_7(self):
        self.__result += 7
        self.__display.append('7')

    @pyqtSlot()
    def add_6(self):
        self.__result += 6
        self.__display.append('6')

    @pyqtSlot()
    def add_5(self):
        self.__result += 5
        self.__display.append('5')

    @pyqtSlot()
    def add_4(self):
        self.__result += 4
        self.__display.append('4')

    @pyqtSlot()
    def add_3(self):
        self.__result += 3
        self.__display.append('3')

    @pyqtSlot()
    def add_2(self):
        self.__result += 2
        self.__display.append('2')

    @pyqtSlot()
    def add_1(self):
        self.__result += 1
        self.__display.append('1')

    @pyqtSlot()
    def add_0(self):
        self.__result += 0
        self.__display.append('0')


