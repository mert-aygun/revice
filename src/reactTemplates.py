class HeroSection:
    def __init__(self, filename):
        self.classFilename = filename
        filename = filename[0].upper() + filename[1:]
        self.filename = filename


    def buildJSX(self):
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