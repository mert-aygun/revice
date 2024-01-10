#A small app that automates the creation of React pages
from src.core import Console
from src.reactTemplates import HeroSection
import os

def main():
    run = True
    while run:
        clear = lambda: os.system('cls')
        clear()
        console = Console()
        console.updateConsoleTitle("Select Template")
        print(console.getConsole())
        console.getInput()
        if(console.input == 1):
            print("Add Colour Scheme")
        elif(console.input == 2):
            print("Add Colour Scheme")
        elif(console.input == 3): #ADD TEMPLATES
            a = HeroSection("ballsack")
            print(a.buildJSX())
            break
        else:
            exit()

    
if __name__ == "__main__":
    main()