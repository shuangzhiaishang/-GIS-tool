
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainWindow import Ui_MainWindow
from controller import Controller


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    controller = Controller(window)

    window.show()
    sys.exit(app.exec_())

'''
TODO:
    1. display coordinates real time        √
    2. check point attributes
    3. modify point attributes
    4. coordinates translate
    5. files                               
    6. zoom in and zoom out
    7. tree view on the left
    8. 
'''