import argostranslate.package
import argostranslate.translate
from print_color import print

# language code

from_code = input("From language) : ")
to_code = input("To (language) : ")

# Downloads remote package index
argostranslate.package.update_package_index()

# availible package 
available_packages = argostranslate.package.get_available_packages()

# download function of packages
package_to_install = next(filter(lambda x: x.from_code == from_code
                and x.to_code == to_code, 
                        available_packages))

print(f'Downloading language package {from_code}->{to_code} . . .',
        format='bold',tag='start of the download',
            tag_color='green' ,color= 'yellow' )

# download and install language package file
argostranslate.package.install_from_path(package_to_install.download())

# offline translation
texte="cette traduction est hors ligne"
translatedText = argostranslate.translate.translate(texte, from_code, to_code)

print('\n',texte , end=' ' , color = 'black' )
print(translatedText.capitalize()+'\n' , tag=f'{from_code}->{to_code}'
            ,tag_color='green',color='blue' , background='' )
