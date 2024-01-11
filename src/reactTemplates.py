
class HeroSection:
    def __init__(self, filename, colour, font, animation=False):
        #Needs Input Validation but CBA rn
        self.primaryColour = colour[0]
        self.secondaryColour = colour[1]
        self.animation = animation
        self.classFilename = filename
        filename = filename[0].upper() + filename[1:]
        self.filename = filename
        self.documentFilenameJS = f"{filename}.js"
        self.documentFilenameCSS = f"{self.classFilename}.css"

    def buildJSX(self):
        if(self.animation):
            pass #Animated Version with framer.motion installed
        else:
            return f"""const {self.filename} = () => {{
    return(
        <div className="{self.classFilename}_wrapper">
            <div className="{self.classFilename}">
                
            </div>
        </div>
    )
    export default {self.filename};
}}
        """
        

        
    def build(self):
        pass

    def __str__(self):
        return self.filename