import os
from os import path

def Chemin(chemin) : 
    user_path = os.path.expanduser('~')
    nano_path=user_path+"\\.nano"
    account_path = nano_path+"\\account"
    users_path=account_path+"\\users"
    root_path=account_path+"\\root"
    db_path=nano_path+"\\database"
    articleDB=db_path+"\\article"
    db_version_path=db_path+"\\per_users"
    setting_path=nano_path+"\\setting"
    rootdb=root_path+"\\admin.csv"
    usersdb=users_path+"\\users.csv"
    datab_c=db_path+"\\data_base.csv"
    datab_aritcle = articleDB + "\\article.csv"
    datab_liste_article=articleDB+"\\liste_article.csv"
    other_db_path=db_path+"\\autre"
    datab_other=other_db_path+"\\others.csv"


    all_path = [nano_path,account_path,users_path,root_path,
            db_path,db_version_path , setting_path , articleDB ,other_db_path ]
    all_file = [rootdb , usersdb ,datab_other , datab_c , datab_aritcle , datab_liste_article ]
    if chemin=='':
        return 0 
    else :
        return locals()[chemin]


def createPath() :
    #if not os.path.exists(Chemin('nano_path')) :
    for path_ in Chemin('all_path') :  
        os.makedirs(path_,exist_ok=True)


def createFile() :
    for file_ in Chemin('all_file') :
        if not os.path.exists(file_) :
            open(file_ , mode='w')


