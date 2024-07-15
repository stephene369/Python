from moviepy.editor import AudioFileClip 
from pathlib import Path

class Segment :

    def __init__(self ,folder:str , filename:str ,  sec:int ) -> None:
        self.folder = folder 
        self.sec = sec 
        self.filename = filename
        self.suffix = Path(self.filename).suffix
        self.audio = AudioFileClip(self.filename)

        if not Path(self.folder).exists() : Path(self.folder).mkdir()
        self.duration =  self.audio.duration
        print(self.filename , self.suffix)


    def segment(self) :
        total =  self.audio.duration 
        debut = 0 
        fin  = self.sec
        keep = True

        while keep :
            if fin <= total :
                name = str( Path(self.folder).joinpath(f"sub_{debut}-{fin}.wav")  )

                if not Path(name).is_file() : 
                    print(f"Writing {name}")
                    self.audio.subclip(debut , fin).write_audiofile(name)
                    debut=fin
                    fin +=self.sec
                else :
                    debut=fin
                    fin +=self.sec                    

            else :
                name = str( Path(self.folder).joinpath(f"sub_{debut}-{total}.wav")  )
                
                if not Path(name).is_file() :                 
                    print(f"Writing {name}")
                    self.audio.subclip(debut , total).write_audiofile(name)
                    keep = False
                else :
                    keep = False