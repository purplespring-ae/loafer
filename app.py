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
    wrapper = QWidget()

    formula_input = QFormLayout()
    # Hydration
    lbl_hyd = QLabel()
    lbl_hyd.setText("Hydration:")
    txt_hyd = QLineEdit()
    formula_input.addWidget(lbl_hyd)
    formula_input.addWidget(txt_hyd)
    # Levain
    lbl_lev = QLabel()
    lbl_lev.setText("Levain:")
    txt_lev = QLineEdit()
    formula_input.addWidget(lbl_lev)
    formula_input.addWidget(txt_lev)
    # Salt
    lbl_sal = QLabel()
    lbl_sal.setText("Salt:")
    txt_sal = QLineEdit()
    formula_input.addWidget(lbl_sal)
    formula_input.addWidget(txt_sal)

    wrapper.setLayout(formula_input)

    wrapper.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    my_formula = Formula("Low Hydration Basic", 0.65, 0.2, 0.02)
    my_formula.math(350)
    window()
