"""
In this example, we display the x and y
coordinates of a mouse pointer in a label widget.

6/5/2019
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('Button1',self)
        btn1.move(30,50)

        btn2 = QPushButton('Button2', self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,290,150)

        self.setWindowTitle('Event Sender')

        self.show()
    def buttonClicked(self):
        sender=self.sender()
        self.statusBar().showMessage(sender.text()+'was pressed!')
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
