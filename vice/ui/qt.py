#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PySide import QtCore, QtGui, QtDeclarative

class MainWindow(QtDeclarative.QDeclarativeView):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)


        filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'qml', 'view.qml')
        )
        self.setWindowTitle("Main Window")
        self.setSource(filename)
        self.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
