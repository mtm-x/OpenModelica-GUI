import sys
from PySide6.QtCore import QStringListModel, QSortFilterProxyModel, Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

import subprocess
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import os
current_directory = os.getcwd()

from PySide6.QtCore import QThread, Signal

class SimulationWorker(QThread):
    # Signal to notify when the simulation is done
    simulation_done = Signal(str)

    def __init__(self, tank_exe, start_time, stop_time):
        super().__init__()
        self.tank_exe = tank_exe
        self.start_time = start_time
        self.stop_time = stop_time

    def run(self):
        # Running the simulation in the background
        process = subprocess.run(
            [self.tank_exe, f"-override=startTime={self.start_time},stopTime={self.stop_time}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(process.stdout)
        try:
            if "LOG_SUCCESS" in process.stdout:
                self.simulation_done.emit("Simulation finished successfully.")
            else:
                self.simulation_done.emit(f"Simulation failed: {process.stderr}")
        except Exception as e:
            self.simulation_done.emit(f"An error occurred: {str(e)}")
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        data = ["TwoTankModel","test model1","testmode2"]

        self.source_model = QStringListModel(data)
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
        #self.ui.launch_but.setEnabled(False)
    def pressed_list_item(self):
        self.current_model = None
        self.current_model = self.ui.listView.currentIndex().data()
        if self.current_model == "TwoTankModel":
            print("TwoTankModel")


    def launch_but_clicked(self):
        self.stop_time = self.ui.stop_line.text().strip()
        self.start_time = self.ui.start_line.text().strip()
        tank_exe = os.path.join(current_directory,"Model","TwoConnectedTanks","Tank.exe")
        print(tank_exe)
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
        
        self.ui.launch_but.setEnabled(False)

        # Create and start the worker thread
        self.worker = SimulationWorker(tank_exe, self.start_time, self.stop_time)
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
