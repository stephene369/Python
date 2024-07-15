import os
from pathlib import Path
from print_color import print
from tqdm import tqdm
import time

path_=r"D:\Projects\MesProjets\PythonProject\rangeFileByFolder\files"
# liste file and dir in path

liste_file_ = os.listdir(path_) 

liste_suffix = [] 
for i in liste_file_ :
    liste_suffix.append(Path(i).suffix)
liste_suffix=set(liste_suffix) # removing duplicated suffix

# for a specifie suffix

for suffix_ in (liste_suffix) :

    destination_path_ = os.path.join(path_ ,suffix_+"_Files") 

    if not os.path.exists(destination_path_) and suffix_!='':
        os.makedirs(destination_path_,exist_ok=False)

    print(suffix_ +" Files",tag="Start moving" , tag_color='green' ,color='blue' )
    
    for file_name in tqdm(liste_file_ ,  bar_format="") :        
        if Path(file_name).suffix==suffix_ :
            src = os.path.join(path_ ,file_name)
            dst = os.path.join(destination_path_,file_name)

            if os.path.isfile(src) :
                try : 
                    os.rename(src , dst )
                except FileExistsError :
                    pass
        time.sleep(.2)
                


