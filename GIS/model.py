
class Model:
    def __init__(self, view):
        self._view = view

    def addPoint(self):
        self._view.centralwidget.setState('AddPoint')

    def deletePoint(self):
        self._view.centralwidget.setState('DeletePoint')

    def setPoint(self):
        self._view.dialogSetPoint.show()

    def inputPoint(self):
        self._view.dialogInputPoint.show()

    def selectPoint(self):
        self._view.centralwidget.setState('SelectPoint')