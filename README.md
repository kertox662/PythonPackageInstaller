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
    - Some packages are not named the same as a module as it is on PyPi. PyPi is 
    the database that pip uses to install the packages. When adding the pair of
    values to the file or the list, make sure to add it in the form:
    "moduleName","PyPiName"
    To find the PyPi name, search for the package online and choose which version
    of the module you would like the installer to get.
    - It is possible for the installer to get extra command line arguments for the
    pip install call. The only argument that is present by default is --user. To
    specify an extra argument, add the argument to the end of the PyPiName wherever
    it is used. Make sure there is a space between the package name and the arguments.

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
