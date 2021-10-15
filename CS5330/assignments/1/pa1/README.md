# CS 5330: Assignment-1

Welcome to the CS 5330 Assignment-1! 

##Getting Started

### Install Anaconda

#### Graphical Install (Windows/macOS)

If you are more familiar with graphical user interface, simply download the installer through this [link](https://www.anaconda.com/products/individual) and follow the instructions.

#### Command-line install (Linux/macOS)

Use this method if you prefer to use a terminal window.

1. In your browser, download the [Anaconda installer for Linux](https://www.anaconda.com/download/#linux) or [Anaconda installer for macOS](https://www.anaconda.com/downloads#macos).

2. Open a terminal and run the following:

   + For Python 3.7

     ```sh
     bash ~/Downloads/Anaconda3-2020.02-<Linux or MacOS>-x86_64.sh
     ```

   + For Python 2.7

     ```sh
     bash ~/Downloads/Anaconda2-2019.10-<Linux or MacOS>-x86_64.sh
     ```

   + Note: be sure to enter the write installer name.

3. Follow the instructions in the terminal.

### Create a Clean Conda Environment

To make life easier, you'd better create a new clean conda environment for this course or even for each assignment.

####HowTo

Use the terminal or an Anaconda Prompt for the following steps:

1. To create an environment:

   ```sh
   conda create --name myenv
   ```

   You can replace `myenv` with any name you like.

2. When conda asks you to proceed, type `y`:

   ```sh
   proceed ([y]/n)?
   ```

3. To create an environment with a specific version of Python:

   ```sh
   conda create -n myenv python=3.6
   ```

   This step is not a must. If you do not specify a Python version, the conda will install the latest Python version in `myenv`.

4. Activate the new environment:

   ```sh
   conda activate myenv
   ```

Note: Please refer this [document](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) for more information. 

###Install Dependency

We only need the following four packages for this assignment.

1. `matplotlib`
2. `opencv-python`
3. `numpy`
4. `jupyter`

For `numpy` and `jupyter`, they will be installed automatically in your conda environment. Following the next two command to install `matplotlib` and `opencv-python`.

```sh
conda install -c conda-forge matplotlib
conda install -c conda-forge opencv
```



### Begin to Code

Use the terminal or an Anaconda Prompt for the following steps:

1. Under the environment you just created.

   ```sh
   jupyter notebook
   ```

2. Open the `pa1.ipynb` and follow the instructions.

3. Submit your finished Jupyter notebook `pa1.ipynb`.

## Useful Links

1. [CONDA documents](https://docs.anaconda.com/anaconda/): If you have no experience with Anaconda, do read Anaconda's official documents to get started. 
2. [CONDA CHEAT SHEET](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf): If you have some experience with Anaconda, feel free to refer it to find the command you need.

