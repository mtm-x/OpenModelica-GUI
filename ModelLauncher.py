import logging
import os
import subprocess
from webbrowser import open as open_browser

from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from src.gui import Ui_Widget
from src.logger import setup_logging

FILE_DIALOG_TITLE = "Please Select Model Executable"


class Launcher(QWidget):
    """
    A launcher application for executing Modelica models with specific
    simulation start and stop times.
    """

    def __init__(self):
        """
        Initialize the Launcher class and set up the UI, validators,
        and event handlers.
        """
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Set window title and icon
        self.setWindowTitle("OpenModelica Model Launcher")
        self.setWindowIcon(QIcon("res/OML1.ico"))

        # Initialize variables to hold user selections and input values
        self.working_directory = None
        self.exe_path = None
        self.start_time = None
        self.stop_time = None

        # Connect UI buttons and fields to their respective event handlers
        self.ui.set_but.clicked.connect(self.on_set_button)
        self.ui.folder_but.clicked.connect(self.on_folder_button)
        self.ui.launch_but.clicked.connect(self.on_launch_button)
        self.ui.help_but.clicked.connect(self.on_help_button)
        self.ui.info_but.clicked.connect(self.on_info_button)
        self.ui.start_line.textChanged.connect(self.text_changed_start)
        self.ui.stop_line.textChanged.connect(self.text_changed_stop)
        self.ui.clear_but.clicked.connect(self.clear)

        # Add input validators to restrict start/stop time to integers
        # within range 0-10000
        validator = QIntValidator(0, 10000, self)
        self.ui.start_line.setValidator(validator)
        self.ui.stop_line.setValidator(validator)

    def on_set_button(self):
        """
        Handle the set button click event. Validate and log the start and
        stop time values.
        """
        self.start_time = self.ui.start_line.text().strip()
        self.stop_time = self.ui.stop_line.text().strip()
        logging.info(
             "Start Time: %s, Stop Time: %s", self.start_time, self.stop_time
                    )

        # Show an error message if either of the input fields is empty.
        if not self.start_time or not self.stop_time:
            self.show_message_box(
                "Error",
                "Please enter a start and stop time and click set time",
                "warning"
            )
            return

        # Show an error message if stop time <= start time.
        if self.stop_time <= self.start_time:
            self.show_message_box(
                "Error", "Stop time must be greater than start time", "warning"
            )
            return

    def on_folder_button(self):
        """
        Handle the folder button click event.
        Open a file dialog to select the model executable and update the UI
        and logs with the selection.
        """
        self.exe_path, _ = QFileDialog.getOpenFileName(
            self, "Select Model "
        )
        # Extract the file name and update the UI and logs.
        if self.exe_path:
            file_name = os.path.basename(self.exe_path)
            self.working_directory = os.path.dirname(self.exe_path)
            self.ui.main_label.setText(f"Selected Model: {file_name}")
            logging.info("Selected Model: %s", file_name)
            logging.info("Model Path: %s", self.exe_path)

    def on_launch_button(self):
        """
        Handle the launch button click event.
        Validate inputs and execute the selected executable as a subprocess.
        """
        # Validate all necessary inputs and selections before launching.
        if not self.exe_path:
            self.show_message_box(
                "Error", FILE_DIALOG_TITLE, "warning"
            )
            return
        if not self.start_time or not self.stop_time:
            self.show_message_box(
                "Error", "Please enter a start and stop time", "warning"
            )
            return
        if self.stop_time <= self.start_time:
            self.show_message_box(
                "Error", "Stop time must be greater than start time", "warning"
            )
            return
        if not self.working_directory:
            self.show_message_box(
                "Error", FILE_DIALOG_TITLE, "warning"
            )
            return

        # Run the simulation executable as a subprocess.
        try:
            result = subprocess.run(
                [
                    self.exe_path,
                    f"-override=startTime={self.start_time},stopTime={self.stop_time}",
                ],
                cwd=self.working_directory,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            logging.error("Subprocess failed: %s", e.stderr)
            self.show_message_box("Error",
                                  "Simulation failed to run.",
                                  "critical"
                                  )
            return

        # Handle simulation results and show appropriate message.
        if result.stdout:
            if "LOG_SUCCESS" in result.stdout:
                logging.info("STDOUT:\n%s", result.stdout.strip())
                self.show_message_box(
                    "Simulation Status",
                    "Simulation successful. Check the log file.",
                    "info"
                )
            else:
                logging.error("STDOUT:\n%s", result.stdout.strip())
                logging.error(
                    "STDERR:\nModel may not have necessary dependent files "
                    "to run the simulation"
                )
                self.show_message_box(
                    "Simulation Status",
                    "Simulation failed. Check the log file.",
                    "critical"
                )
        else:
            logging.exception("An error occurred during simulation.")
            self.show_message_box(
                "Simulation Status", "An error occurred", "critical"
            )

    def text_changed_stop(self):
        """
        Handle the event when the stop time text field value is changed.
        Clear the stop time value if the field is empty.
        """
        if not self.ui.stop_line.text():
            self.stop_time = None

    def text_changed_start(self):
        """
        Handle the event when the start time text field value is changed.
        Clear the start time value if the field is empty.
        """
        if not self.ui.start_line.text():
            self.start_time = None

    @staticmethod
    def on_help_button():
        """
        Open the GitHub repository URL in the default web browser for help
        and additional information.
        """
        open_browser("https://github.com/mtm-x/OpenModelica-GUI")

    def on_info_button(self):
        """
        Show an informational message about the application and its purpose.
        """
        self.show_message_box(
            "Information",
            "This is a simple Modelica model launcher. It allows you to "
            "select a Modelica model and specify the start and stop times "
            "for the simulation. The simulation will run in the background, "
            "and you will be notified when it is done.",
            "info"
        )

    def clear(self):
        """
        Reset the UI and internal states, clearing model selection and
        associated variables.
        """
        self.ui.main_label.setText("Model : no model selected")
        self.working_directory = None
        self.exe_path = None
        logging.info("Model and working directory cleared")

    def show_message_box(self, title, message, icon_type):
        """
        Display a message box with the specified title, message, and icon type.

        :title: The title of the message box.
        :message: The message content to display.
        :icon_type: The type of icon to use ('info', 'warning', or 'critical').
        """
        if icon_type == "info":
            QMessageBox.information(self, title, message)
        elif icon_type == "warning":
            QMessageBox.warning(self, title, message)
        elif icon_type == "critical":
            QMessageBox.critical(self, title, message)


# Create and run the application.
app = QApplication([])
setup_logging()  # Set up application logging.
window = Launcher()
window.show()
app.exec()
