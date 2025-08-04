# Homework 1: Sets, Set Operations, and Testing with Pytest

In this assignment, you'll review mathematical set operations and learn how to write **unit tests** using `pytest`.

## 🧠 Learning Goals

- Understand and distinguish Python **modules** and **packages**
- Practice **set operations**: union, intersection, Cartesian product
- Identify and test **correct vs. incorrect implementations**
- Use **pytest** to write and run automated tests
- Run tests from the **command line** and **VS Code Testing Panel**

---

## 📁 Project Structure

```
homework1/
├── pyproject.toml
├── README.md
├── src/
│   └── setops.py
└── tests/
    └── test_setops.py
```

---

## ✅ Your Tasks

1. Examine the functions in `src/setops.py`
2. Read the provided test cases in `tests/test_setops.py`
3. Run the tests using both:
   - `pytest` in the **integrated terminal**
   - The **Testing panel** in VS Code

## 📥 1. Clone the Starter Repository
We've created a set of files that you will use for the rest of this project. The files are stored in a _git repository_. You've cloned a repository in Project 0. If you can't remember the steps, use your favorite LLM to clone the repository into `VSCode`. The basic steps are: click **Clone Repository**, paste your repo URL, and choose `CS236/` as the destination.


---

## 📁 2. Explore Project Structure

The root folder is the `CS236` directory you created earlier. Inside that folder is another folder named something like `homework1`. The precise name might vary, but you'll see the name `homework1` somewhere in the name. Inside the `homework1` folder are a handful of other files and folders. The general structure is given by

```
homework1/
├── pyproject.toml
├── README.md
├── src/
│   └── set_operations.py
└── tests/
    └── test_set_operations.py
```

The key files and folders are:

- **README.md** – this tutorial  
- **pyproject.toml** – configuration file that defines project metadata 
- **src/** - source directory containing the python module that defines various set operations
- **tests/** –  directory where you'll use unit tests to verify your code automatically


## 🧪 3. Set up your Python Environment with `venv`

Recall that a _virtual environment_ is a lightweight, local Python environment used to isolate project-specific packages from the default Python settings on your computer. Using a virtual environment prevents dependency conflicts and ensures that `pytest` behaves consistently across machines. The name of the virtual environment we will use is `venv`.

### 3.1 Deactivate Conda (if active)

We've learned that some prior classes have you install and automatically load an environment called `conda` so that the tools in those classes work. Deactivate `conda` by doing the following steps:

- Open the Integrated Terminal inside VSCode
  - **Menu**: _View → Terminal_  
  - **Shortcut**:  
    - Windows/Linux: ``Ctrl+` ``  
    - macOS: ``⌃` ``
- Look to see if you have a conda environment enstalled. Look at the line before the prompt in the terminal. If it starts with `(base)` or has some other environment indicator in parentheses `(myenv)`, then you need to do the next step.
- Deactive conda by typing

```bash
conda deactivate
```

You'll know you've been successful if the `(base)` part of the prompt will have disappeared.

### 3.2 Create a Virtual Environment 
You've done this before, but it's helpful to review the steps. Make sure you are in your `CS236/` directory. What you type next depends on what type of computer you are using and how it is configured. Usually, PCs install the latest version of Python so that you can execute it by typing `python`. Macs usually ship with an old version of python and the command `python` points to that old version. To overcome this, you run python by typing `python3`. Thus,

If on a PC then you should type 
```bash
python -m venv .venv
```
and if on a Mac or a computer configured to use Linux then you should type
```bash
python3 -m venv .venv
```
This creates a hidden directory called `.venv` in your project folder containing a standalone Python environment.

### 4.3 Activate the Virtual Environment
You now have to tell VSCode that you want to use the virtual environment. This is called _activating_ the environment. How you activate `venv` depends on your machine. 

For a Windows machine running PowerShell,
```powershell
venv\Scripts\Activate.ps1
```

and on a Mac or Linux-based machine
```bash
source .venv/bin/activate
```
If you are having trouble activating the virtual environment, ask an AI agent how to tell machine you are working on and ask for help.

You'll know that you've been successful if the name of the prompt changes and starts with `(.venv)`.

---

## 🚀 4 Install pytest

Open the Integrated Terminal in VSCode. Make sure the virtual environment is activated.

From the project root, run the following. On most PCs, 

```bash
pip install pytest     # if not already installed
```
On most Macs or Linux-based machines
```bash
pip3 install pytest     # if not already installed
```

---
## 5 Configure project
On most PCs, 
```bash
pip install --editable .
```

On most Macs and Linux-based machines
```bash
pip3 install --editable .
```

---
## 🚀 6 Run Tests from the Terminal

You’ll see which tests pass and which fail.

---

## 🧪 7 Running Tests in VS Code

## 🧠 How to Tell VS Code to Use the Correct Python Interpreter

If you installed packages like `pytest` in a virtual environment but VS Code still tries to use the system Python (e.g., `/usr/local/bin/python3`), follow these steps to make sure VS Code is using the correct interpreter.

---

### ✅ Step-by-Step: Set the Interpreter to Your Virtual Environment

1. **Open the Command Palette**

   - On macOS: `⌘ + Shift + P`  
   - On Windows/Linux: `Ctrl + Shift + P`

2. **Run the command:**

1. Open the project folder in VS Code
2. Click the **Testing** icon in the sidebar (flask icon)
3. If needed, open the Command Palette (`Ctrl+Shift+P` or `⌘+Shift+P`) and run:
   ```
   Python: Configure Tests → pytest → tests folder
   ```
4. Click ▶ next to each test to run them!

---

## 🎯 What You’ll Notice

- The `union` function is correct.
- The `intersection` and `cartesian_product` functions are **wrong** — your tests will expose this!
- Try fixing those functions and rerun the tests to verify your fixes.

---

Happy testing!
