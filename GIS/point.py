from math import sqrt

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint

class Point():
    def __init__(self, x, y, color, size, lineWidth=1, fill=None):
        self.x = x
        self.y = y
        self.color =  color
        self.size = size
        self.lineWidth = lineWidth
        self.selected = False
        self.erase = 0

    def draw(self, painter):
        ...

    def cover(self, x, y):
        ...

    def setSelected(self, condition):
        self.selected = condition

    def isSelected(self):
        return self.selected

    def skip(self):
        ans = self.erase
        self.erase = 1 - self.erase
        return ans


class CirclePoint(Point):
    def draw(self, painter):
        pen = QPen(Qt.black, self.lineWidth, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawEllipse(self.x, self.y, self.size, self.size)

    def cover(self, x, y):
        return abs(self.x - x) <= self.size and abs(self.y - y) <= self.size


class TrianglePoint(Point):
    def draw(self, painter):
        pen = QPen(Qt.black, self.lineWidth, Qt.SolidLine)
        painter.setPen(pen)
        points = [
            QPoint(self.x - self.size*self.size**0.5/2, self.y + self.size/2),
            QPoint(self.x + self.size*self.size**0.5/2, self.y + self.size/2),
            QPoint(self.x, self.y - self.size)
        ]
        poly = QPolygon(points)
        painter.drawPolygon(poly)

    def cover(self, x, y):
        x -= self.x
        y -= self.y + self.size/2
        y = -y
        if x <= 0:
            return 0 <= y <= sqrt(3) * x + 1.5 * self.size and x >= -self.size*sqrt(3)/2
        return 0 <= y <= -sqrt(3) * x + 1.5 * self.size and x <= self.size*sqrt(3)/2



class SquarePoint(Point):
    def draw(self, painter):
        pen = QPen(Qt.black, self.lineWidth, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(self.x - self.size/2, self.y - self.size/2, self.size, self.size)

    def cover(self, x, y):
        return self.x - self.size/2 <= x <= self.x + self.size/2 and self.y - self.size/2 <= y <= self.y + self.size/2