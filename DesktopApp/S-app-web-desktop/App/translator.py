from .lib import *

class Translator:
    def __init__(self):
        self.isLangInit = False
        self.available_packages = argostranslate.package.get_available_packages()
        self.available_packages_list = sorted([ str(i).replace("→","->") for i in self.available_packages ] )


    def initLang(self, from_language, to_language):
        self.isLangInit = True
        with open("App/languages/codes.json", "r") as f:
            data = load(f)
            from_code = data[from_language]
            to_code = data[to_language]

        self.installed_languages = argostranslate.translate.get_installed_languages()
        self.from_lang = list(filter(
            lambda x: x.code == from_code,
            self.installed_languages))[0]

        self.to_lang = list(filter(
            lambda x: x.code == to_code,
            self.installed_languages))[0]

        self.translation = self.from_lang.get_translation(self.to_lang)

    def translate(self, text: str) -> str:
        return self.translation.translate(text)
    
    def installedPackages(self) :
        return argostranslate.package.get_installed_packages()


    def installLanguagesPackages(self , from_language , to_language) : 
        print("Updating package index ...")
        argostranslate.package.update_package_index()
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]
        
        print("Downloading Package ...")
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
        print("Downloaded and installed.")
        return True
    

    def availablesPackages(self) : 
        with open("App/languages/availables.json","r") as f:
            data = load(f)
        
        return list(data["Models"])


    def installLanguagesPackages(self , from_language , to_language) : 
        print("Updating package index ...")
        argostranslate.package.update_package_index()
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]
        
        print("Downloading Package ...")
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
        print("Downloaded and installed.")
        
    
    
    def uninstallPackage(self,from_language , to_language):
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]   
             
        argostranslate.package.uninstall( available_package )

