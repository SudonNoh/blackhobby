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
        self.height = 200
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
        self.img_label = QLabel('')
        self.change_btn = QPushButton('Image Update')
        self.update_btn = QPushButton('Image Update')
        self.change_btn.setMaximumWidth(100)
        self.update_btn.setMaximumWidth(100)
        
        self.label = QLabel('File: ')
        self.lineEdit = QLineEdit()
        self.Add_btn = QPushButton('File Add')
        self.Ok_btn = QPushButton('OK')
        self.Add_btn.setMaximumWidth(100)
        self.Ok_btn.setMaximumWidth(100)
        
        # Add_btn Click
        self.Add_btn.clicked.connect(self.add_open)
        self.Ok_btn.clicked.connect(self.add_ok)
        self.change_btn.clicked.connect(self.change_open)
        self.update_btn.clicked.connect(self.img_update)
        
        # layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        
        hbox3.addStretch(1)
        hbox3.addWidget(self.img_label)
        hbox3.addStretch(1)
        
        hbox4.addStretch(1)
        hbox4.addWidget(self.change_btn)
        hbox4.addWidget(self.update_btn)
        hbox4.addStretch(1)
        
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)
        hbox.addStretch(1)
        
        hbox2.addStretch(1)
        hbox2.addWidget(self.Add_btn)
        hbox2.addWidget(self.Ok_btn)
        hbox2.addStretch(1)
        
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
    def change_open(self):
        
        urls, _ = QFileDialog.getOpenFileNames(
            caption='Select one or more files to change',
            directory='./',
            filter="image(*.jpg *.jpeg *.png)"
        )
        self.img_label.setText("Ready to Change Image.")
        # 여기 할 차례 urls 를 목록으로 보여주기 or get해서 img_update로 보내기
        
    def img_update(self):
        
        print(self.FileOpen[0])
        
    def add_open(self):
        
        FileOpen = QFileDialog.getOpenFileName(self, 'Open File', './')
        self.lineEdit.setText(FileOpen[0])
        
    def add_ok(self):
        
        print(self.lineEdit.text())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = MainApp()
    sys.exit(app.exec_())