# Learning Goals

By the end of this Python introduction, we will have covered the following:

* **Setup a Python software development environment** using JupyterHub or Miniconda
* **Write Python code** knowing the basic syntax
* **Use Jupyter notebooks** for interactive coding sessions
* **Perform data processing** using [NumPy](https://numpy.org/)
* **Perform data visualization** using [Matplotlib](https://matplotlib.org/)

## Additional Resources

This week covers Data Science fundamentals, but you can continue learning with these resources:

### Python Resources
- [Python 3.11+ Documentation](https://docs.python.org/3/) - Comprehensive official documentation
- [Python Tutorial](https://docs.python.org/3/tutorial/) - Official beginner-friendly tutorial

### NumPy Resources
- [NumPy Official Documentation](https://numpy.org/doc/stable/) - Complete NumPy reference
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html) - Essential NumPy basics
- [NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) - Step-by-step introduction
- [NumPy Cheat Sheet (PDF)](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf) - Quick reference

### Matplotlib Resources
- [Matplotlib Official Documentation](https://matplotlib.org/stable/contents.html) - Complete Matplotlib reference
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html) - Comprehensive tutorials
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Example plots with code
- [Matplotlib Cheat Sheets](https://matplotlib.org/cheatsheets/) - Quick reference guides

</br>
</br>
</br>

# Setup and Installation

This section describes how to set up the Python environment needed for this course.

## Python Environment Options

You have several options to get started with Python for this course:

### Option 1: JupyterHub (Recommended for Beginners)
The easiest way to get started is using the University's JupyterHub:
- Access the JupyterHub platform with your university credentials
- All necessary packages are pre-installed
- No local setup required
- Ideal for getting started quickly

### Option 2: Local Installation
For a more flexible development environment, install Python locally on your computer.

#### Conda Installation
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

## Verifying Your Installation

### Test Your Conda Installation
Open a new terminal (macOS/Linux) or Command Prompt (Windows) and verify conda is working:

```bash
conda --version
```

### Activate the Course Environment
**Important**: You must activate the course environment before using Python for this course:

```bash
# Activate the course environment (do this every time you start working)
conda activate ais-nn

# Now test Python and packages
python --version  # Should show Python 3.11 or later
python -c "import numpy, matplotlib, jupyter; print('All packages imported successfully!')"
```

> **💡 Remember**: You need to run `conda activate ais-nn` every time you open a new terminal to work on the course materials!

</br>
</br>
</br>

# Further Information

## Getting the Materials
The course materials are organized in this repository. We will update the content according to the lecture schedule.

## During the Course
- Ask questions during sessions
- Use the course discussion forum [Mattermost](https://mattermost.uni-muenster.de/signup_user_complete/?id=egospupx5pd7jdjwzsg3zkfish&md=link&sbr=su)
- Work with your peers in study groups

## Online Resources
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - Community Q&A
- [Python.org Community](https://www.python.org/community/) - Official community resources
- [Real Python](https://realpython.com/) - High-quality Python tutorials

</br>
</br>
</br>

# Attributions

This course material builds upon:
- Snoek, L. (2021). introPy (Version 0.2.0) [Computer software]. https://doi.org/10.5281/zenodo.4392860