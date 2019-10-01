from installFunctions import checkPip, installPip, checkPackage, installPackage
import sys


def install():
    pipInstalled = checkPip()
    packageInstalled = checkPackage()
###################################################################################################
    query = input("Show full output log? [y/n] ")
    doFullLog = False
    if query.lower() in ["y", 'yes']:
        doFullLog = True
###################################################################################################
    if pipInstalled and packageInstalled: #If both pip and PIL are installed
        print("Pip and all packages are installed.\nNo installations are required.")
        sys.exit()
 ###################################################################################################   
    if not pipInstalled: #If pip is not installed
        print("Pip was not found on the system.")
        answer = input("Would you like to install the pip command? [y/n] ")
        
        if answer.lower() in ["y", "yes"]:
            print("Preparing to install Pip...")
            pipSuccess = installPip(doFullLog)
            
            if not pipSuccess:
                print("Error occurred when installing pip")
                if input("Would you like to try to continue anyways?[y/n] ").lower() in ["y", "yes"]:
                    sys.exit()

            else:
                print("Pip was installed successfully!")
        
        else:
            print("Package installation cannot continue without pip.\nExiting...")
            sys.exit()
###################################################################################################    
    if not packageInstalled:
        print("Package PIL was not found on the system.")
        answer = input("Would you like to install the PIL package? [y/n] ")

        if answer.lower() in ["y", "yes"]:
            print("Preparing to install PIL...")
            pilSuccess = installPackage(doFullLog)
            
            if not pilSuccess:
                print("Error occurred when installing PIL")
                if input("Would you like to try to continue anyways?[y/n] ").lower() in ["y", "yes"]:
                    sys.exit()
            else:
                print("PIL was installed successfully!")
        
        else:
            print("Exiting...")
            sys.exit()
    
    print("Everything was installed successfully!")
###################################################################################################
if __name__ == '__main__': #Only runs automatically if the actual script is run
    install()