"""
In this example, we receive data from
a QInputDialog dialog.

"""
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication,QLabel
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn=QPushButton('Dialog', self)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)

        self.label = QLabel("fsdafasdfasdfas",self)
        self.label.move(30,50)

        self.le=QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input Dialog')
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self,'Input Dialog', 'enter your name')
        if ok:
            self.le.setText(str(text))
            self.label.setText("")
        else: self.label.setText("bula bula bula")
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())