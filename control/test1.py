"""
In this example, a QCheckBox widget
is used to toggle the title of a window.
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20,20)
        #cb.toggle()
        cb.stateChanged.connect(self.changeState)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeState(self,state):
        if state == Qt.Checked:
            self.setWindowTitle("yesysysys")
        else:
            self.setWindowTitle("nonononono")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
