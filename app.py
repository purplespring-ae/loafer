import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Formula():
    def __init__(self, lbl, hyd, lev, sal):
        self.lbl = lbl
        # self.flr = flr # how to take different ratios of multiple flours?
        self.hyd = hyd  # hydration percentage as float
        self.lev = lev  # levain percentage as float
        self.sal = sal  # salt percentage as float

    def math(self, flr):
        water = self.hyd * flr
        starter = self.lev * flr
        salt = self.sal * flr
        loaf_wgt = flr + water + starter + salt

        print(f"Your {self.lbl} recipe:")
        print(f"Flour: {flr}g")
        print(f"Water: {water}g")
        print(f"Salt: {salt}g")
        print(f"Total loaf weight: {loaf_wgt}g")


def window():
    app = QApplication(sys.argv)
    wrapper = QBoxLayout()

    wrapper.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    my_formula = Formula("Low Hydration Basic", 0.65, 0.2, 0.02)
    my_formula.math(350)
    # window()
