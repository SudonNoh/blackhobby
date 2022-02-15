import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, 
    QPushButton, QLabel, QHBoxLayout, QVBoxLayout,
    QMainWindow, QLineEdit, QDesktopWidget
    )
from PyQt5.QtGui import QIcon


class MainApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        # window Title, Icon
        self.setWindowTitle('BlackHobby')
        self.setWindowIcon(QIcon('./img/logo.png'))
        
        # window 위치 및 크기
        self.center()
        self.width = 300
        self.height = 100
        self.setFixedSize(self.width, self.height)
        
        # 작업 APP
        self.SubApp = SubApp()
        self.setCentralWidget(self.SubApp)
        
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
class SubApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # widgets
        self.label = QLabel('File: ')
        self.lineEdit = QLineEdit()
        self.Add_btn = QPushButton('File Add')
        self.Ok_btn = QPushButton('OK')
        self.Add_btn.setMaximumWidth(100)
        self.Ok_btn.setMaximumWidth(100)
        
        # Add_btn Click
        self.Add_btn.clicked.connect(self.add_open)
        
        # layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)
        hbox.addStretch(1)
        
        hbox2.addStretch(1)
        hbox2.addWidget(self.Add_btn)
        hbox2.addWidget(self.Ok_btn)
        hbox2.addStretch(1)
        
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
    def add_open(self):
        
        FileOpen = QFileDialog.getOpenFileName(self, 'Open File', './')
        self.lineEdit.setText(FileOpen[0])
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = MainApp()
    sys.exit(app.exec_())