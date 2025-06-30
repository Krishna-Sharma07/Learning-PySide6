from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLable and QLineEdit")

        lable = QLabel("Name :")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab ")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I am Here")

        hlayout = QHBoxLayout()
        hlayout.addWidget(lable)
        hlayout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(hlayout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def button_clicked(self):
        print("Name : ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print("Text changed to : ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def editing_finished(self):
        print("Finished Editing")

    def selection_changed(self):
        print("Selected Text: ", self.line_edit.selectedText())

    def selection_changed(self, new_text):
        print("Text edited. New Text : ", new_text)
