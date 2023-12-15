import os
import pyfiglet
import random
from termcolor import colored

os.system("clear")

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'Install'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

libraries_to_install = [
    "subprocess",
    "Style",
    "Fore",
    "init",
    "colored",
    "pyfiglet",
    "requests",
    "os",
    "sys"
]

for library in libraries_to_install:
    os.system(f"pip install {library}")
    
