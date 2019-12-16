# PythonPackageInstaller
This script allows for easy installation of a batch of package dependencies
given a file or modifying the script. This tool uses pip, which is included
locally for ease of inclusion for the tool.

HOW TO USE
1. When including in a project, provide the lib folder on the top level of the
project. This ensures that the functions can reach each other. Additionally,
make sure to have a resources folder for the pip script and the list of target
packages.

2. Packages can be specified in two ways:
    - Modifying the list named "targetPackages" in install_Functions.py under lib
    - Modifying the targetPackages.txt in resources
    - Note that the list in the script takes priority over the file. If it is not
    empty, it will take the packages from there rather than the file.

3. Import install_packages.py and run the install() procedure. This will run the
process to ask the user to install each package.

4. Please take note that to have the packages be available on the same run as when
the packages are installed, it is necessary for all import of the packages that are
being installed to occur after running the install() procedure. What this means is
that no imports apart from the installation can be done prior to calling the procedure.

For example:
from lib.install_Functions import install
install()
import [Insert Library Here]
...Program

Thank you for using this python package installer.
