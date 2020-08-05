import os
from config import decorama

# DECORATOR GLOBALS PARAMETERS
global CF
CF = decorama().prefix


class BaseView:
    methods = ['GET','POST', 'OPTION',...]

class ExampleViews(BaseView):
    def __init__(self, create_opt=False):
        self.create_opt = create_opt
        self.template_name = ExampleViews.__name__+'_template'
        self.template_dirname = 'templates'
        self.ext = 'html'


    def Templater(self):
        if self.create_opt == True:
            base_path = __file__.strip(__file__.split('/')[-1])
            base_html = open(f'{base_path}res/base_html.html', "r")
            html_content = base_html.read()
            perso_html = ""
            if perso_html == "":
                os.system(f"echo '{html_content}' > {base_path}{self.template_dirname}/{self.template_name}.{self.ext}")
                base_html.close()
            
            else:
                os.system(f"echo '{perso_html}' > {base_path}{self.template_dirname}/{self.template_name}.{self.ext}")
                base_html.close()
    

    @staticmethod
    def jinja_formater(arg:str):
        startTag = "\n\n{% for a in "+ arg + " %}\n\n"+ "<li>{{a}}</li>" +"\n\n{% endfor %}"
        return startTag
    

    @property
    def requested_arguments(self, arguments):
        self.arguments = arguments
    
        
    @requested_arguments.getter
    def requested_arguments(self):
        arguments = list(input("input all the args that will be requested : ").split(','))
        self.arguments = arguments
        dir_path = __file__.strip(__file__.split('/')[-1])
        with open(f'{dir_path}/templates/{self.template_name}.html', 'a+') as template:
            for arg in self.arguments:
                template.write(self.jinja_formater(arg))
            
            # close HTML balises
            template.write('\n\n\n</body></html>')
            
            print(CF.GREEN, "[i] Jinja Formating ... Done ")
            print(CF.RESET)
            template.close()
    
               

    @classmethod
    def request_display(cls, file_path:str):
        path = cls(file_path)
    



