import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
from image_converter import Ui_ImageConverter
import itertools
import re


class ImageToGrayscale(QMainWindow, Ui_ImageConverter):
    image_txt = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selectButton.clicked.connect(self.select_image)
        self.saveButton.clicked.connect(self.save_image)
        self.unpackButton.clicked.connect(self.unpacked)

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        self.infoLabel.setAlignment(Qt.AlignCenter)

    def select_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Изображения (*.png *.jpg *.jpeg *.bmp *.gif);;Все файлы (*)",
                                                  options=options)

        if fileName:
            try:
                self.convert_grayscale_display(fileName)
            except Exception as e:
                self.infoLabel.setText(f"Ошибка обработки изображения: {str(e)}")

    def convert_grayscale_display(self, image_path):
        try:
            img = Image.open(image_path).convert('L')

            a_img = np.where(np.array(img) > 127, 255, 0)

            fragments = []
            for row in a_img:
                for value, group in itertools.groupby(row):
                    count = sum(1 for _ in group)
                    fragments.append(str(count) + ("b" if value == 0 else "w"))

            self.image_txt = "".join(fragments)

            arr_img = np.where(np.array(img) > 127, 255, 0).astype(np.uint8)
            height, width = arr_img.shape

            self.image_txt += f"\n{width} {height}"

            q_img = QImage(arr_img.data, width, height, width, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_img)

            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

            self.infoLabel.setText(f"Изображение загружено и преобразовано в оттенки белочёрного. Размеры: {width}x{height}")

            self.saveButton.setEnabled(True)

        except FileNotFoundError:
            self.infoLabel.setText("Файл не найден.")
        except Exception as e:
            self.infoLabel.setText(f"Ошибка: {str(e)}")

    def save_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                   "Изображение (*.txt);;Все файлы (*)",
                                                   options=options)
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(self.image_txt)
                QMessageBox.information(self, "Сохранение", f"Файл '{file_name}' успешно сохранен.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")

    def unpacked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Изображения (*.txt);;Все файлы (*)",
                                                  options=options)

        text = []

        if fileName:
            try:
                with open(fileName, 'r') as file:
                    text = file.readlines()
                QMessageBox.information(self, "Открыт", "Файл успешно открыт")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")
                return

        width, height = text[1].split()
        image_txt = text[0][:-1]

        decoded_image = np.zeros((int(height), int(width)), dtype=np.uint8)

        current_row = 0
        current_col = 0

        fragments = re.findall(r'(\d+)([bw])', image_txt)  # Используем регулярное выражение для парсинга

        if not fragments:
            print("Ошибка: Неверный формат image_txt.")
            return None

        try:
            for count, color in fragments:
                count = int(count)
                color_value = 0 if color == 'b' else 255

                for _ in range(count):
                    decoded_image[current_row, current_col] = color_value
                    current_col += 1

                    if current_col == width:
                        current_col = 0
                        current_row += 1

                    if current_row == height:
                        break

        except Exception as e:
            print(f"Ошибка при декодировании: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageToGrayscale()
    ex.show()
    sys.exit(app.exec_())