# PythonPackageInstaller
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/kertox662/PythonPackageInstaller.svg)](https://github.com/kertox662/PythonPackageInstaller/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/kertox662/PythonPackageInstaller.svg)](https://GitHub.com/kertox662/PythonPackageInstaller/releases/)
[![Github all releases](https://img.shields.io/github/downloads/kertox662/PythonPackageInstaller/total.svg)](https://GitHub.com/kertox662/PythonPackageInstaller/releases/)
[![GitHub contributors](https://img.shields.io/github/contributors/kertox662/PythonPackageInstaller.svg)](https://GitHub.com/kertox662/PythonPackageInstaller/graphs/contributors/)
[![GitHub stars](https://img.shields.io/github/stars/kertox662/PythonPackageInstaller.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/kertox662/PythonPackageInstaller/stargazers/)
<br/>
This script allows for easy installation of a batch of package dependencies
given a file or modifying the script. This tool uses pip, which is included
locally for ease of inclusion for the tool.

## HOW TO USE ##
1. When including in a project, provide the `pipinstaller` folder on the top level of the
project. Inlcude all files in the repository `pipinstaller` folder in the project folder.
This ensures that the functions can reach each other. Additionally, make sure 
to have a resources folder for the pip script and the list of target packages.
This can be done easily by simply copying both folders from the repository to 
the project.

2. Packages can be specified in two ways:
    - Modifying the list named "targetPackages" in install_Functions.py under `pipinstaller`
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

If the `pipinstaller` folder is in the same folder as the starter file, this can be done by doing:
```python
import pipinstaller
```
For simplicity sake, this is also an option
```python
import pipinstaller as pipi
```

Another option is to just import the install function. To do this, do:
```python
from pipinstaller import install
```
To see an example, look at the install.py file.

4. Please take note that to have the packages be available on the same run as when
the packages are installed, it is necessary for all import of the packages that are
being installed to occur after running the install() procedure. What this means is
that no imports apart from the installation can be done prior to calling the procedure.

For example:
```python
from pipinstaller import install  

install()

#...Your Program
```
or
```python
import pipinstaller as pipi

pipi.install()

#...Your Program
```

Thank you for using this python package installer.