import os
import subprocess
from colorama import Fore, Style, init

init(autoreset=True) 

os.system("clear")

blue_text = f"""
            ..,;:ccc,.                             
          ......''';lxO.                           
.....''''..........,:ld;                           
           .';;;:::;,,.x,                          
      ..'''.            0Xxoc:,.  ...              
  ....                ,ONkc;,;cokOdc',.            
 .                   OMo           ':ddo.          
                    dMc               :OO;          
                    0M.                 .:o.       
                    ;Wd                            
                     ;XO,                       [BY MohmmadALbaqer]  
                       ,d0Odlc;,..              [version 2]     
                           ..',;:cdOOd::,.          
                                    .:d;.':;.       
                                       'd,  .'      
                                         ;l   ..   
                                          .o         
                                            c      
                                            .'
                                             .                                                                      
  _________ __          __         ___________/\\                           
 /   _____//  |_____ __|  |   ____ \\__    ___/  |__   ____   _____   ____  
 \\_____  \\\\   __\\   |  |  | _/ __ \\  |    |  |  |  \\_/ __ \\ /     \\_/ __ \\ 
 /        \\|  |  \\___  |  |__  ___/_ |    |  |      \\  ___/_  | |  \\  ___/_
/_______  /|__|  / ____|____/\\___  / |____|  |___|  /\\___  /__|_|  /\\___  /
        \\/       \\/              \\/               \\/     \\/      \\/     \\/ 
"""

print(Fore.BLUE + blue_text + Style.RESET_ALL)

print(f'''
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.instagram.com/r94xs/        {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+
{Style.RESET_ALL}''')

text = "Note:- After making each shape, you need to work on it\"Restart\" "

note_start_index = text.find("Note:-")
if note_start_index != -1:
    note_end_index = note_start_index + len("Note:-")
    colored_text = Fore.RED + text[:note_start_index] + text[note_start_index:note_end_index] + text[note_end_index:]
else:
    colored_text = text

restart_start_index = colored_text.find("Restart")
if restart_start_index != -1:
    restart_end_index = restart_start_index + len("Restart")
    colored_text = colored_text[:restart_start_index] + Fore.YELLOW + colored_text[restart_start_index:restart_end_index] + colored_text[restart_end_index:]

print(colored_text)

print(1 * "\n")

environments = {
    1: 'xfce4',
    2: 'gnome',
    3: 'kde-plasma',
    4: 'mate',
    5: 'lxqt',
    6: 'i3',
    7: 'lightdm',
}

def change_default_environment():
    try:
        subprocess.run(['sudo', 'update-alternatives', '--config', 'x-session-manager'])
        subprocess.run(['sudo', 'reboot'])
        print('Successfully restored the default desktop environment')
    except Exception as e:
        print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Error restoring default environment: {e}{Style.RESET_ALL}')

def change_desktop_environment():
    print_colored_options()
    try:
        environment_choice = int(input(f'{Fore.GREEN}[+] Enter the number corresponding to the desired environment: {Style.RESET_ALL}'))
        change_desktop_environment_by_choice(environment_choice)
    except ValueError:
        print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}')

def change_desktop_environment_by_choice(choice):
    selected_environment = environments.get(choice)

    if selected_environment:
        try:
            subprocess.run(['sudo', 'apt', 'install', f'kali-desktop-{selected_environment}', '-y'])
            print(f'Successfully changed the desktop environment to {selected_environment}')

            reboot_choice = input('[*] Do you want to reboot? (y/n): ').lower()
            if reboot_choice == 'y':
                subprocess.run(['sudo', 'reboot'])
        except Exception as e:
            print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Error changing desktop environment: {e}{Style.RESET_ALL}')
    else:
        print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid choice{Style.RESET_ALL}')

def print_colored_options():
    colored_options = {
        1: Fore.GREEN,   # Green
        2: Fore.BLUE,    # Blue
        3: Fore.YELLOW,  # Yellow
        4: Fore.RED,     # Red
        5: Fore.CYAN,    #Cyan
        6: Fore.MAGENTA, #Magenta
        7: Style.RESET_ALL,   # Reset color
    }

    for i in range(1, 7):
        print(f'{colored_options[i]}[ {i} ] {colored_options[5]}{environments[i]}')

def main():
    print(f'{Fore.GREEN}[1] Restore Default Environment{Style.RESET_ALL}')
    print(f'{Fore.GREEN}[2] Change Desktop Environment{Style.RESET_ALL}')

    try:
        choice = int(input(f'{Fore.BLUE}[+] Enter your choice: {Style.RESET_ALL}'))

        if choice == 1:
            change_default_environment()
        elif choice == 2:
            change_desktop_environment()
        else:
            print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid choice{Style.RESET_ALL}')
    except ValueError:
        print(f'{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}')

if __name__ == "__main__":
    main()
