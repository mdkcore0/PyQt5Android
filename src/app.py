#!/usr/bin/env python3

import sys
import os

# from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QUrl
# from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # view = QQuickView()

    # view.setSource(QUrl.fromLocalFile(
        # os.path.join(os.path.dirname(__file__), 'main.qml')))

    # view.resize(300, 300)
    # view.setColor(Qt.black)
    # view.showFullScreen()

    # sys.exit(app.exec_())
    w = QWidget(windowTitle="Sour?")
    w.setStyleSheet("background-color:magenta;")
    w.show()
    app.exec_()
    sys.exit()
