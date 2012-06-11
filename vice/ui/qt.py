import os
import sys
from PySide import QtCore, QtGui, QtDeclarative

qml_dir = os.path.join(os.path.dirname(__file__), 'qml')

class MainWindow(QtDeclarative.QDeclarativeView):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setSource(os.path.abspath(os.path.join(qml_dir, 'main.qml')))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
