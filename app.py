import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    title = QWidget()
    title_label = QLabel(title)
    title_label.setText("Loaf Life")

    title.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    window()

