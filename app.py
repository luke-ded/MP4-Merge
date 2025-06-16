import sys, time

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from merge import merge


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MP4 Merge")
        self.setGeometry(100, 100, 500, 200)
        self.setStyleSheet("background-color: #e0e0e0;")

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


        # Run button
        self.run_button = QPushButton("Merge Now")
        self.run_button.setEnabled(False)
        self.run_button.clicked.connect(self.run_merge)

        main_layout.addWidget(self.run_button)


        # Status message
        self.status_label = QLabel("Ready. Select a folder to begin.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Push elements to top
        main_layout.addStretch()


    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select MP4 Folder")

        if folder:
            self.folder_path.setText(folder)
            self.status_label.setText("Ready to merge.")
            self.run_button.setEnabled(True)
        else:
            self.status_label.setText("Folder selection cancelled.")

            if not self.folder_path.text():
                self.run_button.setEnabled(False) 


    def run_merge(self):
        self.run_button.setEnabled(False) 
        folder = self.folder_path.text()

        if not folder:
            self.status_label.setText("No folder selected.")
            return
        
        self.status_label.setText("Merging in progress...")

        merge(folder, folder, "output.mp4")

        self.run_button.setEnabled(True)
        self.status_label.setText("Merge Complete. Check the selected folder for your output file.")

        
        
app = QApplication(sys.argv)
window = AppWindow()
window.show()
app.exec()