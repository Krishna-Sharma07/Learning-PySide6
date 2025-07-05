from PySide6.QtWidgets import QListWidget, QPushButton, QAbstractItemView, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout

class List(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List")

        self.list = QListWidget(self)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.addItem("One")
        self.list.addItems(["Two","Three"])
        self.list.currentItemChanged.connect(self.current_item_changed)
        self.list.currentTextChanged.connect(self.current_text_changed)

        add = QPushButton("Add Item")
        add.clicked.connect(self.add_item)

        delete = QPushButton("Delete Item")
        delete.clicked.connect(self.delete_item)

        count = QPushButton("Count Items")
        count.clicked.connect(self.count_items)

        selected = QPushButton("Selected Item")
        selected.clicked.connect(self.selected_item)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.list)
        vlayout.addWidget(add)
        vlayout.addWidget(delete)
        vlayout.addWidget(count)
        vlayout.addWidget(selected)
        

        self.setLayout(vlayout)

    def current_item_changed(self, item):
        print("Current Item: ", item.text())

    def current_text_changed(self, text):
        print("Current Text: ", text)

    def add_item(self):
        self.list.addItem("new item")

    def delete_item(self):
        self.list.takeItem(self.list.currentRow())

    def count_items(self):
        print("Item count: ", self.list.count())

    def selected_item(self):
        l = self.list.selectedItems()
        for i in l:
            print(i.text())