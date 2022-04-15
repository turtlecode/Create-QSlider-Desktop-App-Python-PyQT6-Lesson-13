from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Turtle Code")

        self.label = QLabel(self)
        self.label.move(130, 100)

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setGeometry(50, 50, 200, 50)
        slider.setMinimum(0)
        slider.setMaximum(20)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setTickInterval(1)
        slider.valueChanged.connect(self.display)

    def display(self):
        self.label.setText("Value: " + str(self.sender().value()))
        self.label.adjustSize()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())