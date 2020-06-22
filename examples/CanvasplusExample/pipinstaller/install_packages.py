"""The Python Package Installer"""
"""
Copyright 2020 Misha Melnyk, Luke Zhang | MIT License
"""

from pipinstaller.install_Functions import (
    checkPip,
    installPip,
    checkPackage,
    installPackage,
    packagesMissing,
    installRequirements,
)
import sys

targetPackages = [
    # ["PIL", "Pillow"]
]


def install(pathToRequirements="pipinstaller/resources", auto=False):
    """Installs the specified packages\n
    Leave this blank if you are using targetPackages, or if your requirements.txt matches this path
    """
    global targetPackages

    acceptAll = (
        "-y" in sys.argv or auto
    )  # Checks if the -y parameter is passed in. Will ignore [y/n] queries if it is

    pipInstalled = checkPip()

    ###################################################################################################
    if len(targetPackages) == 0:
        suffix = "/" if pathToRequirements[-1] != "/" else ""
        try:
            open(
                f"{pathToRequirements}{suffix}requirements.txt"
            )  # Check for a requirements.txt file

            if acceptAll:
                doFullLog = True
            else:
                query = input("Show full output log? [y/n] ")
                doFullLog = True if query.lower() in ["y", "yes"] else False

            installRequirements(pathToRequirements, printOut=doFullLog)

            return
        except FileNotFoundError:
            pass

    ###################################################################################################
    if len(targetPackages) == 0:  # If target packages array is not speficied
        with open(
            "pipinstaller/resources/targetPackages.txt"
        ) as fin:  # Read from targetpackages.txt
            targetPackages = fin.read().splitlines()
            for i in range(len(targetPackages)):
                targetPackages[i] = targetPackages[i].split(",")
    for pkg in targetPackages:
        checkPackage(pkg)
    if len(packagesMissing) == 0:
        print("Nothing to do. Exiting...")
        return
    ###################################################################################################
    if acceptAll:
        doFullLog = True
    else:
        query = input("Show full output log? [y/n] ")
        doFullLog = True if query.lower() in ["y", "yes"] else False
    ###################################################################################################
    if pipInstalled and len(packagesMissing) == 0:  # If both pip and PIL are installed
        print("Pip and all packages are installed.\nNo installations are required.")
        return
    ###################################################################################################
    if not pipInstalled:  # If pip is not installed
        print("Pip was not found on the system.")
        if acceptAll:
            answer = "y"
        else:
            answer = input("Would you like to install the pip command? [y/n] ")

        if answer.lower() in ["y", "yes"]:
            print("Preparing to install Pip...")
            pipSuccess = installPip(doFullLog)

            if not pipSuccess:
                print("Error occurred when installing pip")
                if not acceptAll:
                    if not input(
                        "Would you like to try to continue anyways?[y/n] "
                    ).lower() in ["y", "yes"]:
                        return

            else:
                print("Pip was installed successfully!")

        else:
            print("Package installation cannot continue without pip.\nExiting...")
            return
    ###################################################################################################
    for pkg in packagesMissing:
        print(f"Package {pkg[0]} was not found on the system.")
        if acceptAll:
            answer = "y"
        else:
            answer = input(f"Would you like to install the {pkg[0]} package? [y/n] ")

        if answer.lower() in ["y", "yes"]:
            print(f"Preparing to install {pkg[0]}...")
            pkgSuccess = installPackage(pkg, doFullLog)

            if not pkgSuccess:
                print(f"Error occurred when installing {pkg[0]}")
                if not acceptAll and not input(
                    "Would you like to try to continue anyways?[y/n] "
                ).lower() in ["y", "yes"]:
                    return
            else:
                print(f"{pkg[0]} was installed successfully!")

    print("Everything Finished! Exiting...")


###################################################################################################
