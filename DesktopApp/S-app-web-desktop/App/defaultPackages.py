import os
import argostranslate.package

class PackageInstaller:
    def __init__(self, package_directory="./packages"):
        self.package_directory = package_directory
    

    def is_package_installed(self, package_name):
        installed_packages = argostranslate.package.get_installed_packages()
        for package in installed_packages:
            if "-".join(package.package_path.name.split("-")[0:2]) == package_name:
                return True
        return False

    def install_language_package(self, package_path):
        # Load and install the package
        #package = argostranslate.package.Package(package_path)
        argostranslate.package.install_from_path(package_path)
        print(f"Installed package from {package_path}")


    def setup_default_packages(self):
        package_files = [
            "translate-en_fr.argosmodel",
            "translate-en_zh.argosmodel",
            "translate-fr_en.argosmodel"
        ]
        
        for package_file in package_files:
            package_path = os.path.join(self.package_directory, package_file)
            package_name = package_file.split('.')[0]
            
            if not self.is_package_installed(package_name):
                print(f"Installing package {package_name}...")
                self.install_language_package(package_path)
            else:
                print(f"Package {package_name} is already installed")



