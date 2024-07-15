import os 

def changeWordFromFile(paths : str , extension : str ):
    file_list=[]
    for f in os.listdir(paths) :
        if os.path.isfile(os.path.join(paths , f)) :
            if f.endswith(extension) :
                file_list.append(f)
    
    for file in file_list :
        with open(os.path.join(paths,file) , mode='r') as f:
            text=f.read()
            f.close()
        with open(os.path.join((paths+'\\newFile'),file) , mode='w') as f:
            text=text.replace('PySide2','PySide6')
            f.write(text)
            f.close()

changeWordFromFile(paths='D:\Programs\Python\QtPysideGestionBoutiqueVente1' 
    , extension='py')
