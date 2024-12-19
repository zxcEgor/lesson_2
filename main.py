from PyQt6.QtWidgets import QPushButton, QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
import sys
import random
from PyQt6 import uic


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

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
        qp.setBrush(QColor(255, 255, 0))
        x = random.randint(20, 100)
        qp.drawEllipse(90, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    WordTrick = Circle()
    WordTrick.show()
    sys.exit(app.exec())