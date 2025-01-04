# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import os
import subprocess
from webbrowser import open
from PySide6.QtCore import  QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtGui import QIntValidator
from gui import Ui_Widget

current_directory = os.getcwd()
base_directory = os.path.dirname(os.path.abspath(__file__))

class SimulationWorker(QThread):
    # Signal to notify when the simulation is done
    simulation_done = Signal(str, str, str)  # Custom signal with three arguments

    def __init__(self, start_time, stop_time, exe_path,working_directory):
        super().__init__()
        self.start_time = start_time
        self.stop_time = stop_time
        self.exe_path = exe_path
        self.working_directory = working_directory

    def run(self):
        # Running the simulation in the background
        command = [self.exe_path, "-override=startTime=0,stopTime=5"]
        result = subprocess.run(
            command,
            cwd=self.working_directory,  # Set the working directory
            capture_output=True,
            text=True
        )
        print(result.stdout)
        try:
            if "LOG_SUCCESS" in result.stdout:
                self.simulation_done.emit("Simulation status","Simulation finished successfully.","info") 
            else:
                self.simulation_done.emit("Simulation status",f"Simulation failed: {result.stderr}","critical")
        except Exception as e:
            self.simulation_done.emit("Simulation status",f"An error occurred: {str(e)}","critical")

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.exe_path = None

        #Signals and slots
        self.ui.launch_but.clicked.connect(self.launch_but_clicked)
        #self.ui.set_but.clicked.connect(self.set_but_clicked)
        self.ui.folder_but.clicked.connect(self.folder_but_clicked)
        self.ui.help_but.clicked.connect(self.help_but_clicked)
        self.ui.info_but.clicked.connect(self.info_but_clicked)
        #Title of the executable
        self.setWindowTitle("Open Modelica Model Launcher")
        self.setWindowIcon(QIcon("res/OML1.ico"))
    #def set_but_clicked(self):
        #positive_validator = QIntValidator(0, 1000, self)  # Validator to allow positive numbers (1 to 1000)
        #self.ui.start_line.setValidator(positive_validator)
        #self.ui.stop_line.setValidator(positive_validator)
    def folder_but_clicked(self):
        self.exe_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        self.ui.main_search_line.setText(self.exe_path)
        if self.exe_path:
            self.working_directory = os.path.dirname(self.exe_path)  # Extract the folder path from the file path

    def help_but_clicked(self):
        open("https://github.com/mtm-x/OpenModelica-GUI")

    def info_but_clicked(self):
        info= QMessageBox()
        info.setWindowTitle("Information") 
        info.setText("This is a simple Modelica model launcher. It allows you to select a Modelica model and You can specify the start and stop time for the simulation. The simulation will run in the background and you will be notified when it is done.")
        info.setIcon(QMessageBox.Information)
        info.setStandardButtons(QMessageBox.Ok)
        info.setDefaultButton(QMessageBox.Ok)
        info.exec()

    
    def launch_but_clicked(self):
        self.stop_time = self.ui.stop_line.text().strip()
        self.start_time = self.ui.start_line.text().strip()
        
        if not self.stop_time or not self.start_time:
            self.on_simulation_done("Warning","Please enter start and stop time",QMessageBox.Warning)
            return
        
        if not self.exe_path :
            self.on_simulation_done("Warning","Please select a model",QMessageBox.Warning)
            return
        #disable the launch button once it is pressed to get the result 
        self.ui.launch_but.setEnabled(False)

        # Create and start the worker thread
        self.worker = SimulationWorker(self.start_time, self.stop_time,self.exe_path,self.working_directory)
        self.worker.simulation_done.connect(self.on_simulation_done)  # Connect the signal
        self.worker.start()

    def on_simulation_done(self,title, message,icon_type):
        # Show the message in a dialog
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        if icon_type == "info":
            message_box.setIcon(QMessageBox.Information)
        elif icon_type == "critical":
            message_box.setIcon(QMessageBox.Critical)
        else:
            message_box.setIcon(icon_type)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setDefaultButton(QMessageBox.Ok)
        message_box.exec()

        # Re-enable the launch button after simulation finishes
        self.ui.launch_but.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
