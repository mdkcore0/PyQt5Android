#!/usr/bin/env python3

import sys
#import os

from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QUrl
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QQuickView()

    # view.setSource(QUrl.fromLocalFile(
        # os.path.join(os.path.dirname(__file__), 'main.qml')))

    view.resize(300, 300)
    view.setColor(Qt.green)
    view.showFullScreen()

    sys.exit(app.exec_())
