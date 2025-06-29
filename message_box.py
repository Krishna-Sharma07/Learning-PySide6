from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message box")
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_hard_clicked)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_critical_clicked)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_question_clicked)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_information_clicked)

        button_warning = QPushButton("warning")
        button_warning.clicked.connect(self.button_warning_clicked)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_about_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    def button_hard_clicked(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it ?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")
    
    def button_critical_clicked(self):
        ret = QMessageBox.critical(self, "Message Title 2", "Critical Message", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")

    def button_question_clicked(self):
        ret = QMessageBox.question(self, "Message Title 3", "Question Message", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")

    def button_information_clicked(self):
        ret = QMessageBox.information(self, "Message Title 4", "Information Message", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")

    def button_warning_clicked(self):
        ret = QMessageBox.warning(self, "Message Title 5", "Warning Message", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")

    def button_about_clicked(self):
        ret = QMessageBox.about(self, "Message Title g", "About Message")
        if ret == QMessageBox.Ok:
            print("User choose OK")
        else:
            print("User choose cancle")