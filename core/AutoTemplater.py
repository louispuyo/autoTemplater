from templater import CF, ExampleViews
from config import decorama
from res.themes import themes

def Theme_Setter(html_path, css_path, js_path=None):
    with open(html_path+".html","a+") as template:
        template.write("\n{% include \'"+css_path+"\' %}\n")
        if js_path != "":
            template.write("\n{% include \'"+js_path+"\' %}\n")
            template.close()

def setup():
    # TAG AUTO-TEMPLATER®
    Logo = decorama().Logo
    decorama().backline2(Logo)
    choice = input("Do you want to Have automate your template creation ? ")
    condition = (choice in ['yes','y','Y','YES','Yes'])
    status = ((CF.GREEN,"[ON]") if condition else (CF.RED, "[OFF]"))
    print("Templater : STATUS :", status[0],status[1])
    print(CF.RESET)


    if condition:
        # ACTIVE :
        custom_template_name = input('Choose Your Template name (default = ExampleViewsTemplate) ➜ ')
        print(CF.GREEN,"\n[i] STATUS : [OK]\n")
        print(CF.RESET)

        # PARAMS :
        base_path = __file__.strip(__file__.split('/')[-1])
        themes_name_list = {themes.Bootstrap.__name__:themes.Bootstrap, themes.Bulma.__name__: themes.Bulma}

        # INIT :
        MyView = ExampleViews(create_opt=condition)
        MyView.__setattr__('template_name',f'{custom_template_name}')
        css_path = base_path+"/templates/css/"+MyView.template_name+"_theme.css.html"
        js_path = base_path+"/templates/js/"+MyView.template_name+"_theme.js.html"
        html_path = base_path+"/templates/"+MyView.template_name
        MyView.__setattr__('theme_name',f'{decorama().Theme_setup(MyView, themes_name_list, base_path)}')
        # INCLUDE THEME IN FILE
        
        # FILE CREATION :
        MyView.Templater()
        Theme_Setter(html_path, css_path, js_path)

        # ARGUMENTS :
        MyView.requested_arguments




# DEV 
if __name__ == "__main__":
    setup()
