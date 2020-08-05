import colorama

class decorama:
    def __init__(self):
        colorama.init()
        self.prefix = colorama.Fore
        self.Logo = """
    _         _            _____                    _       _            
   / \  _   _| |_ ___     |_   _|__ _ __ ___  _ __ | | __ _| |_ ___ _ __ 
  / _ \| | | | __/ _ \ _____| |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \ '__|
 / ___ \ |_| | || (_) |_____| |  __/ | | | | | |_) | | (_| | ||  __/ |   
/_/   \_\__,_|\__\___/      |_|\___|_| |_| |_| .__/|_|\__,_|\__\___|_|   
                                             |_|                    
                    """
    
    def config_advanced(self):
        pass

    @staticmethod
    def backline1(arg):
        print("\n",arg,"\n")

    @staticmethod
    def backline2(arg):
        print("\n\n",arg,"\n\n")


    def Theme_setup(self,MyView, themes_name_list, base_path):
        CF = decorama().prefix
        self.template_theme = input("choose a template name (default: None) : ")
        if self.template_theme in themes_name_list.keys():
            with open(base_path+"/templates/css/"+MyView.template_name+"_theme.css.html","a+") as template_css:
                template_css.write(themes_name_list[self.template_theme]().css)
                template_css.close
                if self.template_theme == 'Bootstrap':
                    choice_js = input("Do you want to apply js bootstrap links (jquery and Popper.js package) default=[off] : ")
                    if choice_js in ['yes','y','YES','Yes']:
                        with open(base_path+"/templates/js/"+MyView.template_name+"_theme.js.html","a+") as template_js:
                            template_js.write(themes_name_list[self.template_theme]().js)
                            template_js.close()

                print(CF.GREEN, "[i] Template Theme applied !")
                print(CF.RESET)

        return self.template_theme
        



