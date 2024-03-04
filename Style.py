import os
from colorama import Fore, Style
os.system("clear")

print(f"""{Fore.BLUE}
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
                     {Fore.BLUE};XO,                         {Fore.RED}_____ _                            {Fore.YELLOW}__ _         _        
                       {Fore.BLUE},d0Odlc;,..               {Fore.RED}/__   \ |__   ___ _ __ ___   ___   {Fore.YELLOW}/ _\ |_ _   _| | ___     
                           {Fore.BLUE}..',;:cdOOd::,.         {Fore.RED}/ /\/ '_ \ / _ \ '_ ` _ \ / _ \  {Fore.YELLOW}\ \| __| | | | |/ _ \ 
                                    {Fore.BLUE}.:d;.':;.     {Fore.RED}/ /  | | | |  __/ | | | | |  __/  {Fore.YELLOW}_\ \ |_| |_| | |  __/ 
                                       {Fore.BLUE}'d,  .'    {Fore.RED}\/   |_| |_|\___|_| |_| |_|\___|  {Fore.YELLOW}\__/\__|\__, |_|\___|   
                                         {Fore.BLUE};l   ..                                            {Fore.YELLOW}|___/         
                                          {Fore.BLUE}.o         
                                            {Fore.BLUE}c      
                                            {Fore.BLUE}.'
                                             {Fore.BLUE}.
 {Fore.RED}+------------------------------------------------------------------+
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
 {Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}        
""")

def choose_environment():
    print(f"{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}]{Fore.BLUE} Switch between Kali Linux environments{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}]{Fore.BLUE} Install environments{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}]{Fore.BLUE} Install all environments{Style.RESET_ALL}")
    
    choice = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}]{Fore.YELLOW} Please choose the option number: {Style.RESET_ALL}")

    if choice == '1':
        print(f"{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] {Fore.YELLOW}gdm3{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] {Fore.YELLOW}lightdm{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}] {Fore.YELLOW}sddm{Style.RESET_ALL}")
        
        env_choice = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}]{Fore.YELLOW} Please choose the environment number: {Style.RESET_ALL}")
        
        if env_choice in ['1', '2', '3']:
            env_name = ['gdm3', 'lightdm', 'sddm'][int(env_choice) - 1]
            os.system(f"sudo dpkg-reconfigure {env_name}")
        else:
            print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Incorrect selection please try again{Style.RESET_ALL}")

    elif choice == '2':
        print(f"{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}]{Fore.BLUE} lightdm{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}]{Fore.BLUE} gdm3{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}]{Fore.BLUE} kali-desktop-gnome{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}4{Fore.WHITE}]{Fore.BLUE} kali-desktop-kde{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}5{Fore.WHITE}]{Fore.BLUE} kali-desktop-xfce{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}6{Fore.WHITE}]{Fore.BLUE} kali-desktop-lxde{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[{Fore.GREEN}7{Fore.WHITE}]{Fore.BLUE} kali-desktop-i3{Style.RESET_ALL}")

        env_choice = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}]{Fore.YELLOW} Please choose the environment number: {Style.RESET_ALL}")

        if env_choice in ['1', '2', '3', '4', '5', '6', '7']:
            env_name = ['lightdm', 'gdm3', 'kali-desktop-gnome', 'kali-desktop-kde', 'kali-desktop-xfce', 'kali-desktop-lxde', 'kali-desktop-i3'][int(env_choice) - 1]
            os.system(f"sudo apt install {env_name}")
        else:
            print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Incorrect selection please try again{Style.RESET_ALL}")

    elif choice == '3':
        os.system("sudo apt-get install kali-linux-everything")

    else:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Incorrect selection please try again{Style.RESET_ALL}")

if __name__ == "__main__":
    choose_environment()
