from model import Model

class Controller:
    def __init__(self, view):
        self._model = Model(view)
        self._view = view

        self.connectSignals()

    def connectSignals(self):
        self._view.actionAddPoint.triggered.connect(self._model.addPoint)
        self._view.actionDeletePoint.triggered.connect(self._model.deletePoint)
        self._view.actionSetPoint.triggered.connect(self._model.setPoint)
        self._view.actionInputPoint.triggered.connect(self._model.inputPoint)
        self._view.actionSelectPoint.triggered.connect(self._model.selectPoint)