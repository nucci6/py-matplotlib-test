# Matplotlib Testing for the RISE SW Stack

A successful execution of the following test will verify the installation and headless rendering capabilities of Matplotlib on the new RISE software stack. 

Two Python script is provided for testing:
*   `matplotlib_sanity.py` - tests Matplotlib's ability to operate on headless HPC compute nodes. It forces the non-interactive `Agg` backend, draws a figure containing both line and scatter plots, and verifies that the resulting image successfully exports to disk without requiring an X11 window display.

*Note: The official Matplotlib `pytest` suite is not used here, as the massive baseline image directory required for pixel-comparison testing is intentionally stripped from HPC installations to save disk space.*

Two Python scripts are provided for testing:
*   `my_test.py` - Runs the official, exhaustive NumPy test suite.

## Step 1: Environment Setup

We must first set up the environment by loading the appropriate modules and creating a virtual environment. 

*Note: As of this writing, the `py-matplotlib/3.10.7` module is missing several core runtime dependencies (like `packaging` and `kiwisolver`). We use the virtual environment to temporarily patch these missing dependencies so the library can run.*

**1. Load the required modules:**
```
# Clear existing modules
module purge

# Load the RISE software stack, NumPy, and Matplotlib
module use /storage/icds/sw8/modulefiles_rc2026/linux-rhel8-x86_64/Core
module load gcc
module load py-numpy
module load py-matplotlib/3.10.7
```

2. Create and activate a virtual environment:

```
python -m venv --system-site-packages ./mpl_test_env
source ./mpl_test_env/bin/activate
```

3. Install missing runtime dependencies:

```
pip install packaging contourpy cycler fonttools kiwisolver pillow pyparsing python-dateutil
```

## Step 2: Run the Core Sanity Check (matplotlib_sanity.py)

Because compute nodes do not have graphical displays, this script forces Matplotlib to use the Agg backend. It generates a figure containing a line plot and a scatter plot, and exports it directly to disk as a PNG file.

Run the test script:

```
python matplotlib_sanity.py 
```

Expected Output:

```
--- Matplotlib Sanity Check ---
Version: 3.10.7
Backend: Agg

1. Testing basic line plot and scatter plot...
2. Testing file export (PNG)...
   -> Success! Plot saved to matplotlib_test_output.png.

 Matplotlib 3.10.7 is installed and functioning correctly!
```

## Step 3: Cleanup

Once testing is complete, you can deactivate and remove the virtual environment, and delete the generated test image:

```
deactivate
rm -rf ~/mpl_test_env
rm matplotlib_test_output.png
```
