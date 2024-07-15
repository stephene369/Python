from pathlib import Path


list_file = Path("C:\\Users\\steph\\Desktop\\Nouveau dossier\\").glob("*.*")
fil_name = []
fil_ext = []

#
for file in list_file:
    fil_ext.append(Path(file).stem)
    fil_name.append(Path(file).suffix)


# 
fil_ext