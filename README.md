
# 🚀 **OpenModelica Model Launcher (OML)** 

## 📚 **Contents**
- [ OpenModelica Model Launcher (OML)](#-openmodelica-model-launcher-oml-)
  - [Contents](#-contents)
- [ Overview](#-overview)

- [ Features](#-features)

- [ Getting Started](#-getting-started)
    - [Prerequisites](#-prerequisites)
    - [Installation](#-installation)
- [ Usage Instructions](#-usage-instructions)
    - [Step 1: Launching the Application](#-step-1-launching-the-application)
    - [Step 2: Setting up the Simulation](#-step-2-setting-up-the-simulation)
    - [Step 3: Running the Simulation](#-step-3-running-the-simulation)
    - [Step 4: Additional Help](#-step-4-additional-help)
- [ Example Workflow](#-example-workflow)

- [ Logging](#-logging)

- [ Screenshot](#-screenshot)

- [ Demo](#-demo)

---

## 🔍 Overview

The **OpenModelica Model Launcher (OML)** is a graphical user interface (**GUI**) application designed to simplify the execution of Modelica simulations. 
This launcher allows you to:
- Select Modelica model executables.
- Configure simulation parameters such as start time and stop time.
- Execute selected model in the background with proper logs and notifications on success or failure.

---

## ✨ Features
- **User-Friendly GUI**:
    - Simple design using PyQt6 for smooth user interaction.
    - Seamless integration of widgets for parameter configuration and model selection.

- **🌐 Platform Support**:
    - **Linux**
    - **Windows**

- **🎛️ Simulation Control**:
    - Configure simulation start and stop times.
    - Execute Modelica models using the specified parameters. 
    - Execution with real-time status updates.

- **⚠️ Error Handling and Notifications**:
    - Real-time feedback on simulation success or failure with detailed logs.
    - Display user-friendly error and status messages via popups.

- **📝 Logging**:
    - Detailed logging system for debugging and analysis (log files and console output).
    - Configurable logging to ensure ease of troubleshooting.

---

## 🚦 Getting Started

### 🔧 Prerequisites
The following software and dependencies must be installed on your system:
1. Python 3.12.0 or higher.
2. The following Python libraries installed using `pip`:
    - `PyQt6` (for GUI development)
    - `logging` (for logging functionality)
3. OpenModelica or any compatible Modelica simulation executable.

To install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   **or**
   ```bash
   pip3 install -r requirements.txt
   ```


### 🛠️ Installation
1. Clone this repository to your local system:
   ```bash
   git clone https://github.com/mtm-x/OpenModelica-GUI
   ``` 
   ```bash
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

## 📖 Usage Instructions

### ▶️ Step 1: Launching the Application
Run the script `ModelLauncher.py` using Python. The GUI for the OML will appear.

### ⚙️ Step 2: Setting up the Simulation
1. **Select Model File**: Click "Choose File" and browse for the Modelica model executable file.
2. **Set Start and Stop Time**:
    - Enter the start and stop times for your simulation in the respective fields.
    - Ensure that the stop time is greater than the start time.
3. **Validate Parameters**:
    - Once your parameters are set, click "Set" to validate the inputs.

### 🏃 Step 3: Running the Simulation
- Click the "Launch" button.
- The simulation will begin execution in the background with real-time progress tracking.
- Notifications will display success or failure results.

### ❓ Step 4: Additional Help
- Click the "Help" button to open the documentation.
- Use the "Info" button to access details about the application.

---

## 🛠️ Example Workflow
1. **Model Selection**: Choose a Modelica model executable (`*.exe`).
2. **Define Parameters**:
    - Enter values for:
        - Start Time: `0`
        - Stop Time: `5`
3. **Simulation Launch**:
    - Click "Launch" for execution.
    - Check logs and notification pop-ups for results.

---

## 📝 Logging
The application uses a centralized logging system to provide detailed analysis and debugging:
- Console output for real-time monitoring.
- Log files saved as `OPLauncher.log` for deeper diagnostics.

---

## 📷 Screenshot


![Screenshot 2025-01-17 135610](https://github.com/user-attachments/assets/4fd28547-0a5c-44b2-8f51-cd37fed7be02)

---
## 🎥 Demo




https://github.com/user-attachments/assets/863a8a87-e399-463b-b2a0-65427910b429





---

For additional questions, contact: `mahasel.1969@gmail.com`.
