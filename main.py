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

def full_protection_banner():
    print("\x1b[0;32m")
    print("   |\                |\                |\                |\             ")
    print("   || .---.          || .---.          || .---.          || .---.       ")
    print("   ||/_____\         ||/_____\         ||/_____\         ||/_____\      ")
    print("   ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )      ")
    print("   || \_-_/_         || \_-_/_         || \_-_/_         || \_-_/_      ")
    print("   :-\"`\'V\'//-.       :-\"`\'V\'//-.       :-\"`\'V\'//-.       :-\"`\'V\'//-.    ")
    print("  / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `\  ")
    print(" / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |  ")
    print("/_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  ")
    print("\ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  ")
    print(" \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |  ")
    print(" /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |  ")
    print(" `--|`^\"\"\"^`||_|   `--|`^\"\"\"^`||_|   `--|`^\"\"\"^`||_|   `--|`^\"\"\"^`||_|  ")
    print("    |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/   ")
    print("    |   |   |         |   |   |         |   |   |         |   |   |     ")
    print("    |   |   |         |   |   |         |   |   |         |   |   |     ")
    print("    |   |   |         |   |   |         |   |   |         |   |   |     ")
    print("    L___l___J         L___l___J         L___l___J         L___l___J     ")
    print("     |_ | _|           |_ | _|           |_ | _|           |_ | _|      ")
    print("    (___|___)         (___|___)         (___|___)         (___|___)     ")
    print("     ^^^ ^^^           ^^^ ^^^           ^^^ ^^^           ^^^ ^^^      \x1b[0m")

def main_menu():
    print("\x1b[0;32m MAIN MENU \n\x1b[0m")
    print("\x1b[0;32m [1]\x1b[0m Basic Security")
    print("\x1b[0;32m [2]\x1b[0m Privacy")
    print("\x1b[0;32m [3]\x1b[0m Full Protection")
    print("\x1b[0;32m [4]\x1b[0m Exit\n")

    main_choose = input("Your choice (1 - 4) :")

    if(main_choose == "4"):
        system('cls')
        print("\x1b[0;32m")
        print(" _______ _______ _______ __   __      _______ _______ _______ _______")
        print(" |______    |    |_____|   \_/        |______ |_____| |______ |______")
        print(" ______|    |    |     |    |         ______| |     | |       |______")
        print('\x1b[0m')

        choose = input("Would you like to update your hosts file to prevent the settings \nnyou have made from being reverted by Microsoft? [Y or N]")

        if(choose == "y" or  choose == "Y"):
            system('host.bat')

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

        banner()

        privacy_menu()

        privacy_process()


    elif (main_choose == "3"):
        full_protection_banner()

        full_protection_process()

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
    print("\x1b[0;32m [5]\x1b[0m Microsoft Edge Privacy")
    print("\x1b[0;32m [6]\x1b[0m Turn off sending clipboard data to Microsoft")
    print("\x1b[0;32m [7]\x1b[0m Turn off sending device metadata to Microsoft")
    print("\x1b[0;32m [8]\x1b[0m Turn off sending driver information to Microsoft")
    print("\x1b[0;32m [9]\x1b[0m Turn off sending hardware information to Microsoft")
    print("\x1b[0;32m [10]\x1b[0m Internet Explorer Privacy")
    print("\x1b[0;32m [11]\x1b[0m Turn off sending language of OS and browser to Microsoft")
    print("\x1b[0;32m [12]\x1b[0m Turn off sending location information to Microsoft")
    print("\x1b[0;32m [13]\x1b[0m Windows Media Player Privacy")
    print("\x1b[0;32m [14]\x1b[0m One Drive Privacy")
    print("\x1b[0;32m [15]\x1b[0m Turn off sending search bar data to Microsoft")
    print("\x1b[0;32m [16]\x1b[0m Turn off sending settings to Microsoft")
    print("\x1b[0;32m [17]\x1b[0m Back\n")

def privacy_process():
    control = True
    while (control == True):
        privacy_choose = input("Your choice (1 - 17) :")
        if (privacy_choose == "1" or privacy_choose == "2" or privacy_choose == "3" or privacy_choose == "4" or privacy_choose == "5" or privacy_choose == "6" or privacy_choose == "7" or privacy_choose == "8" or privacy_choose == "9" or privacy_choose == "10" or privacy_choose == "11" or privacy_choose == "12" or privacy_choose == "13" or privacy_choose == "14" or privacy_choose == "15" or privacy_choose == "16" or privacy_choose == "17"):
            control = False
    system('cls')
    if (privacy_choose == "1"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/close_telemetry.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "2"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/user_activity.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "3"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/error_reporting.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
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
    elif (privacy_choose == "5"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/edge_privacy.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "6"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/clipboard_info.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "7"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/device_metadata.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "8"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/driver_info.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "9"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/hardware_info.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "10"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/internet_explorer_privacy.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "11"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/language_info.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "12"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/location.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "13"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/media_player.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "14"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/one_drive.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "15"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/windows_search.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    elif (privacy_choose == "16"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S privacy/setting_sync.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        privacy_menu()

        privacy_process()
    else:
        main_page()


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
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S security/usb_storage.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "2"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S security/close_administrative_shares.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
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
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S security/patch_file.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "8"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S security/wipe_patch_file.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        security_menu()

        security_process()
    elif (security_choose == "9"):
        banner()
        print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
        system('REGEDIT /S security/remote_registry.reg')
        sleep(1)
        print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
        sleep(2)
        system('cls')
        banner()

        security_menu()

        security_process()
    else:
        main_page()

# **************************

def full_protection_process():
    print("\x1b[0;32m [!]\x1b[0m Setting is in progress")
    system('REGEDIT /S full_privacy.reg')
    sleep(1)
    print("\x1b[0;32m [!]\x1b[0m Completed Successfully")
    sleep(2)
    main_page()

main_page()

