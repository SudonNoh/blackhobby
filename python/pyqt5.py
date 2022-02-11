import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class exe_func(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # window Title, Icon
        self.setWindowTitle('BlackHobby')
        self.setWindowIcon(QIcon('./img/logo.png'))
        
        # window 위치 및 크기
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = exe_func()
    sys.exit(app.exec_())