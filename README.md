# Homework 1: Sets, Set Operations, and Testing with Pytest

In this assignment, you'll review mathematical set operations and learn how to write **unit tests** using `pytest`.

## 🧠 Learning Goals

- Understand Python **modules** and **packages**
- Practice **set operations**: union, intersection, Cartesian product
- Use **math** to construct and reason about test cases
- Write and categorize **three types of tests**:
  - ✅ Positive tests: what *should* happen
  - ❌ Negative tests: what *should not* happen
  - ⚠️ TypeError tests: when invalid input should raise an error
- Run tests from the **command line** and **VS Code Testing Panel**

---


## ✅ Your Tasks

1. Examine the functions in `src/set_operations.py`
2. Understand how the the provided test cases in `tests/test_set_operations_.py` relate to
   - definitions of mathematical set operations
   - type checks
3. Run the tests using both:
   - `pytest` in the **integrated terminal**
   - The **Testing panel** in VS Code

## 📥 1. Clone the Starter Repository
Clone the repository. If you can't remember the steps from Project0, use your favorite LLM to clone the repository into `VSCode`. The basic steps are: click **Clone Repository**, paste your repo URL, and choose `CS236/` as the destination.


---

## 📁 2. Explore Project Structure

The root folder is the `CS236` directory you created earlier. Inside that folder is another folder named something like `homework1`. The precise name might vary, but you'll see the name `homework1` somewhere in the name. Inside the `homework1` folder are a handful of other files and folders. The general structure is given by

```
homework1/
├── pyproject.toml
├── README.md
├── src/
│   └── homework1/
│       ├── __init__.py
│       └── set_operations.py
└── tests/
    └── test_set_operations.py
```

The key files and folders are:

