import os
import time
import datetime

os.system("clear")

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"

now = datetime.datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "] " + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + " [" + "\033[92;1m" + "Time" + "\033[94;1m" + "] " + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"


if os.geteuid() != 0:
    sudo = "\033[1;31m" + "sudo" + "\033[97;1m"
    root = "\033[93;1m" + "root" + "\033[97;1m"
    print(f"{please} {W}please use {root} Type a command {sudo}")
    exit()

print(f"""{B}
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
                     {B};XO,                         {R}_____ _                            {Y}__ _         _        
                       {B},d0Odlc;,..               {R}/__   \ |__   ___ _ __ ___   ___   {Y}/ _\ |_ _   _| | ___     
                           {B}..',;:cdOOd::,.         {R}/ /\/ '_ \ / _ \ '_ ` _ \ / _ \  {Y}\ \| __| | | | |/ _ \ 
                                    {B}.:d;.':;.     {R}/ /  | | | |  __/ | | | | |  __/  {Y}_\ \ |_| |_| | |  __/ 
                                       {B}'d,  .'    {R}\/   |_| |_|\___|_| |_| |_|\___|  {Y}\__/\__|\__, |_|\___|   
                                         {B};l   ..                                            {Y}|___/         
                                          {B}.o       {G} _  _  _   |  o    |    o               
                                            {B}c       {G}|-<_ |_|_ |_ |    |___ | |\| |_| ><
                                            {B}.'
                                             {B}.
{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}""")

def choose_environment():
    print(f"""
+---+----------------------------------------+
|{G}ID{W} | {Y}Options{W}                                |
|---+----------------------------------------+
| {B}1{W} | {M}Switch between Kali Linux environments{W} |
| {B}2{W} | {M}Install environments{W}                   |
| {B}3{W} | {M}Install all environments{W}               |
+---+----------------------------------------+
""")
    
    choice = input(f"{Enter} Please choose the option number: {W}")

    if choice == '1':
        print(f"""
+---+---------+
|{G}ID{W} | {Y}Options{W} |
|---+---------+
| {B}1{W} | {M}gdm3{W}    |
| {B}2{W} | {M}lightdm{W} |
| {B}3{W} | {M}sddm{W}    |
+---+---------+
""")
        
        env_choice = input(f"{Enter} Please choose the environment number: {W}")
        
        if env_choice in ['1', '2', '3']:
            env_name = ['gdm3', 'lightdm', 'sddm'][int(env_choice) - 1]
            os.system(f"sudo dpkg-reconfigure {env_name}")
        else:
            print(f"{please} Incorrect selection please try again{W}")

    elif choice == '2':
        print(f"""
+---+--------------------+
|{G}ID{W} | {Y}options{W}            |
|---+--------------------+
| {B}1{W} | {M}lightdm{W}            |
| {B}2{W} | {M}gdm3{W}               |
| {B}3{W} | {M}kali-desktop-gnome{W} |
| {B}4{W} | {M}kali-desktop-kde{W}   |
| {B}5{W} | {M}kali-desktop-xfce{W}  |
| {B}6{W} | {M}kali-desktop-lxde{W}  |
| {B}7{W} | {M}kali-desktop-i3{W}    |
+---+--------------------+
""")
        

        env_choice = input(f"{Enter} Please choose the environment number: {W}")

        if env_choice in ['1', '2', '3', '4', '5', '6', '7']:
            env_name = ['lightdm', 'gdm3', 'kali-desktop-gnome', 'kali-desktop-kde', 'kali-desktop-xfce', 'kali-desktop-lxde', 'kali-desktop-i3'][int(env_choice) - 1]
            os.system(f"sudo apt install {env_name}")
        else:
            print(f"{ERROR} Incorrect selection please try again{W}")

    elif choice == '3':
        input(f"{warning} {W}The download size is {G}[{B}50GB{G}]{W} and takes {G}[{B}30 minutes{G}]{W} If you agree click {B}[{G}Enter{B}]{W} or you want to stop and exit click {B}[{Y}Ctrl {W}+{Y} C{B}]{W}\n\r")
        print(date_day)
        os.system("sudo apt-get install kali-linux-everything -y")
        os.system("sudo apt install kali-legacy-wallpapers -y")
        os.system("sudo apt install kali-wallpapers-2019.4 -y")
        os.system("sudo apt install kali-wallpapers-2020.4 -y")
        os.system("sudo apt install kali-wallpapers-2021.4 -y")
        os.system("sudo apt install kali-wallpapers-2022 -y")
        os.system("sudo apt install kali-wallpapers-2023 -y")
        os.system("sudo apt install kali-wallpapers-202 -y")
        os.system("sudo apt install kali-wallpapers-all -y")
        os.system("sudo apt install kali-wallpapers-legacy -y")
        os.system("sudo apt install kali-wallpapers-mobile-2023 -y")
        print(date_day)
        time.sleep(5)
        os.system("clear")
        input(f"{Enter} Do you want to restart? If you agree click {B}[{G}Enter{B}]{W} or you want to stop and exit click {B}[{Y}Ctrl {W}+{Y} C{B}]{W}\n\r")

        os.system("sudo reboot")
    else:
        print(f"{please} Incorrect selection please try again{W}")

if __name__ == "__main__":
    choose_environment()
