import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPen)
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        #resize设置宽高，move设置位置
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("简单的画板4.0")

        #setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
        self.setMouseTracking(False)

        '''
            要想将按住鼠标后移动的轨迹保留在窗体上
            需要一个列表来保存所有移动过的点
        '''
        self.x = 0
        self.y = 0
        self.endx = 0
        self.endy = 0

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(self.x, self.y, abs(self.x - self.endx), abs(self.y - self.endy))
        
        painter.end()

    def mousePressEvent(self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()

    def mouseMoveEvent(self, event):
        '''
            按住鼠标移动事件：将当前点添加到pos_xy列表中
            调用update()函数在这里相当于调用paintEvent()函数
            每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        '''
        self.endx = event.pos().x()
        self.endy = event.pos().y()

        self.update()

    def mouseReleaseEvent(self, event):
        '''
            重写鼠标按住后松开的事件
            在每次松开后向pos_xy列表中添加一个断点(-1, -1)
            然后在绘画时判断一下是不是断点就行了
            是断点的话就跳过去，不与之前的连续
        '''
        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)

        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pyqt_learn = Example()
    pyqt_learn.show()
    app.exec_()