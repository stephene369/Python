import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "fr"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)
print(translatedText)
# '¡Hola Mundo!'


import argostranslate.package
PORT = 8000
packages_from = [pkg.from_name for pkg in argostranslate.package.get_installed_packages()]
packages_to = [pkg.to_name for pkg in argostranslate.package.get_installed_packages()]

packages = [str(pkg) for pkg in argostranslate.package.get_installed_packages()]
packages_split = [ str(f).split(" → ")  for f in packages ]
packages_from = list(set([ str(f).split(" → ")[0]  for f in packages ]))
packages_from_to = {
    package:[ pack[1] for pack in packages_split if package==pack[0] ] for package in packages_from
    }
packages_from_to