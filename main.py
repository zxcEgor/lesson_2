from PyQt6.QtWidgets import QPushButton, QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
import sys
import random


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(100, 100, 350, 400)
        self.setWindowTitle('Окружности')
        self.do_paint = False
        self.trick_button = QPushButton('Окружности', self)
        self.trick_button.move(140, 20)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.clicked.connect(self.paint)
        self.sp_color = [QColor(255, 255, 0), QColor(255, 0, 255), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255)]

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        color = random.randint(0, 4)
        print(color)
        qp.setBrush(self.sp_color[color])
        x = random.randint(20, 100)
        qp.drawEllipse(90, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    WordTrick = Circle()
    WordTrick.show()
    sys.exit(app.exec())