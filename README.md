# Open Modelica Model Launcher (OMML)

## Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage Instructions](#usage-instructions)
    - [Step 1: Launching the Application](#step-1-launching-the-application)
    - [Step 2: Setting up the Simulation](#step-2-setting-up-the-simulation)
    - [Step 3: Running the Simulation](#step-3-running-the-simulation)
    - [Step 4: Additional Help](#step-4-additional-help)
- [Example Workflow](#example-workflow)
- [Logging](#logging)
- [Screenshot](#screenshot)
- [Demostration](#demo)
- [User Experience](#user-experience)

---

## Overview
The **Open Modelica Model Launcher (OMML)** is a graphical user interface (GUI) application designed to simplify the execution of Modelica simulations. Leveraging its user-friendly interface, OMML enables developers to set up, configure, and launch Modelica-based simulations seamlessly.

This launcher allows you to:
- Select Modelica model executables.
- Configure simulation parameters such as start time and stop time.
- Execute simulations in the background with proper logs and notifications on success or failure.

OMML is designed to enhance usability and streamline the simulation process, providing real-time feedback to ensure an efficient workflow.

---

## Features
- **User-Friendly GUI**:
    - Intuitive design using PySide6 for smooth user interaction.
    - Seamless integration of widgets for parameter configuration and model selection.

- **Simulation Control**:
    - Configure simulation start and stop times.
    - Execute Modelica simulations using the specified parameters.
    - Asynchronous execution with real-time status updates.

- **Error Handling and Notifications**:
    - Real-time feedback on simulation success or failure with detailed logs.
    - Display user-friendly error and status messages via popups.

- **Logging**:
    - Detailed logging system for debugging and analysis (log files and console output).
    - Configurable logging to ensure ease of troubleshooting.

---

## Getting Started

### Prerequisites
The following software and dependencies must be installed on your system:
1. Python 3.12.0 or higher.
2. The following Python libraries installed using `pip`:
    - `PySide6` (for GUI development)
    - `logging` (for logging functionality)
3. OpenModelica or any compatible Modelica simulation executable.

To install the required Python packages:
   ```bash
   pip install PySide6 logging
   ```

### Installation
1. Clone this repository to your local system:
   ```bash
   git clone https://github.com/mtm-x/OpenModelica-GUI
   cd OpenModelica-GUI
   ```
2. Run the application:
   ```bash
   python ModelLauncher.py
   ```
   or
   ```bash
   python3 ModelLauncher.py
   ```

---

## Usage Instructions

### Step 1: Launching the Application
Run the script `ModelLauncher.py` using Python. The GUI for the OMML will appear.

### Step 2: Setting up the Simulation
1. **Select Model File**: Click "Choose File" and browse for the Modelica model executable file.
2. **Set Start and Stop Time**:
    - Enter the start and stop times for your simulation in the respective fields.
    - Ensure that the stop time is greater than the start time.
3. **Validate Parameters**:
    - Once your parameters are set, click "Set" to validate the inputs.

### Step 3: Running the Simulation
- Click the "Launch" button.
- The simulation will begin execution in the background with real-time progress tracking.
- Notifications will display success or failure results.

### Step 4: Additional Help
- Click the "Help" button to open the documentation or visit [GitHub Documentation](https://github.com/mtm-x/OpenModelica-GUI).
- Use the "Info" button to access details about the application.

---

## Example Workflow
1. **Model Selection**: Choose a Modelica model executable (`*.exe`).
2. **Define Parameters**:
    - Enter values for:
        - Start Time: `0`
        - Stop Time: `5`
3. **Simulation Launch**:
    - Click "Launch" for execution.
    - Check logs and notification pop-ups for results.

---

## Logging
The application uses a centralized logging system to provide detailed analysis and debugging:
- Console output for real-time monitoring.
- Log files saved as `OPLauncher.log` for deeper diagnostics.

---

## Screenshot
![Screenshot_20250105_164346](https://github.com/user-attachments/assets/d124cbd5-ec96-4115-9644-708734b5fe12)

---
## Demo


https://github.com/user-attachments/assets/305b5387-b8da-42b6-8a65-dfef2e0250cc


---
## User Experience
The OMML provides a smooth and efficient user experience by:
- Simplifying simulation configuration.
- Supporting asynchronous operations to prevent freezing of the UI during execution.
- Providing intuitive feedback and instructions for ease of use.

---

For additional questions, contact: `mahasel.1969@gmail.com`.
