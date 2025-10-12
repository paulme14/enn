# Setup and Installation

This section describes how to set up the Python environment needed for this course. You have several options to get started with Python for this course:

## Option 1: JupyterHub (Recommended for Beginners)
The easiest way to get started is using the University's JupyterHub:
- Access the JupyterHub platform with your university credentials
- All necessary packages are pre-installed
- No local setup required
- Ideal for getting started quickly

## Option 2: Local Installation
For a more flexible development environment, install Python locally on your computer.

### Conda Installation
We recommend using **conda** for package management:

1. **Install Miniconda** (minimal conda installer):
   - Download from [Miniconda.org](https://docs.conda.io/en/latest/miniconda.html)
   - Choose your operating system (Windows, macOS, or Linux)
   - Follow the installation instructions

2. **Create the course environment**:
   ```bash
   # Using the provided environment.yaml file
   conda env create -f environment.yaml
   conda activate ais-nn
   ```

# Verifying Your Installation

## Test Your Conda Installation
Open a new terminal (macOS/Linux) or Command Prompt (Windows) and verify conda is working:

```bash
conda --version
```

## Activate the Course Environment
**Important**: You must activate the course environment before using Python for this course:

```bash
# Activate the course environment (do this every time you start working)
conda activate ais-nn

# Now test Python and packages
python --version  # Should show Python 3.11 or later
python -c "import numpy, matplotlib, jupyter; print('All packages imported successfully!')"
```

> **💡 Remember**: You need to run `conda activate ais-nn` every time you open a new terminal to work on the course materials!
