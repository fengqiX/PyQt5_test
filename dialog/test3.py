"""
In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'),'Open',self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("open new file")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

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