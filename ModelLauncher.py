import logging
import os
import platform
import subprocess
import qdarktheme
import sys

from PyQt6.QtGui import QIcon, QIntValidator, QFontDatabase
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal

from src.gui import Ui_MainWindow
from src.logger import setup_logging
from src.result import run_simulation

FILE_DIALOG_TITLE = "Please Select Model Executable"


class Libloader(QThread):
    """
    A background thread to preload matplotlib and scipy.
    """
    loaded = pyqtSignal()

    def run(self):
        """
        Preload matplotlib and scipy to avoid delays.
        """
        from scipy.io import loadmat
        from matplotlib import pyplot as plt


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

        self.matplotlib_loader = Libloader()
        self.matplotlib_loader.start()  # Start the thread

        # Set window title and icon
        self.setWindowTitle("OpenModelica Model Launcher")
        self.setWindowIcon(QIcon(self.resource_path("res/pngs/OML1.ico")))
        qdarktheme.setup_theme("auto")
        self.ui.stackedWidget.setCurrentIndex(0)

        # Add application fonts
        QFontDatabase.addApplicationFont(
            self.resource_path("res/fonts/Montserrat-ExtraBold.ttf"))
        QFontDatabase.addApplicationFont(
            self.resource_path("res/fonts/Montserrat-Regular.ttf"))
        QFontDatabase.addApplicationFont(
            self.resource_path("res/fonts/Montserrat-SemiBold.ttf"))

        # Initialize variables
        self.working_directory = None
        self.exe_path = None
        self.start_time = None
        self.stop_time = None
        self.file_name = None
        self.change_theme = None

        # Connect UI buttons and fields to their respective event handlers
        self.ui.set_but.clicked.connect(self.on_set_button)
        self.ui.folder_but.clicked.connect(self.on_folder_button)
        self.ui.launch_but.clicked.connect(self.on_launch_button)
        self.ui.doc_but.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.history_but.clicked.connect(self.on_history_button)
        self.ui.start_line.textChanged.connect(self.text_changed_start)
        self.ui.home_but.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.theme_but.clicked.connect(self.theme_button)
        self.ui.theme_set_but.clicked.connect(self.theme_set_button)
        self.ui.stop_line.textChanged.connect(self.text_changed_stop)
        self.ui.clear_but.clicked.connect(self.clear)
        self.ui.clear_time_but.clicked.connect(self.clear_time)
        self.ui.launch_but.setEnabled(False)

        # Add input validators to restrict start/stop time to integers
        # within range 0-10000
        validator = QIntValidator(0, 10000, self)
        self.ui.start_line.setValidator(validator)
        self.ui.stop_line.setValidator(validator)

    def resource_path(self, relative_path):
        """Get the absolute path to a resource."""
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(
                sys._MEIPASS, relative_path)
        return os.path.join(
            os.path.abspath("."), relative_path)

    def theme_button(self):
        """
        Sets up the theme selection button functionality.

        This method updates the stack widget to show the theme selection
        interface, and then dynamically populates it with the
        available themes provided by the `qdarktheme` package.
        """
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(qdarktheme.get_themes())

    def theme_set_button(self):
        """
        Changes the current theme of the application according
        to the user's selection.
        """
        self.change_theme = self.ui.comboBox.currentText()
        qdarktheme.setup_theme(self.change_theme)

    def on_set_button(self):
        """
        Handle the set button click event. Validate and
        log the start and stop time values.
        """
        self.start_time = self.ui.start_line.text().strip()
        self.stop_time = self.ui.stop_line.text().strip()
        logging.info(
             "Start Time: %s, Stop Time: %s", self.start_time, self.stop_time
                    )
        self.ui.status_label.setText(
            f"Configured Start Time: {self.start_time}, Stop Time: {self.stop_time}")

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
        self.ui.status_label.setText("Launching Simulation...")

        # Run the simulation executable as a subprocess.
        try:
            if not os.path.isfile(self.exe_path):
                raise FileNotFoundError(
                    f"File not found: {self.exe_path}"
                )
            # Correct the handling of the arguments for 'mat'.
            self.ui.status_label.setText("Running Subprocess...")
            logging.info("Exporting results to output/result.mat")
            result = subprocess.run(
                [
                    self.exe_path,
                    f"-override=startTime={self.start_time},stopTime={self.stop_time}",
                    "-r=result.mat",
                ],
                cwd=self.working_directory,
                capture_output=True,
                text=True,
            )

        except FileNotFoundError as e:
            self.ui.status_label.setText(
                "Simulation failed. Check the log file...")
            logging.error("Status: File not found: %s", e.filename)
            self.show_message_box(
                "Error",
                f"File not found: {e.filename}",
                "critical"
            )
        except subprocess.CalledProcessError as e:
            self.ui.status_label.setText(
                "Simulation failed. Check the log file...")
            logging.error("Status: Subprocess failed: %s", e.stderr)
            self.show_message_box(
                "Error",
                "Simulation failed to run.",
                "critical"
            )
            return

        # Handle simulation results and show appropriate message.
        if result.stdout:
            if "LOG_SUCCESS" in result.stdout:
                self.ui.status_label.setText(
                    "Simulation successful. Check the log file...")
                logging.info("Status: Simulation successful.")
                logging.info("STDOUT:\n%s", result.stdout.strip())
                self.show_message_box(
                    "Simulation Status",
                    "Simulation successful. Check output directory...",
                    "info"
                )
                try:
                    if not os.path.exists("output"):
                        os.mkdir("output")

                    target_dir = os.path.join("output", self.file_name)
                    original_dir = target_dir
                    counter = 1

                    # Add a numeric suffix until a unique name is found
                    while os.path.exists(target_dir):
                        target_dir = f"{original_dir}_{counter}"
                        counter += 1

                    os.mkdir(target_dir)
                    os.rename(
                        f"{self.working_directory}/result.mat", os.path.join(
                            target_dir, "result.mat"))
                except Exception as e:
                    self.ui.status_label.setText(
                        "Simulation failed. Check the log file...")
                    logging.error("Status: Error creating output directory: %s", e)
                    self.show_message_box(
                        "Error",
                        "Error creating output directory.",
                        "critical"
                    )

            else:
                self.ui.status_label.setText(
                    "Simulation failed. Check the log file...")
                logging.error("Status: Simulation failed.")
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
            self.ui.status_label.setText(
                "Simulation failed. Check the log file...")
            logging.error("Status: Simulation failed.")
            logging.exception("An error occurred during simulation.")
            self.show_message_box(
                "Simulation Status", "An error occurred", "critical"
            )

        plot = self.ui.plot_check_but.isChecked()
        try:
            if plot:
                self.ui.status_label.setText("Showing the plots...")
                run_simulation(
                    os.path.join(target_dir, "result.mat"))

        except Exception as e:
            self.ui.status_label.setText("Cannot show the plots...")
            logging.error("Status: Error showing plots: %s", e)
            self.show_message_box(
                "Error",
                "Error showing plots. Please check the log file.",
                "critical"
            )
        self.ui.status_label.setText("Screening Task - OpenModelica GUI")

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

    def on_history_button(self):
        """
        Handles the event triggered by the History button,
        displaying log details in a list widget.
        If the log file exists, information regarding selected models,
        model paths, and statuses is extracted and
        displayed in the application.
        """
        self.ui.stackedWidget.setCurrentIndex(2)
        if os.path.exists("logs/OPLauncher.log"):
            self.ui.listWidget.clear()

            with open("logs/OPLauncher.log", 'r') as f:
                for line in f:

                    if "Selected Model:" in line:
                        line = line.split("Selected Model:")[1]
                        self.ui.listWidget.addItem("Executable: " + line)

                    if "Model Path:" in line:
                        model = line.split("Model Path:")
                        self.ui.listWidget.addItems(model)

                    if "Status:" in line:
                        status = line.split("Status:")[1]
                        self.ui.listWidget.addItem(
                            "Status: " + status)
                        self.ui.listWidget.addItem(
                            "-----------------------------------------------------------------------------------")

        else:
            self.ui.listWidget.addItem("No Logs Found")

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
        self.ui.status_label.setText("Model and working directory cleared")

    def clear_time(self):
        """
        Clear the start and stop time fields.
        """
        self.ui.start_line.clear()
        self.ui.stop_line.clear()
        self.start_time = None
        self.stop_time = None
        logging.info("Start and stop time cleared")
        self.ui.status_label.setText("Start and stop time cleared")

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
