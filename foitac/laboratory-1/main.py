import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from alphabet import Ui_Alphabet


class Alphabet(QMainWindow, Ui_Alphabet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alphabet()
    ex.show()
    sys.exit(app.exec_())