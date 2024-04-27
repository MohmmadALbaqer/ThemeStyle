import os

os.system("clear")

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey

sign = f"{G}[{B}*{G}] {B}"
Enter = f"{B}[{G}+{B}] {G}"
ERROR = f"{Y}[{R}!{Y}] {R}"

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
                                          {B}.o         
                                            {B}c      
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
            print(f"{ERROR} Incorrect selection please try again{W}")

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
        os.system("sudo apt-get install kali-linux-everything")

    else:
        print(f"{ERROR} Incorrect selection please try again{W}")

if __name__ == "__main__":
    choose_environment()
