import sys
import os
import subprocess
from webbrowser import open
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtGui import QIcon, QIntValidator
from gui import Ui_Widget
 


class SimulationWorker(QThread):
    simulation_done = Signal(str, str, str)  # Signal with title, message, and icon type

    def __init__(self, start_time, stop_time, exe_path, working_directory):
        super().__init__()
        self.start_time = start_time
        self.stop_time = stop_time
        self.exe_path = exe_path
        self.working_directory = working_directory

    def run(self):
        command = [self.exe_path, f"-override=startTime={self.start_time},stopTime={self.stop_time}"]
        result = subprocess.run(
            command,
            cwd=self.working_directory,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        try:
            if "LOG_SUCCESS" in result.stdout:
                self.simulation_done.emit("Simulation Status", "Simulation finished successfully.", "info")
            else:
                self.simulation_done.emit("Simulation Status", f"Simulation failed: {result.stderr}", "critical")
        except Exception as e:
            self.simulation_done.emit("Simulation Status", f"An error occurred: {str(e)}", "critical")


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.worker = None
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.working_directory = None
        self.exe_path = None

        self.setup_ui()
        self.setWindowTitle("Open Modelica Model Launcher")
        self.setWindowIcon(QIcon("res/OML1.ico"))

    def setup_ui(self):
        """Connect signals and set up the UI elements."""
        self.ui.launch_but.clicked.connect(self.on_launch_button_clicked)
        self.ui.folder_but.clicked.connect(self.on_folder_button_clicked)
        self.ui.help_but.clicked.connect(self.on_help_button_clicked)
        self.ui.info_but.clicked.connect(self.on_info_button_clicked)

        # Set validators for start and stop time
        positive_validator = QIntValidator(0, 1000, self)
        self.ui.start_line.setValidator(positive_validator)
        self.ui.stop_line.setValidator(positive_validator)

    def on_folder_button_clicked(self):
        """Open a file dialog to select the executable."""
        self.exe_path, _ = QFileDialog.getOpenFileName(None, "Select Model Executable", "", "All Files (*)")
        self.ui.main_search_line.setText(self.exe_path)
        if self.exe_path:
            self.working_directory = os.path.dirname(self.exe_path)

    def on_help_button_clicked(self):
        """Open the help URL."""
        open("https://github.com/mtm-x/OpenModelica-GUI")

    def on_info_button_clicked(self):
        """Show an information message box."""
        self.show_message_box(
            "Information",
            "This is a simple Modelica model launcher. It allows you to select a Modelica model "
            "and specify the start and stop time for the simulation. The simulation will run in "
            "the background, and you will be notified when it is done.",
            "info"
        )

    def on_launch_button_clicked(self):
        """Validate inputs and launch the simulation worker."""
        start_time = self.ui.start_line.text().strip()
        stop_time = self.ui.stop_line.text().strip()

        if not start_time or not stop_time:
            self.show_message_box("Warning", "Please enter start and stop time", QMessageBox.Warning)
            return
        if not self.exe_path:
            self.show_message_box("Warning", "Please select a model", QMessageBox.Warning)
            return

        self.ui.launch_but.setEnabled(False)
        self.worker = SimulationWorker(start_time, stop_time, self.exe_path, self.working_directory)
        self.worker.simulation_done.connect(self.on_simulation_done)
        self.worker.start()

    def on_simulation_done(self, title, message, icon_type):
        """Handle simulation results and re-enable the launch button."""
        self.show_message_box(title, message, icon_type)
        self.ui.launch_but.setEnabled(True)

    def show_message_box(self, title, message, icon_type):
        """Display a message box with the provided title, message, and icon."""
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
        message_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
