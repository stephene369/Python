import os
from pathlib import Path
from print_color import print
import pandas as pd

path_=r"E:"
liste_file_ = os.listdir(path_) # liste file and dir in path

print(liste_file_ , color='blue')

liste_suffix = [Path(i).suffix for i in liste_file_] 
liste_suffix=set(liste_suffix) # removing duplicated suffix
print(liste_suffix , color='blue')

# for a specifie suffix
for suffix_ in liste_suffix:  

 	# create destination path : expl : /folder/.zip_file/
    destination_path_ = os.path.join(path_, suffix_+"_Files")

 	# create folder if not already exists and suffix is not a folder suffix
    if not os.path.exists(destination_path_) and suffix_ != '':
        os.makedirs(destination_path_, exist_ok=False)

	# for each file , if suffix == specific suffix create source path and destination path
    for file_name in liste_file_:
        if Path(file_name).suffix == suffix_:
            src = os.path.join(path_, file_name)
            dst = os.path.join(destination_path_, file_name)

			# if source is file try to move it
            if os.path.isfile(src):
                try:
                    os.rename(src, dst)
                except Exception as e: print(e)
            else:
                print(src, tag='This is not a file', tag_color='black',
                      color='black')


