import sys

from Desain_GUI import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class MainForm(QDialog):
    def __int__ (self,parent = None) :
        QDialog.__int__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.hallo.clicked.connect(self.halloClicked)

    def halloClicked(self):
        QMessageBox.information(self, 'Demo Qt Designer',
        'Hallo %s, apa kabar?' % self.ui.NameEdit.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
