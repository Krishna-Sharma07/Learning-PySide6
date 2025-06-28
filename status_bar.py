from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class mainwindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window")

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("&Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(100,100))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        toolbar.addSeparator()

        action2 = QAction(QIcon("z.png"),"Some other action", self)
        action2.setStatusTip("Status message 2")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        self.setStatusBar(QStatusBar(self))

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Hello", 2000)