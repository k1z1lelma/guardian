from os import system
from time import sleep
import subprocess

def chrome_banner():
    print("\x1b[0;31m")
    print("  ______ _     _ _______  ______ ______  _____ _______ __   _")
    print(" |  ____ |     | |_____| |_____/ |     \   |   |_____| | \  |")
    print(" |_____| |_____| |     | |    \_ |_____/ __|__ |     | |  \_|\x1b[0m   \x1b[0;32m(CHROME PRIVACY)\x1b[0m\n")
    print("\x1b[0;32m-"*81)
    print("                         Best Friend of Windows Machines")
    print("-" * 81)
    print('\x1b[0m')

def command_clear_chrome_data():
    system('cls')
    print("\x1b[0;32m [!]\x1b[0m Process is starting!")
    sleep(1)
    print("\x1b[0;32m [!]\x1b[0m Data is being deleted!")
    sleep(1)
    out = subprocess.check_output('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"',stderr=subprocess.STDOUT, shell=True)
    out = str(out)

    if (out.startswith("b'Could Not Find") == True):
        print("\x1b[0;31m [!]\x1b[0m \x1b[0;32mNo data to be deleted!\x1b[0m")
        print("\x1b[0;32m [!]\x1b[0m \x1b[0;32mYour data is safe!\n\x1b[0m")
        input("Press any key ...")
        return True

    if (out != "b''"):
        print("\x1b[0;31m [ERROR]\x1b[0m \x1b[0;31m Please turn off chrome. Otherwise, the data will not be deleted!\n\x1b[0m")
        input("Press any key ...")
        return True
    # system('del /q /f "C:\\Users\\k1z1lelma\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Favicons"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Favicons-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\DownloadMetadata"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\History"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\History Provider Cache"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\History-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\LOG"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\LOG.old"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data For Account"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data For Account-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Reporting and NEL"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Reporting and NEL-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Visited Links"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Web Data"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Web Data-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Safe Browsing Cookies"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Safe Browsing Cookies-journal"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\QuotaManager"')
    system('del /q /f "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\QuotaManager-journal"')

    print("\x1b[0;32m [SUCCESSFUL]\x1b[0m Process finish!\n")
    input("Press any key ...")
    return True

def clear_chrome_data():
    print("The following will be cleared:")
    print("\n\x1b[0;32m [1]\x1b[0m Cookies")
    print("\x1b[0;32m [2]\x1b[0m History")
    print("\x1b[0;32m [3]\x1b[0m Logs")
    print("\x1b[0;32m [4]\x1b[0m Login Data")
    print("\x1b[0;32m [5]\x1b[0m Visited Links")
    print("\x1b[0;32m [5]\x1b[0m Visited Links")
    print("\x1b[0;32m [6]\x1b[0m Meta Data\n")

    print("\x1b[0;31m [!]\x1b[0m \x1b[0;32m Make sure Crhome is turned off!\n\x1b[0m")

    approval = input("YES or NO: ")
    if(approval == "YES"):
        command_clear_chrome_data()
        return True
    elif(approval == "NO"):
        return approval
    else:
        while True:
            approval = input("YES or NO: ")
            if(approval == "YES" or approval == "NO"):
                return approval





