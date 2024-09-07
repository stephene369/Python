import os
import argostranslate.package


import os
from enum import Enum
from pathlib import Path
import zipfile


TRUE_VALUES = ["1", "TRUE", "True", "true"]

debug = os.getenv("ARGOS_DEBUG") in TRUE_VALUES

dev_mode = os.getenv("ARGOS_DEV_MODE") in TRUE_VALUES

home_dir = Path.home()
if "SNAP" in os.environ:
    home_dir = Path(os.environ["SNAP_USER_DATA"])

data_dir = (
    Path(os.getenv("XDG_DATA_HOME", default=home_dir / ".local" / "share"))
    / "argos-translate"
)
os.makedirs(data_dir, exist_ok=True)

# ARGOS_TRANSLATE_PACKAGES_DIR deprecated 1.2.0
legacy_package_data_dir = Path(
    os.getenv("ARGOS_TRANSLATE_PACKAGES_DIR", default=data_dir / "packages")
)
package_data_dir = Path(os.getenv("ARGOS_PACKAGES_DIR", legacy_package_data_dir))
os.makedirs(package_data_dir, exist_ok=True)


class PackageInstaller:
    def __init__(self, package_directory="./App/packages"):
        self.package_directory = package_directory



    def is_package_installed(self, package_name):
        installed_packages = argostranslate.package.get_installed_packages()
        for package in installed_packages:
            if ("-".join(package.package_path.name.split("-")[0:2]) == package_name[:-4]) or ("-".join(package.package_path.name.split("-")[0:2]) == package_name) :
                return True
        return False


    def install_package(self, package_path):
        with zipfile.ZipFile(package_path, 'r') as zip_ref:
            print(f"Extracting {package_path} to {package_data_dir}")
            zip_ref.extractall(path=package_data_dir)
    def install_language_package(self, package_path):
        with zipfile.ZipFile(package_path, 'r') as zip_ref:
            print(f"Extracting {package_path} to {package_data_dir}")
            zip_ref.extractall(path=package_data_dir)


    def setup_default_packages(self):
        package_files = [
            "translate-en_fr-1_9.zip",
            "en_ja.zip",
            "translate-fr_en-1_9.zip"
        ]
        
        for package_file in package_files:
            package_path = os.path.join(self.package_directory, package_file)
            package_name = package_file.split('.')[0]
            
            if not self.is_package_installed(package_name):
                print(f"Installing package {package_name}...")
                self.install_package(package_path)
            else:
                print(f"Package {package_name} is already installed")



p = PackageInstaller()
p.package_directory

package_files = [
    "translate-en_fr-1_9.zip",
    "en_ja.zip",
    "translate-fr_en-1_9.zip"
]

for package_file in package_files:
    package_path = os.path.join(p.package_directory, package_file)
    package_name = package_file.split('.')[0]

    installed_packages = argostranslate.package.get_installed_packages()
    for package in installed_packages:
        if ("-".join(package.package_path.name.split("-")[0:2]) == package_name[:-4]) or ("-".join(package.package_path.name.split("-")[0:2]) == package_name) :
            print(package_name,True)

