import logging


def run_simulation(file_path):
    """
    Run the simulation using the data from the .mat file and plot the results.
    It expects the .mat file to contain two variables: data_1 and data_2.
    2D arrays are expected for both variables.
    This script is made to the result generated from TwoConnectedTanks Model
    """
    from scipy.io import loadmat
    from matplotlib import pyplot as plt
    # Load the .mat file
    try:
        data = loadmat(file_path)
    except Exception as e:
        logging.error("Error reading the .mat file: %s", e)
        return

    # Check if the file contains any data
    if not data:
        logging.warning("The .mat file is empty or could not be loaded!")
        return

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot for data_1
    if "data_1" in data:
        x = data["data_1"][:, 0]  # First  - since the data_1 returns 2d array
        y = data["data_1"][:, 1]  # Second column
        axes[0].plot(x, y, marker="o")
        axes[0].set_xlabel("X-axis")
        axes[0].set_ylabel("Y-axis")
        axes[0].set_title("Plot of data_1")
        axes[0].grid()
    else:
        logging.warning("data_1 not found in the .mat file.")
        axes[0].set_title("data_1 not found")

    # Plot for data_2
    if "data_2" in data:
        x = data["data_2"][:, 0]  # First column
        y = data["data_2"][:, 1]  # Second column
        axes[1].plot(x, y, marker="o")
        axes[1].set_xlabel("X-axis")
        axes[1].set_ylabel("Y-axis")
        axes[1].set_title("Plot of data_2")
        axes[1].grid()
    else:
        logging.warning("data_2 not found in the .mat file.")
        axes[1].set_title("data_2 not found")

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()
