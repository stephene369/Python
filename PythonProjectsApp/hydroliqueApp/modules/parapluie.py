import json
from math import sqrt , pi


DATA =  open("../db/data.json" )
DIAMETRE = [1,2,3,30,40,60]
DIAMETRE_Rm = [12,23,45,67,87]
RESULATATS = {}

data = json.load(DATA)
data.keys()
for circuit in list(data.keys()) :
    if circuit=='immeuble' :
        match str(data['immeuble']['usage']) :
            case "Hotel de tourisme" : a = 1.25
            case 'Hotel de séjour' : a =1.25
            case 'Foyers de jeunes travailleurs' : a= 1.25
            case 'Bureau' : a=1
            case 'Maison de retraite' : a=1
            case 'Foyer de personne âgées': a=1
            case 'Hôtels de sports d\'hiver':  a = 1.5
            case 'Hôtels à clientèle spécifique' : a = 1.5
            case "Cantines" : a =1.5
            case "Restaurents" :a = 1.5
            case "Sanitaires publics" :a = 1.5
            case "Ecoles" : a = 1
            case "Internats" :a = 1
            case "Stades" :a = 1
            case "Gymnases":a = 1
            case "Casernes":a = 1
        L = data[circuit]["longueur total"]
        match data[circuit]['categorie'] :
            case 'Plastique' : v = 0
            case "Cuivre" : v = 0.15 
            case "Acier galvaniser" : v = 0.1
        Hbat = data[circuit]['hauteur total']
        Ldef = data[circuit]['longueur defini']
        Pr = data[circuit]['pression reel']
        h = data[circuit]['hauteur']

    else :
        RESULATATS.update({circuit:{}})
        RESULATATS[circuit].update({"Perte de charefge total":0})
        RESULATATS[circuit].update({"Dimensionnement conduite montante":0})
        RESULATATS[circuit].update({"Vitesse Reel de Circulation 'Vrm'":0,
                                    "Verification 'Vrm'":0,
                                    "Perte de charge conduite montante 'Jm'":0,
                                    "Perte de charge 'Jr'":0,
                                    "charge hydrolique":0,
                                    "hauteur de chute minimal":0,
                                    "Pression disponible":0})
        Jc , Qn = 0, 0
        for troncon in data[circuit].keys() :
            Qbt,Kt,Nt,Qnt,Jt=0,0,0,0 ,0
            RESULATATS[circuit].update({troncon:{}})

            for categorie in data[circuit][troncon].keys() : 
                if categorie =='longueur' :
                    Lt = data[circuit][troncon][categorie]

                elif categorie == 'type' :
                    match data[circuit][troncon]['type'] :
                        case "Colonne montante":
                            Vt = 2 ; _ht = Lt ; type_='m'
                        case "Canalisation en sous-sol" :
                            Vt = 1.5 ; _ht = 0 ; type_ = 's'
                
                else :
                    liste = data[circuit][troncon][categorie]
                    match int(liste[0][:2]) :
                        case 1: qb = 0.2
                        case 2: qb = 0.2
                        case 3: qb = 0.05
                        case 4: qb = 0.20 
                        case 5: qb = 0.33
                        case 6: qb = 0.20
                        case 7: qb = 0.33
                        case 8: qb = 0.42
                        case 9: qb = 0.12
                        case 10: qb = 1.5
                        case 11: qb = 0.15
                        case 12: qb = 0.1
                        case 13: qb = 0.33
                        case 14: qb = 0.2
                        case 15: qb = 0.1
                    if liste[1] != 0 : Nt+=1
                    Qbt += (qb * liste[1])

            try : 
                Kt += (0.8*a)/(sqrt(Nt-1))
                Qnt = Kt * Qbt
                Dt = 1000*sqrt((0.001*4*Qnt)/(pi*Vt))
                Drt = [i for i in DIAMETRE if i >=Dt] ; Db = min(Drt)
                Drt = Db
                Vrt = (4*Qnt*0.001)/(pi*((Drt*0.001)**2))
                if type_=='m' and Vrt >=1: B=True 
                elif type_ == 'c' and Vrt>=0.5 : B=True
                else :B=False

                jt = 0.00092*(1-Vt)*pow(Vrt,1.75)*pow(Drt*0.001,-1.25)
                Jt = jt*Lt*1.15
                Jc += Jt
                Qn += Qnt

                RESULATATS[circuit][troncon].update({
                    "Debit de Base 'Qbt'": Qbt ,
                    "Nombre total d'appareil 'Nt'":Nt,
                    "Coefficient de simultaneite 'Kt'":Kt,
                    "Debit necessaire 'Qnt'": Qnt, 
                    "Vitesse de circulation de l'eau 'Vt'":Vt,
                    "Diametre de conduite 'Dt'":Dt,
                    "Diametre reel 'Db'":Db,
                    "Vitesse reel de circulation 'Vrt'":Vrt,
                    "Verification 'Vrt'" : B,
                    "Perte de charge unitaire 'jt'":jt,
                    "Perte de charge total 'Jt'":Jc,
                
                })
            except ValueError :
                RESULATATS[circuit][troncon].update({"Coefficient de simultaneite":'Value Error',
                                            "Nombre d'apparel" : Nt})
            except ZeroDivisionError :
                RESULATATS[circuit][troncon].update({"Coefficient de simultaneite":"ZeroDivisionError"})

        RESULATATS[circuit]["Perte de charefge total"]=Jc
        Dm = 1000 * sqrt( (4*0.001*Qn)/(pi*Vt)  )
        RESULATATS[circuit]["Dimensionnement conduite montante"] = Dm
        drm = [i for i in DIAMETRE_Rm if i >= Dm] 
        Drm = min(drm)
        Vrm = (4*Qn*0.001)/(pi*pow(Drm*0.001 , 2))
        if Vrm >=0.5 : B=True 
        else : B=False
        Vch = Vrm
        jm =( 0.00092*(1-v)*pow(Vrm,1.75)*pow(Drm*0.001,-1.25))
        Jm = jm*L*1.15
        
        jr = (0.00092*(1-v)*pow(Vch,1.75)*pow(Db,-1.25))*Ldef
        Hres = h+Pr+jr
        Hch = Hres-Hbat
        RESULATATS[circuit]["Vitesse Reel de Circulation 'Vrm'"] = Vrm
        RESULATATS[circuit]["Verification 'Vrm'"] = B
        RESULATATS[circuit]["Perte de charge conduite montante 'Jm'"]=Jm
        RESULATATS[circuit]["Perte de charge 'Jr'"] = jr
        RESULATATS[circuit]["charge hydrolique"] = Hres
        RESULATATS[circuit]["hauteur de chute minimal"] = Hch
            
for circuit in data.keys() :
    if 'cir' in circuit :
        for troncon in data[circuit].keys() :
            
            
            pass

with open ("../db/resulats.json" ,'w') as f:
    f.write(json.dumps(RESULATATS , indent=4))
    f.close()




