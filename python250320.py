'''
#PyQt5 images
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        label  = QLabel(self)
        label.setGeometry(0,0,250,250)
        #label.setText=("你好，世界！")

        pixmap = QPixmap("profile_pic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width())//2,
                          (slf.height() - label.height())//2,
                          label.width(),
                          label.height())

def main():
        app = QApplication(sys.argv)
        window = MainWindows()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()



#PyQt5 layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1,self")
        label2 = QLabel("#2,self")
        label3 = QLabel("#3,self")
        label4 = QLabel("#4,self")
        label5 = QLabel("#5,self")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        #
        #vbox = QVBoxLayout()
        #
        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)
        #vbox.addWidget(label5)

        #hbox = QHBoxLayout()

        #hbox.addWidget(label1)
        #hbox.addWidget(label2)
        #hbox.addWidget(label3)
        #hbox.addWidget(label4)
        #hbox.addWidget(label5)

        gridbox = QGridLayout()

        gridbox.addWidget(label1,0,0)
        gridbox.addWidget(label2,0,1)
        gridbox.addWidget(label3,1,0)
        gridbox.addWidget(label4,1,1)
        gridbox.addWidget(label5,2,0)
        central_widget.setLayout(gridbox)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

'''














