"""
In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.
so create a button to open trigger the action
"""
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QPushButton,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton("select file",self)
        btn.move(20,20)

        btn.clicked.connect(self.showDialog)

        self.textEdit = QTextEdit()
        self.setGeometry(50,100,50,100)
        #self.setCentralWidget(self.textEdit)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle("file dialog")
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self,"Open file",'/home')
        if fname[0]:
            f=open(fname[0],'r')
        with f:
            data=f.read()
            self.textEdit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())