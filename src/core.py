import os


version = "1.0.0"
dateStarted = "10/01/24"
author = "Mert Aygun"

class Console:
    def __init__(self):
        self.versionLine = f"Revice - Version {version}"
        self.consoleOutput = ""

    def __str__(self):
        return self.consoleOutput
    #Setters
    def updateConsoleTitle(self, newOutput):
        self.consoleOutput = f"{self.versionLine}\n\t{newOutput}"

    #Getters
    def getOptionList(self):
        return """
        1 - Add Colour Scheme
        2 - Choose Font Size
        3 - Select Template
        4 - Exit
        """

    def getConsole(self):
        return (f"""
        {self.consoleOutput}
        ===================
        {self.getOptionList()}
        """)
        
    def getInput(self):
        consoleInput = int(input("> "))
        self.input = consoleInput