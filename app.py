import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

# Subclass QMainWindow to customize your application's main window
class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MP4 Merge")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)


        # Folder selection
        folder_select_layout = QHBoxLayout()

        self.folder_select_label = QLabel("Selected Folder:")
        folder_select_layout.addWidget(self.folder_select_label)

        self.folder_path = QLineEdit()
        self.folder_path.setReadOnly(True)
        self.folder_path.setPlaceholderText("No folder selected")
        folder_select_layout.addWidget(self.folder_path)

        self.select_button = QPushButton("Select Folder")
        self.select_button.clicked.connect(self.select_folder)
        folder_select_layout.addWidget(self.select_button)

        main_layout.addLayout(folder_select_layout)


        main_layout.addStretch()

    def select_folder(self):
        print("placeholder")
        



        
app = QApplication(sys.argv)
window = AppWindow()
window.show()
app.exec()