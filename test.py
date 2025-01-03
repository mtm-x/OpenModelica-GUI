import os
import subprocess

# Get the base directory dynamically (script's location)
base_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative paths
relative_path_to_exe = "Model/NonInteractingTanks.TwoConnectedTanks/TwoConnectedTanks.exe"
relative_path_to_working_dir = "Model/NonInteractingTanks.TwoConnectedTanks"

# Construct absolute paths
exe_path = os.path.join(base_directory, relative_path_to_exe)
working_directory = os.path.join(base_directory, relative_path_to_working_dir)

# Check if the executable exists
if os.path.isfile(exe_path):
    print("Executable found at:", exe_path)
    
    # Run the executable
    command = [exe_path, "-override=startTime=0,stopTime=5"]
    result = subprocess.run(
        command,
        cwd=working_directory,  # Set the working directory
        capture_output=True,
        text=True
    )
    print("Output:", result.stdout)
    print("Errors:", result.stderr)
else:
    print("Executable not found at:", exe_path)
