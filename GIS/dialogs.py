from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox

from point import CirclePoint, SquarePoint, TrianglePoint

class SetPointDialog(QDialog):
    def __init__(self, canvas):
        super(SetPointDialog, self).__init__()
        self._canvas = canvas
        self.setWindowTitle('设置点属性')
        self.resize(391, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 191, 131))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel('点形状:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxShape = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxShape.addItem("圆形")
        self.comboBoxShape.addItem("三角形")
        self.comboBoxShape.addItem("方形")
        self.horizontalLayout.addWidget(self.comboBoxShape)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel('点颜色:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBoxColor = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxColor.addItem("黑色")
        self.horizontalLayout_2.addWidget(self.comboBoxColor)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel('填充:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBoxFill = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxFill.addItem("无")
        self.horizontalLayout_3.addWidget(self.comboBoxFill)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 220, 271, 61))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButtonOK = QtWidgets.QPushButton('确认', self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.addWidget(self.pushButtonOK)
        self.pushButtonCancel = QtWidgets.QPushButton('退出', self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.addWidget(self.pushButtonCancel)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QtWidgets.QLabel('点大小:', self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setText('4')
        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.box = QMessageBox(QMessageBox.Warning, '警告', '无效输入')
        self.box.addButton(self.tr('重试'), QMessageBox.YesRole)

        self.pushButtonOK.clicked.connect(self.confirm)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def confirm(self):
        # Observer
        # Changes attributes whenever click OK
        self._canvas.pointShape = self.comboBoxShape.currentText()
        self._canvas.pointColor = self.comboBoxColor.currentText()
        self._canvas.pointFill = self.comboBoxFill.currentText()
        size = self.lineEdit.text()

        try:
            self._canvas.pointSize = int(size)
        except ValueError:
            self.box.show()
            return

        self.close()

    def cancel(self):
        '''
            attributes won't change if cancel is clicked
        '''
        index = self.comboBoxShape.findText(self._canvas.pointShape, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBoxShape.setCurrentIndex(index)

        index = self.comboBoxColor.findText(self._canvas.pointColor, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBoxColor.setCurrentIndex(index)

        index = self.comboBoxFill.findText(self._canvas.pointFill, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBoxFill.setCurrentIndex(index)

        self.lineEdit.setText(str(self._canvas.pointSize))

        self.close()


class InputPointDialog(QDialog):
    def __init__(self, canvas):
        super(InputPointDialog, self).__init__()
        self._canvas = canvas
        self.setWindowTitle('输入点')
        self.resize(253, 269)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 210, 151, 51))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonOK = QtWidgets.QPushButton('确认', self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonOK.setFont(font)
        self.horizontalLayout.addWidget(self.pushButtonOK)
        self.pushButtonCancel = QtWidgets.QPushButton('退出', self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCancel.setFont(font)
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 170, 151, 41))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelSize = QtWidgets.QLabel('点大小:', self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSize.setFont(font)
        self.horizontalLayout_3.addWidget(self.labelSize)
        self.lineEditSize = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEditSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.lineEditSize)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 181, 161))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.labelX = QtWidgets.QLabel('X:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelX.setFont(font)
        self.horizontalLayout_2.addWidget(self.labelX)
        self.lineEditX = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.lineEditX)
        self.labelY = QtWidgets.QLabel('Y:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelY.setFont(font)
        self.horizontalLayout_2.addWidget(self.labelY)
        self.lineEditY = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.lineEditY)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.labelShape = QtWidgets.QLabel('点形状:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelShape.setFont(font)
        self.horizontalLayout_4.addWidget(self.labelShape)
        self.comboBoxShape = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxShape.addItem("圆形")
        self.comboBoxShape.addItem("三角形")
        self.comboBoxShape.addItem("方形")
        self.horizontalLayout_4.addWidget(self.comboBoxShape)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.labelColor = QtWidgets.QLabel('点颜色:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelColor.setFont(font)
        self.horizontalLayout_5.addWidget(self.labelColor)
        self.comboBoxColor = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxColor.addItem("黑色")
        self.horizontalLayout_5.addWidget(self.comboBoxColor)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.labelFill = QtWidgets.QLabel('填充:', self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFill.setFont(font)
        self.horizontalLayout_6.addWidget(self.labelFill)
        self.comboBoxFill = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxFill.addItem("无")
        self.horizontalLayout_6.addWidget(self.comboBoxFill)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.lineEditSize.setText('4')

        self.box = QMessageBox(QMessageBox.Warning, '警告', '无效输入')
        self.box.addButton(self.tr('重试'), QMessageBox.YesRole)

        self.pushButtonOK.clicked.connect(self.confirm)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def confirm(self):
        shape = self.comboBoxShape.currentText()
        color = self.comboBoxColor.currentText()
        fill = self.comboBoxFill.currentText()
        x = self.lineEditX.text()
        y = self.lineEditY.text()
        size = self.lineEditSize.text()
        
        # Input not valid
        try:
            x = int(x)
            y = int(y)
            size = int(size)
        except ValueError:
            self.box.show()
            return

        if shape == '圆形':
            point = CirclePoint(x, y, color, size, fill=fill)
        elif shape == '三角形':
            point = TrianglePoint(x, y, color, size, fill=fill)
        elif shape == '方形':
            point = SquarePoint(x, y, color, size, fill=fill)

        self._canvas.points.append(point)
        self.cancel()

    def cancel(self):
        index = self.comboBoxShape.findText('圆形', QtCore.Qt.MatchFixedString)
        self.comboBoxShape.setCurrentIndex(index)

        index = self.comboBoxColor.findText('黑色', QtCore.Qt.MatchFixedString)
        self.comboBoxColor.setCurrentIndex(index)

        index = self.comboBoxFill.findText('无', QtCore.Qt.MatchFixedString)
        self.comboBoxFill.setCurrentIndex(index)

        self.lineEditSize.setText('4')
        self.lineEditX.setText('')
        self.lineEditY.setText('')

        self.close()

    def closeEvent(self, event):
        self.cancel()
    
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    a = 1
    d = InputPointDialog(a)
    d.show()
    sys.exit(app.exec_())