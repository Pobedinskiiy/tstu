import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from alphabet import Ui_Alphabet
from math import ceil, log2


class Alphabet(QMainWindow, Ui_Alphabet):
    path: list = ["rus", "en"]

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.addAlphabetButton.clicked.connect(self.add_alphabet)
        self.analyzeMessageButton.clicked.connect(self.analyze_message)

    def add_alphabet(self) -> None:
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Алфавит (*.txt);;Все файлы (*)",
                                                  options=options)
        self.languageComboBox.addItem(f"{fileName}")

    def analyze_message(self) -> None:
        text_message = self.inTextEdit.toPlainText()
        path = self.languageComboBox.currentText()
        alphabet_power, alphabet = self.read_alphabet(path)
        size = len(self.filter_string(text_message, alphabet)) * self.calc_size_symbol(alphabet_power)
        self.outTextEdit.setText(f"Вес полезной информации: {size}")

    @staticmethod
    def calc_size_symbol(size: int) -> int:
        return ceil(log2(size))

    @staticmethod
    def filter_string(string1: str, string2: str) -> str:
        return "".join([char for char in string1 if char in string2])

    @staticmethod
    def read_alphabet(path: str) -> (int, str):
        file = open(path, "r")
        content = file.read()
        file.close()
        return len(content), content


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alphabet()
    ex.show()
    sys.exit(app.exec_())