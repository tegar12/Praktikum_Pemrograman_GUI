import sys
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from pendaftaran import*
class MainForm (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Tugas Pemograman GUI')
        self.tul = QLabel('Username')
        self.ls = QLabel('Password')
        self.kos = QLineEdit()
        self.pa = QLineEdit()
        self.pa.setEchoMode(QLineEdit.Password)
        self.button =QPushButton('Login')
        self.button1 =QPushButton('Clear')
        btx =QGridLayout()
        btx.addWidget(self.tul)
        btx.addWidget(self.kos, 0,1,1,2)
        btx.addWidget(self.ls)
        btx.addWidget(self.pa, 1,1,1,2)
        btx.addWidget(self.button, 2,1)
        btx.addWidget(self.button1, 2,2)
        self.setLayout(btx)

        self.button.clicked.connect(self.buttonClick)
        self.button1.clicked.connect(self.buttonClick1)

    def buttonClick(self):
        user = self.kos.text()
        pw = self.pa.text()

        if not user or not pw :
            QMessageBox.information(self,'Perhatian','Username atau password tidak boleh kosong')
        else:
            if user == '17104031' and pw =='123456789':
                self.form = pendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self,'Perhatian','Username atau password Salah')

    def buttonClick1 (self):
            self.kos.clear()
            self.pa.clear()
if __name__ =='__main__':
        a =QApplication(sys.argv)
        form =MainForm()
        form.show()

        a.exec_()
