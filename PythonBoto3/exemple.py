from pathlib import Path 

m=Path(r"C:\Users\steph\Videos\music")

files = m.glob("X2*")

for file in files :
    print(file)
    file.replace( str(file).replace("X2Download.app-","") )

