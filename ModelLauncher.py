# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import os
from PySide6.QtCore import QStringListModel, QSortFilterProxyModel, Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
import subprocess
from gui import Ui_Widget

current_directory = os.getcwd()
base_directory = os.path.dirname(os.path.abspath(__file__))

class SimulationWorker(QThread):
    # Signal to notify when the simulation is done
    simulation_done = Signal(str) #custom signal

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
                self.simulation_done.emit("Simulation finished successfully.") 
            else:
                self.simulation_done.emit(f"Simulation failed: {result.stderr}")
        except Exception as e:
            self.simulation_done.emit(f"An error occurred: {str(e)}")

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        models = ["TwoTankModel","test model1","testmode2"]  #test model1,testmode2 are sample models

        #searching for desired model
        self.source_model = QStringListModel(models)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.source_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  

        #Signals and slots
        self.ui.listView.setModel(self.proxy_model)
        self.ui.main_search_line.textChanged.connect(self.proxy_model.setFilterFixedString)
        self.ui.launch_but.clicked.connect(self.launch_but_clicked)
        self.ui.listView.clicked.connect(self.pressed_list_item)
        #self.ui.set_but.clicked.connect(self.set_but_clicked)
        self.setWindowTitle("Open Modelica Model Launcher")
        
    def pressed_list_item(self):
        self.current_model = None
        self.current_model = self.ui.listView.currentIndex().data()
        if self.current_model == "TwoTankModel":
            print("TwoTankModel")

    def launch_but_clicked(self):
        self.stop_time = self.ui.stop_line.text().strip()
        self.start_time = self.ui.start_line.text().strip()
        
        if not self.stop_time or not self.start_time:
            message_box = QMessageBox(self)
            message_box.setWindowTitle("Warning")
            message_box.setText("Time not set")
            message_box.setIcon(QMessageBox.Warning)  
            message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            message_box.setDefaultButton(QMessageBox.Ok)
            message_box.exec()
            
       
        if  self.ui.listView.currentIndex().data() is None:
            listview_msg = QMessageBox(self)
            listview_msg.setWindowTitle("Warning")
            listview_msg.setText("Please select a model")
            listview_msg.setIcon(QMessageBox.Warning)
            listview_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            listview_msg.setDefaultButton(QMessageBox.Ok)
            listview_msg.exec()
            return
        #disable the launch button once it is pressed to get the result 
        self.ui.launch_but.setEnabled(False)

        #Directories for subprocess
        relative_path_to_exe = "Model/NonInteractingTanks.TwoConnectedTanks/TwoConnectedTanks.exe"
        relative_path_to_working_dir = "Model/NonInteractingTanks.TwoConnectedTanks"
        # Construct absolute paths
        self.exe_path = os.path.join(base_directory, relative_path_to_exe)
        self.working_directory = os.path.join(base_directory, relative_path_to_working_dir)


        # Create and start the worker thread
        self.worker = SimulationWorker(self.start_time, self.stop_time,self.exe_path,self.working_directory)
        self.worker.simulation_done.connect(self.on_simulation_done)  # Connect the signal
        self.worker.start()

    def on_simulation_done(self, message):
        # Show the message in a dialog
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Simulation Status")
        message_box.setText(message)
        message_box.setIcon(QMessageBox.Information)
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
