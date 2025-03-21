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



import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 50px;")


    def on_click(self):
        #print("Button clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.label.setText("Goodbye")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# PyQt5 Checkboxes
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox = QCheckBox("Do you like food?",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food!")
        else:
            print("You do not like food")

        #print(state)
        #print("You like food")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio1 = QRadioButton("Visa",self)
        self.radio2 = QRadioButton("Master",self)
        self.radio3 = QRadioButton("GiftCard",self)
        self.radio4 = QRadioButton("In-Store",self)
        self.radio5 = QRadioButton("Online",self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        #self.button_group3 = QButtonGroup(self)
        #self.button_group4 = QButtonGroup(self)
        #self.button_group5 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10,0,300,50)
        self.radio2.setGeometry(10,50,300,50)
        self.radio3.setGeometry(10,100,300,50)
        self.radio4.setGeometry(10,150,300,50)
        self.radio5.setGeometry(10,200,300,50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                            "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)



    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# PyQt5 LineEdit
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Sumbit",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.sumbit)



    def sumbit(self):
        #print("You click the button")
        text = self.line_edit.text()
        print(f"Hello {text}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")


        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: red;
            }
            QPushButton#button2{
                background-color: green;
            }
            QPushButton#button3{
                background-color: blue;
            }
        """)

        #self.button1.setStyleSheet()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

'''









