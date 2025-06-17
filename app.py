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


        # Input Folder selection
        input_folder_select_layout = QHBoxLayout()

        self.input_folder_select_label = QLabel("Input Folder:")
        input_folder_select_layout.addWidget(self.input_folder_select_label)

        self.input_folder_path = QLineEdit()
        self.input_folder_path.setReadOnly(True)
        self.input_folder_path.setPlaceholderText("No folder selected")
        input_folder_select_layout.addWidget(self.input_folder_path)

        self.input_select_button = QPushButton("Select Folder")
        self.input_select_button.clicked.connect(self.select_infolder)
        input_folder_select_layout.addWidget(self.input_select_button)

        main_layout.addLayout(input_folder_select_layout)


        # Output Folder selection
        output_folder_select_layout = QHBoxLayout()

        self.output_folder_select_label = QLabel("Output Folder:")
        output_folder_select_layout.addWidget(self.output_folder_select_label)

        self.output_folder_path = QLineEdit()
        self.output_folder_path.setReadOnly(True)
        self.output_folder_path.setPlaceholderText("No folder selected")
        output_folder_select_layout.addWidget(self.output_folder_path)

        self.output_select_button = QPushButton("Select Folder")
        self.output_select_button.clicked.connect(self.select_outfolder)
        output_folder_select_layout.addWidget(self.output_select_button)

        main_layout.addLayout(output_folder_select_layout)


        # Output File Name
        output_file_name_layout = QHBoxLayout()

        self.output_file_name_label = QLabel("Output File Name:")
        output_file_name_layout.addWidget(self.output_file_name_label)

        self.output_file_input = QLineEdit()
        self.output_file_input.setPlaceholderText("filename")
        self.output_file_input.setReadOnly(True)
        #self.output_file_input.setFixedWidth(200)
        output_file_name_layout.addWidget(self.output_file_input)

        self.output_file_name_suffix_label = QLabel(".mp4  ")
        output_file_name_layout.addWidget(self.output_file_name_suffix_label)


        self.auto_checkbox = QCheckBox("Auto")
        self.auto_checkbox.setChecked(True)
        output_file_name_layout.addWidget(self.auto_checkbox)

        main_layout.addLayout(output_file_name_layout)


        # Push elements to top
        main_layout.addStretch()


        # Status message
        self.status_label = QLabel("Ready. Select a folder to begin.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.status_label)
        

        # Run button
        self.run_button = QPushButton("Merge Now")
        self.run_button.setEnabled(False)
        self.run_button.clicked.connect(self.run_merge)

        main_layout.addWidget(self.run_button)


    def select_infolder(self):
        infolder = QFileDialog.getExistingDirectory(self, "Select MP4 Folder")

        if infolder:
            self.input_folder_path.setText(infolder)
            self.status_label.setText("Ready to merge.")

            if self.output_folder_path.text():
                self.run_button.setEnabled(True)
        else:
            self.status_label.setText("Folder selection cancelled.")

            if not self.input_folder_path.text() or not self.output_folder_path.text():
                self.run_button.setEnabled(False) 


    def select_outfolder(self):
        outfolder = QFileDialog.getExistingDirectory(self, "Select MP4 Folder")

        if outfolder:
            self.output_folder_path.setText(outfolder)
            self.status_label.setText("Ready to merge.")

            if self.input_folder_path.text():
                self.run_button.setEnabled(True)
        else:
            self.status_label.setText("Folder selection cancelled.")

            if not self.output_folder_path.text() or not self.input_folder_path.text():
                self.run_button.setEnabled(False) 


    def run_merge(self):
        self.run_button.setEnabled(False) 
        infolder = self.input_folder_path.text()
        outfolder = self.output_folder_path.text()

        if not infolder or not outfolder:
            self.status_label.setText("No folder selected.")
            return
        
        self.status_label.setText("Merging in progress...")

        merge(infolder, outfolder, "output.mp4")

        self.run_button.setEnabled(True)
        self.status_label.setText("Merge Complete. Check the selected folder for your output file.")

        
        
app = QApplication(sys.argv)
window = AppWindow()
window.show()
app.exec()