- **README.md** – this tutorial  
- **pyproject.toml** – configuration file that defines project metadata 
- **src/** - source directory containing the python module that defines various set operations
- **src/homework1** - the folder for the `homework1` Python package
- **tests/** –  directory where you'll use unit tests to verify your code automatically


## 🧪 3. Set up your Python Environment with `venv`

Recall that a _virtual environment_ is a lightweight, local Python environment used to isolate project-specific packages from the default Python settings on your computer. Using a virtual environment prevents dependency conflicts and ensures that `pytest` behaves consistently across machines. The name of the virtual environment we will use is `venv`.

### 3.1 Deactivate Conda (if active)
If the prompt in the integrated terminal starts with `(base)` or has some other environment indicator in parentheses `(myenv)`, then deactive conda by typing

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
```bash
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

With the virtual environment activated, you'll install pytest. This will install a copy of pytest that is local to this project. When you run pytest, it will use this local copy, which should prevent weird things that can occur given the various ways in which Python can be installed on different computer systems.

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

You should now be set up to run the tests.

## 6. 📊 Command Line Unit Test Structure and Pytest: Union
Computer scientists distinguish between two types of tets:
- A **unit test** checks whether a _single, small part of the code_ (usually one function) works correctly in isolation.
- An **integration test** checks whether _multiple parts of the program work together_ as expected.

Many of you are probably used to thinking about testing in terms of integration tests because that is the kind of testing that has been done in your previous classes: does the code work right or not. In CS 236, project pass-offs will use a series of integration tests, but you'll also be required to write _unit tests_. 

It might seem like a pain to write unit tests, but there are three reasons to do so:
- The unit tests that you write will help you understand how the math we do in class relates to the functions you implement in the projects
- It is much easier to debug small pieces of code than entire programs. Since each project in the class builds on the previous project, you'll end up writing a larger program than many of you have written before, so testing small chunks of the program make sense
- It is easier to modify code when you write unit tests because running the unit tests will tell you whether any small change you make introduces a new error.

Our goal is to have you **write tests before you begin programming**, but we understand that some of you will be in "survivor mode" because of the demands of the semester and, consequently, will write the tests after you've written your code. Try your best.

### Overview
There are three types of unit tests that we'll consider in this class:
- a **positive test* provides evidence that the _code produces the correct result_ for valid input because the test is based on a known math fact or expected behavior 
- a **negative test** provides evidence that the _code does not produce an incorrect result_, and is used to detec logical errors or incorrect outcomes in your code
- a **type-checking test** confirms that a function you've written _raises the correct kind of error_ when given input of the wrong type, and is used to "enforce contracts" so that your code only operates on they kinds of inputs you expect

In this assignment, we'll write type-checking tests, but later in the class we'll use a tool called `mypy` that helps us do _static type checking_ so that we don't have to write so many tests.



### ✅ Positive Test
Suppose that we are given two sets $ A = \{1, 2\} $  and $ B = \{2, 3\} $. The union of two sets is the collection of all elements that are either in the first set or in the second or both. Thus,

$$
    A \cup B = \{1, 2, 3\}
$$ 
If we write a function called `union` that tries to implement the _union_ set operation then it should output the set $\{1,2,3\}$ if its inputs are set $A$ and set $B$. This is the basis of the positive test.

When you open up the file `tests\test_set_operations.py` you'll see the following function.

```python
def test_union_positive():
    # Function inputs
    A: set[int] = {1,2}
    B: set[int] = {2,3}

    # Expected output
    expected: set[int] = {1, 2, 3}
    
    # Assert that the union function works correctly
    assert union(A, B) == expected
```
Notice four things about the function.
1.  It's a function. Unit tests in the `pytest` framework are functions. When we run `pytest`, each function is run.
2. The input to the function are the two sets we chose, $A=\{1,2\}$ and $B=\{2,3\}$. 
3. We define the expected output based on the known behavior of the mathematical union operation, $A\cup B = \{1,2,3\}$
4. The `assert` statement in the code 
```python
assert union(A,B) == expected
```
checks whether the actual result of `union(A, B)` is equal to the expected result `{1, 2, 3}`. If the value returned by the function matches the expected result, **nothing happens**, which means that the test passes silently. If the value returned by the function does not match the expected result, Python raises an `AssertionError`, and the test fails. This will be captured by `pytest` and information about the failure will be given to us.


### ❌ Negative Test

A negative test checks that the function **does not** return an incorrect result. Let's make up something inccorect by defining $A=\{1\}$ and $B=\{1,2\}$, and then noting that
$$ A\cup B \neq \{1\}$$

```python
def test_union_negative():
    # Function inputs
    A: set[int] = {1}
    B: set[int] = {2}

    # Incorrect output
    incorrect_result: set[int] = {1,2}
    
    # Assert that the union function works does not work incorrectly
    assert union(A, B) != incorrect_result
```

Notice that the same pieces are in place, with the only difference is that we check to make sure that the output from the function **does not equal** the incorrect result. If the output does not equal the incorrect result, nothing happens with the `assert` statement and we fail silently. If the output does equal the incorrect result, then the `assert` statement raises an `ExceptionError`, and pytests helps us see the error.

Note that I chose this test to check whether I accidentally implemented the union as an intersection, since the intersection of A and B is 
$$A\cap B = \{1\}$$
This test was designed to detect a logical error.

### ⚠️ TypeError Test

This test checks that non-set input raises an error:

```python
def test_union_invalid_input_type_1():
    # one input is the wrong type
    A: str = "not a set"
    B: set[int] = {1,2}

    # Ask an LLM what is happening here
    with pytest.raises(TypeError):
        union(A, B)
```

Notice the completely different structure of the actual test. It does not use an ``assert`` statement. Instead, it has the structure 
```python
with pytest.raises(TypeError):
    union(A, B)
```
### 🤖 Prompt for Your Assistant

```text
What does 

    with pytest.raises(TypeError):
        union(A, B) 

do in the function 

    def test_union_invalid_input_type_1():
        # one input is the wrong type
        A: str = "not a set"
        B: set[int] = {1,2}

        with pytest.raises(TypeError):
        union(A, B)

How does the `with` statement work?
What does it mean to call the function `pytest.raises`?
What is a `TypeError`?
```

Tests for `union` in `tests\test_set_operations.py` also include a test on whether the second input is a set as well as a test on whether one of the elements of the set is not a integer.

---
## 🚀 6 Run Tests from the Terminal

From the integrated terminal in VSCode, type
```bash
pytest
```
You'll be given a list of which tests fail. Notice that none of the tests involving union appear in the terminal. That's because they all pass. Only tests that fail appear in the output when we run `pytest` from the command line. All successful tests pass silently.

---

## 🧪 7 Running Tests in VS Code
Once you’ve written your tests and configured `pytest`, you can run and debug them directly in VS Code. The first thing to do is tell VSCode that you are using the version of Python from the virtual environement.

### 🧠 Tell VS Code to Use the Correct Python Interpreter

If you installed packages like `pytest` in a virtual environment but VS Code still tries to use the system Python (e.g., `/usr/local/bin/python3`), follow these steps to make sure VS Code is using the correct interpreter.

### ✅ Step-by-Step: Run Your Tests

1. **Open the Testing Panel**  
   Click the beaker icon in the sidebar to open the **Testing panel**.

2. **Configure VS Code for pytest (if needed)**  
   - Open Command Palette (`Ctrl+Shift+P` or `⌘+Shift+P`)
   - Run: `Python: Configure Tests`
   - Select `pytest`
   - Set the test folder to `tests/`

3. **Discover and View Your Tests**  
   You should now see a list of test functions from `test_set_operations.py`. Each function has:
   - A green ▶ to run it
   - A red ❌ or green ✔ to indicate pass/fail status

---

### ❌ Understanding Failing Tests: Example with Intersection

In this assignment, the `intersection` function is implemented incorrectly — it returns the **union** instead. Here's what happens:

#### Test that fails (but should pass)

```python
def test_intersection_positive():
    A = {1, 2}
    B = {2, 3}
    expected = {2}
    assert intersection(A, B) == expected
```

**Math says:**
$$ A \cap B = \{2\} $$  
But if `intersection()` is implemented as a union, it returns:
$$ A \cup B = \{1, 2, 3\} $$  
So the test fails because:
```python
{1, 2, 3} != {2}
```

---

#### Test that fails (but should not)

```python
def test_intersection_negative():
    A = {1}
    B = {2}
    incorrect_result = {1, 2}
    assert intersection(A, B) != incorrect_result
```

**Math says:**
$$ A \cap B = \emptyset $$  
But the incorrect implementation gives:
$$ A \cup B = \{1, 2\} $$  
So the test **fails again**, because the function returns the incorrect result the test was trying to catch.

---

### ⚠️ Type-Checking Tests Still Pass

The **TypeError tests** will still pass as long as your function checks that:
- Both inputs are sets
- All elements are integers

These tests are valuable because they help catch mistakes **even when other logic is broken**.

---

### 🧠 What to Take Away

- The **positive test** failed because the implementation did the wrong thing.
- The **negative test** failed because the implementation did exactly the wrong thing.
- The **type-checking tests** passed because they test input validation, not math.

This is how unit testing helps you **discover logical errors** and diagnose **where** something went wrong — and why your tests need to reflect solid **mathematical reasoning**.

---

💡 Tip: You can click the ❌ next to a failed test in the Testing panel to jump to the failing line and inspect the actual vs expected output.

---

### Fix the implementation for the intersection function
Fix the code that causes the intersection function to fail the tests. Rerun the test to see if the tests now pass. 

## 🔍 What to Look for in the Cartesian Product Tests

In this section, you’ll analyze **two incorrect implementations** of the Cartesian product function. The corresponding tests are designed to help you **discover and explain the errors** based on your mathematical understanding.

---

### ❌ Version 1: Repeats `a` Instead of Using `b`

```python
return {(x, y) for x in a for y in a}
```

**What’s wrong?**  
This version loops over `a` twice, producing \( A \times A \) instead of \( A \times B \).

**Test coverage:**

- ✅ **Positive test** fails because the output is missing combinations with elements from `B`.
- ❌ **Negative test** helps confirm that incorrect logic is producing false positives (e.g., `(1, 1)` instead of `(1, 2)`).
- ⚠️ **TypeError tests** verify that the function properly rejects non-set inputs.
- 📏 **Output type test** confirms the function returns a set of tuples of length 2 — even though they’re the wrong tuples!

---

### ❌ Version 2: Returns a Set of Sets Instead of Tuples

**What’s wrong?**  
This version does not return tuples; it returns sets inside the set — which are **not hashable** and will cause a runtime `TypeError`.

But if you rewrote it to force return of sets, the output would be structurally wrong even if no error is raised.

**Test coverage:**

- ✅ **Positive test** will fail because `{(1, 'a')}` ≠ `{{1, 'a'}}`
- ❌ **Negative test** reveals that incorrect structure leads to the wrong result
- ⚠️ **TypeError tests** check for bad input types
- 📏 **Output type test** checks that the result is:
  - A `set`
  - Of `tuples`
  - Of the correct length

This last test helps **detect structural errors**, even if the values happen to look right.

---

### 🧠 What You’re Practicing

- Using **math** to identify what should be in the Cartesian product:
  \[
  A \times B = \{ (a, b) \mid a \in A, b \in B \}
  \]
- Writing **positive tests** that assert correct output
- Writing **negative tests** to catch subtle bugs
- Writing **type-checking and structure-checking tests** to enforce data format expectations

---

### Fix the errors in the Cartesian Products
