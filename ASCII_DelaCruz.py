import pyfiglet
from termcolor import colored

colors = ['light_red', 'red', 'red', 'red', 'light_red', 'red']
name = pyfiglet.figlet_format("Leinad Clark", font="bloody")
lines = name.splitlines()
colored_lines = []

for line in lines:
    
    colored_line = ""
    for index, char in enumerate(line):     
        
        color = colors[index % len(colors)]  
        colored_char = colored(char, color)
        colored_line += colored_char
    
    print(colored_line)
    