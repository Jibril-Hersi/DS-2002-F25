# Welcome to DS-2002 macOS User Setup Guide!

If you are a macOs User, you are in the right place! If you are a Windows user, please click [here](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/Windows_Users.md) to follow the Windows User Setup Guide.

In this Setup Guide, you will find easy to navigate instructions for downloading and installing the tools you will need this semester:
- Environments ⛰️
- Languages 🗣️
- Packages 📦
- Tools 🛠️
- Etc. 🤷‍♀️

<br>

# Early Semester Must Haves

## Terminal 💻
The **Terminal** (or `Terminal.app` on macOS) is the default command-line interface (CLI) for macOS. It provides a Unix-like environment that allows users to interact directly with the operating system using commands. The Terminal is important because it's the standard tool for developers, system administrators, and data scientists to manage files, run scripts, and automate tasks. Since macOS is built on a Unix foundation, the Terminal is a native and powerful tool that doesn't require any special emulation.

Please follow these steps and read each step carefully:
1. You're done! It comes with your Mac by default!

<br>

## Homebrew 🍺
**Homebrew** is a package manager for macOS. It simplifies the process of installing software that isn't included with macOS by default, such as `jq`, `make`, and other command-line tools. Homebrew is important because it provides a centralized and reliable way to install and manage these applications without needing to download them manually or deal with complex installation processes. It's often referred to as "the missing package manager for macOS."

Please follow these steps and read each step carefully:
1. Open the **Terminal** application.
2. Copy and paste the following command and press Enter:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. The script will prompt you to confirm the installation and may ask for your administrator password. Follow the on-screen instructions.

<br>

---

# Python, Packages, and Libraries

## Python - Programming Language 🐍
Python is a high-level, general-purpose programming language that is widely used for a variety of tasks, from web development to data science and automation. Its design emphasizes code readability and a simple, clean syntax. It's often called a "glue language" because it can easily integrate with components written in other languages, which is why it's a great tool for building pipelines with Bash.

Due to its extensive standard library and many third-party packages, Python is an incredibly versatile language. It also handles complex data structures like dictionaries and lists with ease, making it a popular choice for data-related tasks.

### Check if you have Python installed for your environment
1. Open Git Bash and run:
```
python3 --version
```
  - If a version number like `Python 3.10.6` is displayed, Python 3 is already installed. You are all set for Python!
  - If you get a `command not found` error, you need to install Python following the instructions below.

### Install Python
macOS users should use Homebrew to manage your Python installation.
1. **Install Python**: If `python3 --version` failed, you need to run the following command in your Git Bash terminal. This will install the latest version of Python and include pip.
```
brew install python3
```
  - **Explanation**: The `brew` command uses Homebrew, a popular package manager for macOS, to automatically download and install Python for you. It handles the details of adding Python to the system's PATH, which is a common source of errors.

2. **Verify the Installation**: Close and reopen the Git Bash terminal. This is a crucial step to ensure the changes to the system's PATH are recognized. Once the terminal is restarted, run the check for Python again:
```
python3 --version
```
3. Verify PIP was also installed:
```
pip3 --version
```
  - Similar to Python, you should see either a version number or an error. If you see a version number, you are all set!
4. If you are getting an error that PIP does not exist, and you have confirmed you have Python installed properly, run the following to manually download PIP.
```
python3 -m ensurepip
```
  - For more information on PIP, see below!

<br>

## PIP - Package Management System

PIP stands for "Pip Installs Packages". It is a recursive acronym, which means that the acronym itself is part of its definition. PIP is a package management system used to install and manage software packages written in Python.

### Key Principles of PIP
PIP connects to an online repository of public packages called the Python Package Index (PyPI). It can also be configured to connect to other package repositories, both local and remote, provided they comply with Python Enhancement Proposal 503. PIP is included by default in Python versions 3.4 and later, as well as Python 2.7.9 and later.

PIP is an essential tool for Python developers as it simplifies the process of managing dependencies and packages. It is recommended by the Python Software Foundation for installing Python applications and their dependencies. By understanding and utilizing PIP, developers can efficiently manage their Python environments and ensure that their projects have all the necessary dependencies.

### Why do I need both Homebrew and PIP?
You need both a system-level package manager like `Homebrew` and a language-specific one like `pip` because they serve different purposes.

`Homebrew` manages applications and tools at the operating system level. They install software like web browsers, text editors, development tools (like Git), and the Python interpreter itself. Think of them as a universal app store for your computer.

`Pip` is specific to Python. Its sole job is to install, manage, and remove Python libraries and packages. These are code modules that your Python scripts use, such as `requests` for making web calls or `pandas` for data analysis.

It's good to have both because they specialize in different layers of your system. You use `Homebrew` to install the foundation (Python), and you use `pip` to install the building blocks (libraries) that your Python code needs to run.

### PIP Usage
PIP is used through the command line interface. Here are some common commands:
- Install a package:
```
pip install package-name
```

- Uninstall a package:
```
pip uninstall package-name
```

- Install packages from a requirements file:
```
pip install -r requirements.txt
```

- List installed packages:
```
pip list
```

### Example
To install a package named `requests`, you would use the following command:
```
pip install requests
```
After installation, you can use the package in your Python code:
```
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
```
