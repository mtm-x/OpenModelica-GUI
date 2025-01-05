# OpenModelica Model Launcher

This project is a Qt-based graphical user interface (GUI) application built with PySide6 and Python. It helps you launch models compiled from OpenModelica, allowing you to set custom start and stop times instead of relying on default parameters. The interface remains simple for all users, providing intuitive controls to organize tasks and configure simulations.

---

## Installation Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/mtm-x/OpenModelica-GUI
    ```
2. Navigate to the project directory:
    ```bash
    cd OpenModelica-GUI
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the application:
    ```bash
    python ModelLauncher.py  
    ```
   or
   ```bash
    python3 ModelLauncher.py 
    ```
2. Select openmodelica model (complied executable file from openmodelica). 
3. Give simulation start and stop times.

---

## Features

- Launch OpenModelica models with custom start/stop times
- Enhanced UI Controls
- Override the default simulation start and stop times to meet your specific needs.


---

## Acknowledgments

- [PySide6](https://doc.qt.io/qtforpython-6/)
- [OpenModelica](https://openmodelica.org/)
