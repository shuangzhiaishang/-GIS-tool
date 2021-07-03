import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

from point import CirclePoint, TrianglePoint, SquarePoint

class Canvas(QWidget):

    def __init__(self):
        super(Canvas, self).__init__()

        self.pointShape = '圆形'
        self.pointColor = '黑色'
        self.pointFill = '无'
        self.lineWidth = 1
        self.pointSize = 4
        self.resize(400, 300)
        self.move(100, 100)
        self.setMouseTracking(True)
        self.points = []
        self.state = 'null'
        self.labelCoords = QLabel('X: 0, Y: 0', self)
        self.labelCoords.resize(145, 20)
        self.labelCoords.move(0, 1122)
        self.startX, self.startY = 0, 0
        self.endX, self.endY = 0, 0
        self.showSelectionRect = False
    
    def setState(self, state):
        self.state = state

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for point in self.points:
            if not point.isSelected():
                point.draw(painter)
            elif point.skip():
                continue
            point.draw(painter)

        if self.state == 'SelectPoint' and self.showSelectionRect:
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            painter.drawRect(self.startX, self.startY, self.endX-self.startX, self.endY-self.startY)


    def mousePressEvent(self, event):
        if self.state == 'AddPoint':
            self.addPoint(event)
            
        elif self.state == 'DeletePoint':
            self.deletePoint(event)

        elif self.state == 'SelectPoint':
            self.setSelectionStart(event)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.labelCoords.setText(f'X: {x}, Y: {y}')

        if self.state == 'SelectPoint':
            self.setSelectionEnd(event)

    def mouseReleaseEvent(self, event):
        if self.state == 'SelectPoint':
            self.selectPoint(event)

    def addPoint(self, event):
        if self.pointShape == '圆形':
            point = CirclePoint(event.pos().x(), event.pos().y(), self.pointColor, self.pointSize)
            self.points.append(point)
        elif self.pointShape == '三角形':
            point = TrianglePoint(event.pos().x(), event.pos().y(), self.pointColor, self.pointSize)
            self.points.append(point)
        elif self.pointShape == '方形':
            point = SquarePoint(event.pos().x(), event.pos().y(), self.pointColor, self.pointSize)
            self.points.append(point)
        self.update()

    def deletePoint(self, event):
        x = event.pos().x()
        y = event.pos().y()
        for i in range(len(self.points)-1, -1, -1):
            if self.points[i].cover(x, y):
                self.points.pop(i)
                break
        self.update()

    def setSelectionStart(self, event):
        self.startX = event.pos().x()
        self.startY = event.pos().y()
        self.showSelectionRect = True

    def setSelectionEnd(self, event):
        if event.buttons() == Qt.LeftButton:
            self.endX = event.pos().x()
            self.endY = event.pos().y()
            self.update()

    def selectPoint(self, event):
        self.showSelectionRect = False
        self.update()
        for point in self.points:
            if min(self.startX, self.endX) <= point.x <= max(self.startX, self.endX) and min(self.startY, self.endY) <= point.y <= max(self.startY, self.endY):
                point.setSelected(True)
        self.blink()

    def blink(self):
        s = 0
        while s < 10:
            self.update()
            time.sleep(1)
            s += 1
