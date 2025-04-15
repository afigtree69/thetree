import sys
import PySide6.QtWidgets as qt

from mdn_box import MdnBox


class HelloWorldApp(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.init_layout()

    def init_layout(self):
        layout = qt.QGridLayout()

        items = [
            ("Blog", "JavaScript Temporal is Coming", "A new way to handle date and times is being added to javascript."),
            (
            "Blog", "JavaScript Temporal is Coming", "A new way to handle date and times is being added to javascript."),
            (
            "Blog", "JavaScript Temporal is Coming", "A new way to handle date and times is being added to javascript."),
            (
            "Blog", "JavaScript Temporal is Coming", "A new way to handle date and times is being added to javascript.")
        ]
        row = 0
        col = 0
        MAX_ROW = 2
        for mdnBox in items:


            box = MdnBox(mdnBox[0], mdnBox[1], mdnBox[2])
            layout.addWidget(box, row, col)
            row += 1
            if row == MAX_ROW:
                row = 0
                col += 1

        grid_widget = qt.QWidget()
        grid_widget.setObjectName("grid")
        grid_widget.setLayout(layout)
        main_layout = qt.QVBoxLayout()
        main_layout.addWidget(grid_widget)
        self.setLayout(main_layout)



app = qt.QApplication(sys.argv)
app.setStyleSheet("""
                #grid { 
                    background-color: #1f1f1f;
                }

                [class="mdnBox"] {
                    border: 6px solid red;
                }
    """)
result = HelloWorldApp()
result.show()
app.exec()
