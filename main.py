from os import system
from time import sleep
import chrome_privacy

def banner():
    print("\x1b[0;31m")
    print("  ______ _     _ _______  ______ ______  _____ _______ __   _")
    print(" |  ____ |     | |_____| |_____/ |     \   |   |_____| | \  |")
    print(" |_____| |_____| |     | |    \_ |_____/ __|__ |     | |  \_|\x1b[0m\n")
    print("\x1b[0;32m-"*62)
    print("                Best Friend of Windows Machines")
    print("-" * 62)
    print('\x1b[0m')

def main_menu():
    print("\x1b[0;32m MAIN MENU \n\x1b[0m")
    print("\x1b[0;32m [1]\x1b[0m Basic Security")
    print("\x1b[0;32m [2]\x1b[0m Privacy")
    print("\x1b[0;32m [3]\x1b[0m Optimization")
    print("\x1b[0;32m [4]\x1b[0m Exit\n")

    main_choose = input("Your choice (1 - 4) :")

    if(main_choose == "4"):
        system('cls')
        print("\x1b[0;32m")
        print(" _______ _______ _______ __   __      _______ _______ _______ _______")
        print(" |______    |    |_____|   \_/        |______ |_____| |______ |______")
        print(" ______|    |    |     |    |         ______| |     | |       |______")
        print('\x1b[0m')

        exit()

    system('cls')
    return main_choose

def main_page():
    system('cls')
    banner()
    main_choosee = main_menu()
    main_choose(main_choosee)

def main_choose(main_choose):
    if (main_choose == "1"):
        banner()

        security_menu()

        security_process()

    elif (main_choose == "2"):

        privacy_host_file_process()

        banner()

        privacy_menu()

        privacy_process()

    elif (main_choose == "3"):
        banner()

        optimization_menu()

        optimization_process()

    else:
        print("Please enter a number between 1 and 4 !")
        sleep(2)
        main_page()

# **************************

def privacy_menu():
    print("\x1b[0;32m PRIVACY MENU \x1b[0m")
    print("\n\x1b[0;32m [1]\x1b[0m Turn off windows telemetry")
    print("\x1b[0;32m [2]\x1b[0m Block sending user events")
    print("\x1b[0;32m [3]\x1b[0m Turn off windows error reporting")
    print("\x1b[0;32m [4]\x1b[0m Chrome Privacy")
    print("\x1b[0;32m [5]\x1b[0m Back\n")

def privacy_process():
    control = True
    while (control == True):
        privacy_choose = input("Your choice (1 - 5) :")
        if (privacy_choose == "1" or privacy_choose == "2" or privacy_choose == "3" or privacy_choose == "4" or privacy_choose == "5"):
            control = False
    system('cls')
    if (privacy_choose == "1"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "2"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "3"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "4"):
        chrome_privacy.chrome_banner()
        approval = "NO"
        while (approval == "NO"):
            approvall = chrome_privacy.clear_chrome_data()
            if (approvall == "NO" or approvall == True):
                main_page()
            else:
                approval = "YES"
                chrome_privacy.command_clear_chrome_data()
                main_page()
    else:
        main_page()

def privacy_host_file_process():
    print("")

# **************************

def security_menu():
    print("\x1b[0;32m SECURITY MENU \x1b[0m")
    print("\n\x1b[0;32m [1]\x1b[0m Turn off USB storage")
    print("\x1b[0;32m [2]\x1b[0m Turn off sharing windows folder")
    print("\x1b[0;32m [3]\x1b[0m IP blocking")
    print("\x1b[0;32m [4]\x1b[0m Activate HSTS (Strict Transport Security)")
    print("\x1b[0;32m [5]\x1b[0m Turn off ping (by other computers)")
    print("\x1b[0;32m [6]\x1b[0m Password protection")
    print("\x1b[0;32m [7]\x1b[0m Encrypt patch file")
    print("\x1b[0;32m [8]\x1b[0m Delete patch file (when computer shuts down)")
    print("\x1b[0;32m [9]\x1b[0m Turn off remote registry access")
    print("\x1b[0;32m [10]\x1b[0m Back\n")


def security_process():
    control = True
    while (control == True):
        security_choose = input("Your choice (1 - 10) :")
        if (security_choose == "1" or security_choose == "2" or security_choose == "3" or security_choose == "4" or security_choose == "5" or security_choose == "6" or security_choose == "7" or security_choose == "8" or security_choose == "9" or security_choose == "10"):
            control = False
    system('cls')
    if (security_choose == "1"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "2"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "3"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "4"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "5"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "6"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "7"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "8"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "9"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        security_menu()

        security_process()
    else:
        main_page()

# **************************

def optimization_menu():
    print("\x1b[0;32m OPTIMIZATION MENU \x1b[0m")
    print("\n\x1b[0;32m [1]\x1b[0m Regular writing of Windows system files")
    print("\x1b[0;32m [2]\x1b[0m Turn off unnecessary animations")
    print("\x1b[0;32m [3]\x1b[0m Defrag the disk")
    print("\x1b[0;32m [4]\x1b[0m Fix windows errors")
    print("\x1b[0;32m [5]\x1b[0m Back\n")


def optimization_process():
    control = True
    while (control == True):
        optimization_choose = input("Your choice (1 - 5) :")
        if (optimization_choose == "1" or optimization_choose == "2" or optimization_choose == "3" or optimization_choose == "4" or optimization_choose == "5"):
            control = False
    system('cls')
    if (optimization_choose == "1"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        optimization_menu()

        optimization_process()
    elif (optimization_choose == "2"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        optimization_menu()

        optimization_process()
    elif (optimization_choose == "3"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        optimization_menu()

        optimization_process()
    elif (optimization_choose == "4"):
        banner()
        print("The development process continues.")
        sleep(1)
        system('cls')
        banner()

        optimization_menu()

        optimization_process()
    else:
        main_page()

main_page()





