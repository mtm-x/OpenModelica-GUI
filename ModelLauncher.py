import logging
import os
import platform
import subprocess
import qdarktheme
from webbrowser import open as open_browser

from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from src.gui import Ui_MainWindow
from src.logger import setup_logging
#from src.result import run_simulation

FILE_DIALOG_TITLE = "Please Select Model Executable"


class Launcher(QMainWindow):
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title and icon
        self.setWindowTitle("OpenModelica Model Launcher")
        self.setWindowIcon(QIcon("res/OML1.ico"))
        qdarktheme.setup_theme("light")
        self.ui.stackedWidget.setCurrentIndex(0)

        # Initialize variables to hold user selections and input values
        self.working_directory = None
        self.exe_path = None
        self.start_time = None
        self.stop_time = None
        self.file_name = None

        # Connect UI buttons and fields to their respective event handlers
        self.ui.set_but.clicked.connect(self.on_set_button)
        self.ui.folder_but.clicked.connect(self.on_folder_button)
        self.ui.launch_but.clicked.connect(self.on_launch_button)
        self.ui.doc_but.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.info_but.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.start_line.textChanged.connect(self.text_changed_start)
        self.ui.home_but.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.theme_but.clicked.connect(self.theme)
        self.ui.git_but.clicked.connect(lambda: open_browser("https://github.com/mtm-x/OpenModelica-GUI"))
        self.ui.theme_set_but.clicked.connect(self.theme_set)
        self.ui.stop_line.textChanged.connect(self.text_changed_stop)
        self.ui.clear_but.clicked.connect(self.clear)
        self.ui.clear_time_but.clicked.connect(self.clear_time)
        self.ui.launch_but.setEnabled(False)

        # Add input validators to restrict start/stop time to integers
        # within range 0-10000
        validator = QIntValidator(0, 10000, self)
        self.ui.start_line.setValidator(validator)
        self.ui.stop_line.setValidator(validator)


    def theme(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(qdarktheme.get_themes())
        
    def theme_set(self):
        self.change_theme = self.ui.comboBox.currentText()
        qdarktheme.setup_theme(self.change_theme)

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
        if platform.system() == "Windows":
            self.exe_path, _ = QFileDialog.getOpenFileName(
                self, "Select Model ", "", "*.exe"
            )
        elif platform.system() == "Linux":
            self.exe_path, _ = QFileDialog.getOpenFileName(
                self, "Select Model "
            )
        # Extract the file name and update the UI and logs.
        if self.exe_path:
            self.ui.launch_but.setEnabled(True)
            self.file_name = os.path.basename(self.exe_path)
            self.working_directory = os.path.dirname(self.exe_path)
            self.ui.main_label.setText(f"Selected Model: {self.file_name}")
            logging.info("Selected Model: %s", self.file_name)
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
        mat = self.ui.mat_check_but.isChecked()
        # Run the simulation executable as a subprocess.
        try:
            if not os.path.isfile(self.exe_path):
                raise FileNotFoundError(
                    f"File not found: {self.exe_path}"
                )
            # Correct the handling of the arguments for 'mat'.
            if mat:
                logging.info("Exporting results to output/result.mat")
                result = subprocess.run(
                    [
                        self.exe_path,
                        f"-override=startTime={self.start_time},stopTime={self.stop_time}",
                        f"-r=output/result.mat",
                    ],
                    cwd=self.working_directory,
                    capture_output=True,
                    text=True,
                )

            else:

                result = subprocess.run(
                    [
                        self.exe_path,
                        f"-override=startTime={self.start_time},stopTime={self.stop_time}"
                    ],
                    cwd=self.working_directory,
                    capture_output=True,
                    text=True,
                )

        except FileNotFoundError as e:
            logging.error("File not found: %s", e.filename)
            self.show_message_box(
                "Error",
                f"File not found: {e.filename}",
                "critical"
            )
        except subprocess.CalledProcessError as e:
            logging.error("Subprocess failed: %s", e.stderr)
            self.show_message_box(
                "Error",
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
        #if mat :
            #run_simulation("Model/NonInteractingTanks.TwoConnectedTanks/TwoConnectedTanks_Win/output/result.mat")
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

    def on_doc_button(self):
        """
        Open the GitHub repository URL in the default web browser for help
        and additional information.
        """
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_info_button(self):
        """
        Show an informational message about the application and its purpose.
        """
        self.ui.stackedWidget.setCurrentIndex(2)

    def clear(self):
        """
        Reset the UI and internal states, clearing model selection and
        associated variables.
        """
        self.ui.main_label.setText("Model : no model selected")
        self.working_directory = None
        self.exe_path = None
        self.ui.launch_but.setEnabled(False)
        logging.info("Model and working directory cleared")

    def clear_time(self):
        """
        Clear the start and stop time fields.
        """
        self.ui.start_line.clear()
        self.ui.stop_line.clear()
        self.start_time = None
        self.stop_time = None
        logging.info("Start and stop time cleared")

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
