#!/usr/bin/env python3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("About")
        label = QLabel("About")
        label.setAlignment(Qt.AlignCenter)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Risk Management Tool")

        label = QLabel("Risk Management Tool")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)


        exit_action = QAction("Exit", self)
        exit_action.setStatusTip("Exit")
        exit_action.triggered.connect(self.onExitClick)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu("&File")
        file_menu.addAction(exit_action)

        about_action = QAction("About", self)
        about_action.setStatusTip("About")
        about_action.triggered.connect(self.onAboutClick)

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(about_action)

    def onExitClick(self, s):
        print("Clicked", s)
        sys.exit()
    def onAboutClick(self, s):
        print("About Clicked", s)

        about_window = AboutDialog(self)
        about_window.exec_()
def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__": main()
