#A small app that automates the creation of React pages
from src.core import Console
from src.reactTemplates import HeroSection
import os
from time import sleep
def main():
    run = True
    primaryColour = ""
    secondaryColour = ""
    fontSize = 0
    while run:
        clear = lambda: os.system('cls')
        clear()
        console = Console()
        console.updateConsoleTitle("Choose Option")
        print(console.getConsole())
        console.getInput()
        if(console.input == "1"):
            print("Add Colour Scheme")
        elif(console.input == "2"):
            print("Add Colour Scheme")
        elif(console.input == "3"): #ADD TEMPLATES
            console.updateTemplateConsoleTitle("Select Template")
            print(console.getTemplateConsole())
            console.getTemplateInput()
            if(console.templateInput == "1"): #Select Hero Section 1
                if(primaryColour == ""):
                    primaryColour = "rgb(255,255,255)"
                if(secondaryColour == ""):
                    secondaryColour = "rgb(255,255,255)"
                if(fontSize == 0):
                    fontSize = 1 
                heroSection1 = HeroSection("myfile", colour=[primaryColour, secondaryColour], font=fontSize, animation=False)
                print(heroSection1.buildJSX())
                break
            elif(console.templateInput == "2"): #Select Hero Section 2
                pass
            elif(console.templateInput == "3"): #Select Hero Section 3
                pass
            else:
                pass
            
        elif(console.input == "4"): #Exit Program
            print("Exiting Program...")
            sleep(1)
            exit()
        else: #Anything Else
            print("Unknown Command")
            sleep(1)

    
if __name__ == "__main__":
    main()