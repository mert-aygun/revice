import os


version = "1.0.0"
dateStarted = "10/01/24"
author = "Mert Aygun"

class Console:
    def __init__(self):
        self.versionLine = f"Revice - Version {version}"
        self.consoleOutput = ""
        self.templateConsoleOutput = ""
        self.templateInput = ""

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
        consoleInput = input("> ")
        self.input = consoleInput.strip().lower()

    def getTemplateInput(self):
        consoleInput = input("Template > ")
        self.templateInput = consoleInput.strip().lower()

    def getTemplateOptionList(self):
        return """
        1 - Hero Section Style 1
        2 - Hero Section Style 2
        3 - Hero Section Style 3
        4 - Gallery Style 1
        5 - Gallery Style 2
        """


    def updateTemplateConsoleTitle(self, newOutput):
        self.templateConsoleOutput = f"{self.versionLine}\n\t{newOutput}"

    def getTemplateConsole(self):
        return (f"""
        {self.templateConsoleOutput}
        ===================
        {self.getTemplateOptionList()}

    """)