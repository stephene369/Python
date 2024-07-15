from speech_recognition import Recognizer , AudioFile,AudioSource
from pathlib import Path 


class Reconnaisseur(Recognizer) :
    def __init__(self , folder:str ):
        super().__init__()
        
        self.folder = Path(folder)

        self.files = self.folder.glob(f"*.wav")

    def reconnaisseur(self) :
        texts = ''
        for file in self.files :

            print(f"Recongnizing {file}")

            with AudioFile(str(file)) as source :
                audio = self.record(source)

                try : 
                    t = self.recognize_google(audio)
                    print(1)

                    print(f"{file} texte = {t}")
                    texts+= t
                    texts+= "\n"
                except Exception as e :
                    print(e)
                    
        return texts
