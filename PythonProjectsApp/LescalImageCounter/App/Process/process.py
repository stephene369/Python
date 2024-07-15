from ..Lib import *

from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.morphology import (erosion, dilation, closing, opening, area_closing, area_opening)
from skimage.measure import label, regionprops
import matplotlib.pyplot as plt


class ShowImageProcessus(QThread) :
    signal = pyqtSignal(dict)
    
    def __init__(self , filepath, imageLab:ImageLabel) :   
        super().__init__()

        d = datetime.now()
        name = str(d).replace(":","").replace("-","").replace(" ","")
        self.chemin = Path.cwd().joinpath(f"History\Images\{name}.png") 
        self.chemin = str(self.chemin)
        print(self.chemin)

        self.filepath = filepath
        self.imagelab = imageLab
        self.image = Image.open(self.filepath)


        self.p = 360/self.image.height
        w = int(self.image.width*self.p)
        h = int(self.image.height*self.p)

        import pprint
        pprint.pprint({"image size : " : self.image.size , "new property : " : self.p ,"new image size : " : {"w" : w ,"h" : h} , "memoryview" : memoryview},indent=4)
        self.image = self.image.resize((w,h))
        self.image.save(self.chemin)

    def run(self) :
        self.msleep(2000)
        self.imagelab.setImage(self.chemin)   
        self.signal.emit({0:self.chemin , 1:self.p})


class ShowImage(QThread) :
    signal = pyqtSignal(dict)
    
    def __init__(self , filepath, imageLab:ImageLabel) :   
        super().__init__()

        self.filepath = filepath
        self.imagelab = imageLab

    def run(self) :
        self.msleep(2000)
        self.imagelab.setImage(self.chemin)   
        self.signal.emit({})




class EasyCountProcess(QThread) :
    signal = pyqtSignal(dict)
    
    def __init__(self , filePath ,imagelab:ImageLabel) :
        super().__init__()
        self.imagelab = imagelab

### FilePath est le chemin vers l'Image 
        self.filePath = filePath
        self.image = Image.open(self.filePath)

### Chemin vers lequel enregister l'image a la fin du processus
        self.chemin = str(Path(self.filePath).parent)
        self.chemin = Path(self.chemin).joinpath(str(Path(self.filePath).stem) + "--counted.png")
        self.chemin = str(self.chemin)

### Esay Count Processus 
    def run(self) :
        depart = datetime.now()

    ## Ecrivez le Processus ICI
        print(self.filePath)
        print(self.chemin)  
#
        self.resultat = self.countElements(image_path=self.filePath , destination=self.chemin,size=self.image.size)
        ## enregistrement de l'Image
        self.msleep(1000)
        print("IMage saved")

        ## Indiquer le nombre d'element ici 
        self.elements = self.resultat[1]    
### 
        try : 
            ms = 5000//self.elements
        except Exception as e : 
            print(e)
            ms = 1

        if ms ==0 : ms = 1
        i=0
        for i in range(1,self.elements) :
            self.signal.emit({0:i, 1:(i/self.elements)*200})
            self.msleep(ms)

        self.msleep(3000)
        self.imagelab.setImage(self.chemin)

        
        if Path("History\history.json").exists() :
            try : 
                with open("History\history.json","r") as js :
                    data = json.load(js)
            except Exception : 
                with open("History\history.json","w") as js :
                    js.write( json.dumps([{"TOTAL":0},[]] , indent=4))    
        else :    
            with open("History\history.json","w") as js :
                js.write( json.dumps([{"TOTAL":0},[]] , indent=4))    

        with open("History\history.json","r") as js :
            data =  json.load(js)
        

        data[0]["TOTAL"]+=1
        self.im = Image.open(self.chemin)
        data[1].append({
            "image":self.filePath,
            "image-infos":{
                "wh":self.image.size,
                "size":Path(self.filePath).stat().st_size
            },
            
            "image-counted":self.chemin,
            "image-counted-infos":{
                "wh":self.im.size,
                "size":Path(self.chemin).stat().st_size
            },
            "count":self.elements,
            "time":str(datetime.now()),
            "diff":str(datetime.now()-depart)
        })

        with open("History\history.json","w") as js :
            js.write(json.dumps(data, indent=4))

        self.signal.emit({0:i, 1:0})



    def countElements(self, image_path , destination , size):
        # lecture image
        print("debut du processus")
        im = imread(image_path)
        
        # Pre Traitement selon la nature de l'image
        if len(im.shape) == 2:
            pass
        elif len(im.shape) == 3:
            if im.shape[2] == 3:
                im = rgb2gray(im)
            elif im.shape[2] > 3:
                im = im[:,:,:3]
                im = rgb2gray(im)
                
        # Binarisation
        seuil_otsu = threshold_otsu(im)
        im = im < seuil_otsu
        
        # operations morphologiques
        im_morph = area_closing(area_opening(im, 201), 201)
        
        # labelling
        label_im = label(im_morph)
        
        # extraction blobs
        props = regionprops(label_im)

        area_list = []
        for prop in props:
            area_list.append(prop.area)
        mini = min(area_list)
        
        # comptage et affichage des blob identifiés
        fig, ax = plt.subplots(figsize=(18, 8))
        ax.imshow(label_im)

        count = 0
        for i, prop in enumerate(filter(lambda x: x.area > mini, props)):
            y1, x1, y2, x2 = (prop.bbox[0], prop.bbox[1],
                            prop.bbox[2], prop.bbox[3])
            width = x2 - x1
            height = y2 - y1
            r = plt.Rectangle((x1, y1), width = width, height=height, color='b', fill=False)
            plt.xticks([])
            plt.yticks([])
            ax.add_patch(r)
            count += 1
            
        # enregistrer l'image traitée
        plt.savefig(destination, bbox_inches='tight', pad_inches=0)

        Image.open(destination).resize(size).save(destination)

        # retourner l'image traitée et le nbre d'éléments
        print("Fin du processus")
        return [label_im, count] 