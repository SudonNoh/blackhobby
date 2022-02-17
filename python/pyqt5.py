import time
import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QPushButton, 
    QLabel, 
    QHBoxLayout, 
    QVBoxLayout,
    QMainWindow, 
    QLineEdit, 
    QDesktopWidget, 
    QMessageBox,
    )
from PyQt5.QtGui import QIcon
import file_setting as fs

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
        self.fs = fs.file_setting()
        
    def initUI(self):
        # widgets
        self.img_label = QLabel('Input URL for updating img')
        self.img_label2 = QLabel('Files: ')
        self.img_lineEdit = QLineEdit()
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
        
        # widget's style
        self.img_label.setStyleSheet(
            "color: #0d3300;"
            "padding: 5px;"
            "font-weight: bold;"
            "background-color: #53ff1a;"
            )
        
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
        hbox5 = QHBoxLayout()
        
        hbox5.addStretch(1)
        hbox5.addWidget(self.img_label2)
        hbox5.addWidget(self.img_lineEdit)
        hbox5.addStretch(1)
        
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
        vbox.addLayout(hbox5)
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
        if not urls:
            pass
        else:
            urls_text = ', '.join(urls)
            self.img_lineEdit.setText(urls_text)
            self.img_lineEdit.setReadOnly(True)
            self.img_label.setText("Ready to Change Image.")
            self.img_label.setStyleSheet(
                "color: #332200;"
                "padding: 5px;"
                "font-weight: bold;"
                "background-color: #ffaa00;"
                )
        
    def img_update(self):
        # img 파일 주소를 url로 불러와서 list로 변경
        if not self.img_lineEdit.text():
            QMessageBox.information(self, 'Error', 'Please input correct Img url.')
            pass
        else:
            update_imgs = self.img_lineEdit.text().split(', ')
        
            # 'update_img'는 img의 주소
            # progressbar 입력 예정
            count = 0
            for i in update_imgs:
                self.fs.img_change(i, 'image')
                count += 1
                pbar_value = int(count/len(update_imgs)*100)

            # img 파일 주소를 초기화
            self.img_lineEdit.setText('')
            # ReadOnly를 True로 설정했던 lineEdit을 False로 설정
            self.img_lineEdit.setReadOnly(False)
            self.img_label.setText("Input URL for updating img.")
            self.img_label.setStyleSheet(
                "color: #0d3300;"
                "padding: 5px;"
                "font-weight: bold;"
                "background-color: #53ff1a;"
                )
            
            # 업데이트 완료 표시
            QMessageBox.information(self, 'Update', 'Image Updated !')
        
    def add_open(self):
        
        FileOpen = QFileDialog.getOpenFileName(self, 'Open File', './')
        self.lineEdit.setText(FileOpen[0])
        self.img_lineEdit.setReadOnly(True)
        
    def add_ok(self):
        
        print(self.lineEdit.text())

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = MainApp()
    sys.exit(app.exec_())