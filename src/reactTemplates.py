class BaseStylesheet:
    def __init__(self, colour): #add font parameter
        #Needs Input Validation as well as all other classes (Leave this till the end of the project)
        #Add font sizes
        stylesheet = f"""* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}
:root {{
    --blackBackground: #252525;
    --whiteBackground: #e9e9e9;
    --primaryBackground: {colour[0]};
    --secondaryBackground: {colour[1]};
}}

.black {{

}}
.white {{

}}
.body {{
    width: 100%;
    height:fit-content;
    display:flex;
    flex-direction: column;
    justify-content: baseline;
    align-items: center;
}}

"""
        with open("styles.css", "w") as css:
            css.write(stylesheet)


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
            return f"""import './styles.css'
import './{self.filename}.css'

const {self.filename} = () => {{
    return(
        <div className="body">
            <div className="hero_section_wrapper">
                <div className="hero_section">
                    <div className="hero_section_left">
            
                    </div>
                    <div className="hero_section_right">
            
                    </div>
                </div>
            </div>
        </div>
    )
}}
export default {self.filename};
        """
        

        
    def build(self):
        pass

    def __str__(self):
        return self.filename