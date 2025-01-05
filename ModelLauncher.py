import sys
import os
import subprocess
import logging
from webbrowser import open as open_browser
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QFileDialog
)
from PySide6.QtGui import QIcon, QIntValidator
from gui import Ui_Widget
from logger import setup_logging


class SimulationWorker(QThread):
    """
    A worker thread for asynchronous simulation execution.
    Signals progress and completion status to the main GUI.
    """
    simulation_done = Signal(str, str, str)

    def __init__(self, start_time, stop_time, exe_path, working_directory):
        super().__init__()
        self.start_time = start_time
        self.stop_time = stop_time
        self.exe_path = exe_path
        self.working_directory = working_directory
        logging.info(
            "Simulation Worker initialized. Start Time: %s, Stop Time: %s, "
            "Executable Path: %s", start_time, stop_time, exe_path
        )

    def run(self):
        """
        Executes the simulation using a subprocess.
        Captures and analyzes stdout/stderr for success or failure.
        """
        command = [
            self.exe_path,
            f"-override=startTime={self.start_time},stopTime={self.stop_time}"
        ]
        logging.info(
            "Executing command: %s in working directory: %s",
            command, self.working_directory
        )

        result = subprocess.run(
            command,
            cwd=self.working_directory,
            capture_output=True,
            text=True
        )

        try:
            if "LOG_SUCCESS" in result.stdout:
                logging.info("STDOUT:\n%s", result.stdout.strip())
                self.simulation_done.emit(
                    "Simulation Status",
                    "Simulation successful. Check the log file.",
                    "info"
                )
            else:
                logging.error("STDERR:\n%s", result.stderr.strip())
                self.simulation_done.emit(
                    "Simulation Status",
                    "Simulation failed. Check the log file.",
                    "critical"
                )
        except Exception as e:
            self.simulation_done.emit(
                "Simulation Status",
                f"An error occurred: {str(e)}",
                "critical"
            )


class Widget(QWidget):
    """
    Main GUI widget for the Modelica Model Launcher application.
    Enables users to configure and launch simulations.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stop_time = None
        self.start_time = None
        self.worker = None
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.working_directory = None
        self.exe_path = None

        self.setup_ui()
        self.setWindowTitle("Open Modelica Model Launcher")
        self.setWindowIcon(QIcon("res/OML1.ico"))

    def setup_ui(self):
        """
        Setup the UI and connect signals to their corresponding slots.
        """
        self.ui.launch_but.clicked.connect(self.on_launch_button_clicked)
        self.ui.folder_but.clicked.connect(self.on_folder_button_clicked)
        self.ui.help_but.clicked.connect(self.on_help_button_clicked)
        self.ui.info_but.clicked.connect(self.on_info_button_clicked)
        self.ui.set_but.clicked.connect(self.on_set_button_clicked)

        validator = QIntValidator(0, 1000, self)
        self.ui.start_line.setValidator(validator)
        self.ui.stop_line.setValidator(validator)

    def on_set_button_clicked(self):
        """
        Validate and set start and stop times for the simulation.
        """
        self.start_time = self.ui.start_line.text().strip()
        self.stop_time = self.ui.stop_line.text().strip()

        if self.stop_time <= self.start_time:
            self.show_message_box(
                "Warning",
                "Stop time must be greater than start time.",
                QMessageBox.Warning
            )
            return

    def on_folder_button_clicked(self):
        """
        Open a file dialog to select the simulation executable.
        """
        self.exe_path, _ = QFileDialog.getOpenFileName(
            self, "Select Model Executable", "", "All Files (*)"
        )
        self.ui.main_search_line.setText(self.exe_path)
        if self.exe_path:
            self.working_directory = os.path.dirname(self.exe_path)

    def on_help_button_clicked(self):
        """
        Open the help/documentation URL in the default browser.
        """
        open_browser("https://github.com/mtm-x/OpenModelica-GUI")

    def on_info_button_clicked(self):
        """
        Show application information in a message box.
        """
        self.show_message_box(
            "Information",
            "This is a simple Modelica model launcher. It allows you to "
            "select a Modelica model and specify the start and stop times "
            "for the simulation. The simulation will run in the background, "
            "and you will be notified when it is done.",
            "info"
        )

    def on_launch_button_clicked(self):
        """
        Launch the simulation after validating inputs.
        """
        if not self.start_time or not self.stop_time:
            self.show_message_box(
                "Warning",
                "Please enter valid start and stop times.",
                QMessageBox.Warning
            )
            return

        if not self.exe_path:
            self.show_message_box(
                "Warning",
                "Please select a model file.",
                QMessageBox.Warning
            )
            return

        self.ui.launch_but.setEnabled(False)
        self.worker = SimulationWorker(
            self.start_time,
            self.stop_time,
            self.exe_path,
            self.working_directory
        )
        self.worker.simulation_done.connect(self.on_simulation_done)
        self.worker.start()

    def on_simulation_done(self, title, message, icon_type):
        """
        Perform actions when the simulation is finished.
        """
        self.show_message_box(title, message, icon_type)
        self.ui.launch_but.setEnabled(True)

    def show_message_box(self, title, message, icon_type):
        """
        Display a message box with the specified title, message, and icon.
        """
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
    setup_logging()
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
