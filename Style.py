import os
import sys
import subprocess
import pyfiglet
import time 
import random
from colorama import Fore, Style, init
from termcolor import colored
from time import sleep

def print_loading():
    loading_text = colored("[*]", "blue") + colored("Running", "red") + colored("...", "yellow")
    
    for char in loading_text:
        print(char, end='', flush=True)
        time.sleep(0.1)

print_loading()

print(1*"\n")

os.system("clear")

blue_text = """
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
                       ,d0Odlc;,..              [version 1]     
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

print('\033[94m' + blue_text + '\033[0m')

insta_text = (
    "+----------------------------------------------------+\n"
    f"{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   \n"
    f"{Fore.RED}GitHub{Fore.YELLOW} =====> {Fore.CYAN}https://www.github.com/MohmmadALbaqer/{Style.RESET_ALL}   \n"
    "+----------------------------------------------------+"
)
print(insta_text)

print(1*"\n")

def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\rPlease wait {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
wait_with_spinner(wait_time)

text = "Note:- After making each shape, you need to work on it\"Restart\" "

note_start_index = text.find("Note:-")
if note_start_index != -1:
    note_end_index = note_start_index + len("Note:-")
    colored_text = colored(text[:note_start_index], "red") + colored(text[note_start_index:note_end_index], "red") + text[note_end_index:]
else:
    colored_text = text

restart_start_index = colored_text.find("Restart")
if restart_start_index != -1:
    restart_end_index = restart_start_index + len("Restart")
    colored_text = colored_text[:restart_start_index] + colored(colored_text[restart_start_index:restart_end_index], "yellow") + colored_text[restart_end_index:]

print(colored_text)

print(1*"\n")

environments = {
    1: 'xfce4',
    2: 'gnome',
    3: 'kde-plasma',
    4: 'mate',
    5: 'lxqt',
}

def change_default_environment():
    try:
        subprocess.run(['sudo', 'update-alternatives', '--config', 'x-session-manager'])
        subprocess.run(['sudo', 'reboot'])
        print('Successfully restored the default desktop environment')
    except Exception as e:
        print(f'Error restoring default environment: {e}')

def change_desktop_environment():
    print_colored_options()
    try:
        environment_choice = int(input('Enter the number corresponding to the desired environment: '))
        change_desktop_environment_by_choice(environment_choice)
    except ValueError:
        print('Invalid input. Please enter a valid number.')

def change_desktop_environment_by_choice(choice):
    selected_environment = environments.get(choice)

    if selected_environment:
        try:
            subprocess.run(['sudo', 'apt', 'install', f'kali-desktop-{selected_environment}', '-y'])
            print(f'Successfully changed the desktop environment to {selected_environment}')

            reboot_choice = input('Do you want to reboot? (y/n): ').lower()
            if reboot_choice == 'y':
                subprocess.run(['sudo', 'reboot'])
        except Exception as e:
            print(f'Error changing desktop environment: {e}')
    else:
        print('Invalid choice')

def print_colored_options():
    colored_options = {
        1: '\033[92m',  # Green
        2: '\033[94m',  # Blue
        3: '\033[93m',  # Yellow
        4: '\033[91m',  # Red
        5: '\033[0m',   # Reset color
    }

    for i in range(1, 6):
        print(f'{colored_options[i]}[ {i} ] {colored_options[5]}{environments[i]}')

def main():
    print('[1] Restore Default Environment')
    print('[2] Change Desktop Environment')

    try:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            change_default_environment()
        elif choice == 2:
            change_desktop_environment()
        else:
            print('Invalid choice')
    except ValueError:
        print('Invalid input. Please enter a valid number.')

if __name__ == "__main__":
    main()
