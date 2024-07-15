#new
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
        PrSol = data[circuit]['pression au sol']
        h = data[circuit]['altitude']
        Pr = data[circuit]['pression residuelle']

        Hbat = data[circuit]['hauteur total']
        Ldef = data[circuit]['longueur defini']

    elif 'cir' in circuit:
        RESULATATS.update({circuit:{}})
        RESULATATS[circuit].update({"Remarque":'',
                                    "Pression origine 'Por'":0,
                                    "Pression au sol":0,
                                    "Suffisance de pression":0,
                                    "Vitesse Reel de Circulation 'Vrm'":0,
                                    "Verification 'Vrm'":0,
                                    "Perte de charge conduite montante 'Jm'":0,
                                    "Perte de charge 'Jr'":0,
                                    "charge hydrolique":0,
                                    "hauteur de chute minimal":0,
                                    "Pression disponible":0})
        Jc , Qn , Pdk= 0, 0 , 0
        for troncon in data[circuit].keys() :
            Qbt,Kt,Nt,Qnt,Jt=0,0,0,0,0 
            Pdk_t = 0
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
                    Qbt += qb*liste[1]
                  
            try :
                if PrSol <= h+Pr :
                    RESULATATS[circuit].update({
                        "Remarque":"Le dernier point de puisage ne peut en aucun cas être alimenté par le réseau public. C'est généralement le cas des I.G.H. Il faut installer un système adéquat pour palier à ce problème. "
                    })
                    Vt=1.5 ; Vt_ = 1
                else :
                    RESULATATS[circuit].update({
                        "Remarque":"Il y a possibilité que le dernier point de puisage soit alimenté. Une évaluation des pertes de charge sera faite pour vérifier cela."
                    })
                    Vt=2 ; Vt_ = 1.5

                Kt - (0.8*a)/sqrt(Nt-1)
                Qnt = Kt * Qbt
                if type_=='s' : Dt =1000*sqrt((4*0.001*Qbt)/(pi*Vt))
                elif type_=='m' : Dt =1000*sqrt((4*0.001*Qbt)/(pi*Vt_))

                Drt = [i for i in DIAMETRE if i >= Dt]
                Db = min(Drt)
                Vrt = (4*Qnt*0.001)/(pi*pow(Db*0.001 , 2))

                jt = 0.00092*(1-v)*pow(Vrt,1.75)*pow(Drt*0.001,-1.25)
                Jt+=jt*Lt*1.15
                Jc+=Jt
                
                RESULATATS[circuit][troncon].update({
                    "Debit de Base 'Qbt'": Qbt ,
                    "Nombre total d'appareil 'Nt'":Nt,
                    "Coefficient de simultaneite 'Kt'":Kt,
                    "Debit necessaire 'Qnt'": Qnt, 
                    #"Vitesse de circulation de l'eau 'Vt'":Vt,
                    "Diametre de conduite 'Dt'":Dt,
                    "Diametre reel 'Db'":Db,
                    "Vitesse reel de circulation 'Vrt'":Vrt,
                    "Verification 'Vrt'" : Vrt,
                    "Perte de charge unitaire 'jt'":Jt,
                    
                
                })
            except ValueError :
                RESULATATS[circuit][troncon].update({"Coefficient de simultaneite":'Value Error',
                                            "Nombre d'apparel" : Nt})
            except ZeroDivisionError :
                RESULATATS[circuit][troncon].update({"Coefficient de simultaneite":"ZeroDivisionError"})

            
    
        RESULATATS[circuit]["Perte de charge total"]=Jc
        val = Qn*3.6
        if 0<val<=2.5 : jb = 1.2
        elif 2.5<val<=5: jb = 3.5
        elif 5<val<=7.5: jb = 5
        elif 7.5<val<=10: jb = 8
        elif 10<val<=15: jb = 10
        elif val>15 : jb = 10
        Por = PrSol-jb

        RESULATATS[circuit]["Pression origine 'Por'"]=Por
        Jd = 0

        if type_=="s" :
            Pdk = Por-h
        if Por - Jd >= h + Pr:
            RESULATATS[circuit]["Suffisance de pression"]="La Pression origine de la compagnie distributrice est suffissante pour la distribution d'eau dans l'immeuble"

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




