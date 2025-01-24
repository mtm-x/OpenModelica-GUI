
# 🚀 **OpenModelica Model Launcher (OML)** 

## 📚 **Contents**
- [ OpenModelica Model Launcher (OML)](#-openmodelica-model-launcher-oml)
  - [Contents](#-contents)
- [ Overview](#-overview)

- [ Features](#-features)

- [ Getting Started](#-getting-started)
    - [Prerequisites](#-prerequisites)
    - [Installation](#️-installation)

- [ Usage Instructions](#-usage-instructions)

- [ Example Workflow](#️-example-workflow)

- [ Logging](#-logging)

- [ Screenshot](#-screenshot)

- [ Demo](#-demo)

---

## 🔍 Overview

The **OpenModelica Model Launcher (OML)** is a graphical user interface (**GUI**) application designed to simplify the execution of Modelica simulations. 
This launcher allows you to:
- Select Modelica model executables.
- Configure simulation parameters such as start time and stop time.
- Execute the selected model and generate output files in `.mat` format.
- Visualize the simulation results using Matplotlib for detailed analysis.

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
    - Plot the model output when the "Plot the Output" button is        pressed.
    - Receive real-time status updates during execution.

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
    - `matplotlib` (for plotting results)
    - `scipy` (for handling .mat files)
    - `qdarktheme` (for dark theme support)
3. OpenModelica simulation executable.

To install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   **or**
   ```bash
   pip3 install -r requirements.txt
   ```

---

### 🛠️ Installation
### Installation via Executables

1. **Download the Executable:**
   - Navigate to the [Releases](https://github.com/mtm-x/OpenModelica-GUI/releases/tag/v1.0.0) section of this repository.
   - Find the latest version and download the appropriate executable file for your operating system (e.g., `.exe` for Windows or a binary for Linux/Mac).

2. **Run the Executable:**
   - For **Windows**:
     - Double-click the `.exe` file to launch the application.
   - For **Linux**:
     - Open a terminal in the directory containing the executable.
     - Run the file using:  
       ```bash
       ./ModelLauncher_Lin_V1.0.0
       ```
---

### Installation via GitHub
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
Run the script `ModelLauncher.py` using Python or launch the application.

### ⚙️ Step 2: Setting up the Simulation
1. **Select Model File**: Click "Choose File" and browse for the Modelica model executable file.
2. **Set Start and Stop Time**:
    - Enter the start and stop times for your simulation in the respective fields.
    - Ensure that the stop time is greater than the start time.
3. **Validate Parameters**:
    - Once your parameters are set, click "Set" to validate the inputs.

### 🏃 Step 3: Running the Simulation
- To generate a plot, ensure you check the "Plot the O/p" button before launching.
- Click the "Launch" button to start the simulation.
- The simulation will execute in the background with real-time progress tracking.
- Notifications will display the results, indicating success or failure.

### ❓ Step 4: Additional Help
- Click the "History" button to view recent simulation logs.
- Use the "Docs" button to access detailed information about the application and relevant links.
---

## 🛠️ Example Workflow
1. **Model Selection**: Choose a Modelica model executable (`*.exe` for Windows).
2. **Define Parameters**:
    - Enter values for:
        - Start Time: `0`
        - Stop Time: `5`
3. **Simulation Launch**:
    - Check the "Plot the O/p" option if you need to generate plots.
    - Click "Launch" to start the execution.
    - Check logs and notification pop-ups for results.
---

## 📝 Logging
The application uses a centralized logging system to provide detailed analysis and debugging:
- Console output for real-time monitoring.
- Recent simulation data can be viewed using the "History" button.
- Log files are saved as `OPLauncher.log` for deeper diagnostics.
---

## 📷 Screenshot
1. Home screen
   
![Screenshot 2025-01-23 221824](https://github.com/user-attachments/assets/2d4fbbaa-12f1-4849-b9d7-09d38e61bd00)

2. Themes
 
![Screenshot 2025-01-23 221847](https://github.com/user-attachments/assets/1fbaf38f-094f-4676-b7bc-1740814b85a6)

3. Log History

![Screenshot 2025-01-23 221901](https://github.com/user-attachments/assets/71e153a4-5371-4677-bbba-4534881685d8)

4. Docs

![Screenshot 2025-01-23 222606](https://github.com/user-attachments/assets/1084ce31-2c2c-4b79-9c87-e51d7a76464e)

5. Plot

![Screenshot 2025-01-23 224410](https://github.com/user-attachments/assets/a2c886a2-0ad7-4937-9dec-ae17dcf85c37)


---
## 🎥 Demo




https://github.com/user-attachments/assets/937f8298-f274-42ce-b769-a867979abcb3





---

For additional questions, contact: `mahasel.1969@gmail.com`.
