"""The Python Package Installer"""
"""
pipinstaller/install_Functions.py
Copyright 2020 Misha Melnyk, Luke Zhang | MIT License
"""
import subprocess
import sys
import pathlib

packagesMissing = []
resPath = pathlib.Path("pipinstaller/resources")


def checkPip() -> bool:
    """Function to check pip install"""
    cmd = (
        "py -3 -m pip" if sys.platform == "win32" else "python3 -m pip"
    )  # This command will normally give options for
    # Arguments for the pip command but will output to stderr if the command is not found
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    for _ in process.stderr:
        return False
    return True  # Returns if whether it is installed or not


def checkPackage(pkg):
    """Function to check PIL install.

    pkg - a list of packages to check for\n
    returns boolean annotating if package is installed or not
    """
    try:
        _ = __import__(pkg[0])
    except ImportError:  # If the package in question is not installed, this import will raise an ImportError
        packagesMissing.append(pkg)
        return False
    print(pkg[0], "was found on the system")
    return True  # Returns if whether it is installed or not


def installPip(printOut=False):
    """Function to install pip.

    returns boolean annotating if an error was raised or not
    """
    cmd = (
        "py -3 pipinstaller\\resources\get-pip.py --user"
        if sys.platform == "win32"
        else "python3 pipinstaller/resources/get-pip.py --user"
    )
    # Runs the python script in resources and installs pip locally for the user
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if not printOut:  # Default Behaviour
        process.wait()
    else:
        while process.poll() is None:  # Keeps printing stdout until the process is done
            for line in process.stdout:
                print(line.decode(), end="")

    noError = True  # Assumes no errors have occurred
    for line in process.stderr:
        if line.lower().startswith(b"deprecation"):
            break
        print("Err: {}".format(line.decode()), end="")
        noError = (
            False  # If there are any items from stderr, then an error has occurred
        )

    if not noError:
        print("Something went wrong in installation, see information above.")
    return noError


def installPackage(pkg, printOut=False):
    """Function to install Package.
    
    pkg - package to be installed\n
    returns boolean annotating if an error was raised or not
    """
    cmd = (
        "py -3 -m pip install {} --user".format(pkg[1])
        if sys.platform == "win32"
        else "python3 -m pip install {} --user".format(pkg[1])
    )
    # Runs the pip command to install the Pillow (PIL) package from online
    # cmd = "py -3 -m pip install resources\Pillow-4.3.0-cp33-cp33m-win32.whl --user" if sys.platform == 'win32' else "python3 -m pip install Pillow"
    # Runs the pip command for the wheel file in resources
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if not printOut:  # Default Behaviour
        process.wait()
    else:
        while process.poll() is None:  # Keeps printing stdout until the process is done
            for line in process.stdout:
                print(line.decode(), end="")

    noError = True  # Assumes no errors have occurred
    for line in process.stderr:
        if line.lower().startswith(b"deprecation"):
            break
        print("Err: {}".format(line.decode()), end="")
        noError = (
            False  # If there are any items from stderr, then an error has occurred
        )

    if not noError:
        print("Something went wrong in installation, see information above.")
    # else:
    #     print(pkg[1],"was successfully installed")
    return noError


def installRequirements(path="pipinstaller/resources", printOut=False):
    """Installs via requirements.txt
    
    Pass in path to requirmenets\n
    returns boolean annotating if an error was raised or not
    """
    cmd = (
        f"py -3 -m pip install -r {path}/requirements.txt --user"
        if sys.platform == "win32"
        else f"python3 -m pip install -r {path}/requirements.txt --user"
    )

    # Runs the pip install -r requirements.txt
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if not printOut:  # Default Behaviour
        process.wait()
    else:
        while process.poll() is None:  # Keeps printing stdout until the process is done
            for line in process.stdout:
                print(line.decode(), end="")

    noError = True  # Assumes no errors have occurred
    for line in process.stderr:
        if line.lower().startswith(b"deprecation"):
            break
        print("Err: {}".format(line.decode()), end="")
        noError = (
            False  # If there are any items from stderr, then an error has occurred
        )

    if not noError:
        print("Something went wrong in installation, see information above.")
    # else:
    #     print(pkg[1],"was successfully installed")
    return noError
