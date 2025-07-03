from PySide6.QtWidgets import QTextEdit, QWidget, QHBoxLayout,QVBoxLayout, QPushButton

class text_edit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.text_edit = QTextEdit()

        current_text = QPushButton("Current text")
        current_text.clicked.connect(self.current_text_clicked)

        copy = QPushButton("Copy")
        copy.clicked.connect(self.text_edit.copy)

        cut = QPushButton("Cut")
        cut.clicked.connect(self.text_edit.cut)

        paste = QPushButton("Paste")
        paste.clicked.connect(self.text_edit.paste)

        undo = QPushButton("Undo")
        undo.clicked.connect(self.text_edit.undo)

        redo = QPushButton("Redo")
        redo.clicked.connect(self.text_edit.redo)

        clear = QPushButton("Clear")
        clear.clicked.connect(self.text_edit.clear)

        set_plain_text = QPushButton("Set Plain Text")
        set_plain_text.clicked.connect(self.setplaintext)

        set_html = QPushButton("Set HTML")
        set_html.clicked.connect(self.setHtml)

        hlayout = QHBoxLayout()
        hlayout.addWidget(current_text)
        hlayout.addWidget(copy)
        hlayout.addWidget(cut)
        hlayout.addWidget(paste)
        hlayout.addWidget(undo)
        hlayout.addWidget(redo)
        hlayout.addWidget(set_plain_text)
        hlayout.addWidget(set_html)
        hlayout.addWidget(clear)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.text_edit)

        self.setLayout(vlayout)

    def current_text_clicked(self):
        print(self.text_edit.toPlainText())

    def setHtml(self):
        self.text_edit.setHtml("<h1>hello</h1>")

    def setplaintext(self):
        self.text_edit.setPlainText("I am Autonomus")