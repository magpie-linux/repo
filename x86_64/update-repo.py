#!/usr/bin/python3

''' Written by: Rizwan Hasan '''

import os  as magpie
import sys as system
from colorama import Fore, Back, Style

class GitWork:
    # MagpieOS Github repo updater
    def repoUpdate(self, commit, remove = "empty", x = 0):
        if magpie.path.isdir('.git') is True:
            if remove is not "empty":
                if x is not 0:
                    print(Fore.GREEN + "\nRemoving files...\n" + Style.RESET_ALL)
                gitRemove = "git rm " + remove
                magpie.system(gitRemove)
            if x is not 0:
                print(Fore.GREEN + "\nRemoving files...\n" + Style.RESET_ALL)
            magpie.system('git rm -f magpieos.*')
            if x is not 0:
                print(Fore.GREEN + "\nCreating new arch repository...\n" + Style.RESET_ALL)
            magpie.system('repo-add magpieos.db.tar.xz *.pkg.tar.xz')
            if x is not 0:
                print(Fore.GREEN + "\nAdding files to github..." + Style.RESET_ALL)
            magpie.system('git add -A')
            if x is not 0:
                print(Fore.GREEN + "\nCommitting to github...\n" + Style.RESET_ALL)
            gitCommit = "git commit -m " + "'" + commit + "'"
            magpie.system(gitCommit)
            if x is not 0:
                print(Fore.GREEN + "\nPushing updated repo to github...\n" + Style.RESET_ALL)
            magpie.system('git push')
            if x is not 0:
                print(Fore.GREEN + "\nSuccessfuly done." + Style.RESET_ALL)
            return 0
        else:
            print(Fore.RED + "This is not a git repo directory." + Style.RESET_ALL)
            return 1

def GitStart():
    # Git work starting function
    gitCommit = input(Fore.YELLOW + "Git commit comment: " + Style.RESET_ALL)
    if gitCommit is "" :
        gitCommit = "update"
    gitRemove = input(Fore.YELLOW + "Enter file names for removal: " + Style.RESET_ALL)
    if gitRemove is "" :
        gitRemove = "empty"
    print(Fore.BLUE + "Working.." + Style.RESET_ALL)
    GitWork().repoUpdate(gitCommit,gitRemove,1)
    return 0


# Main Function ↓
def main():
    try:
    	if system.platform == "linux":
        	GitStart()
    	else:
        	print(Fore.RED + "You platform is not Linux." + Style.RESET_ALL)
    except KeyboardInterrupt:
	    print(Fore.RED + "\nProgram is quitted by user" + Style.RESET_ALL)
    return 0


# Start Application ↓
if __name__ == '__main__':
    main()

# End of Code
