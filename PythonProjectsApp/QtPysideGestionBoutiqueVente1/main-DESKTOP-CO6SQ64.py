#Python moduls
# Local Moduls
from folder import Chemin , createPath 
from addarticle import *
from connexion import Conn , logBtnConn
from compute import *
from display import *
from placeholder import *
from autoCompleter import *
from insert import *
from dateheure import *
from login_ import * 
from signin import *
from changeShadow import changeRandom
from generatedb import *


# interface
from interface.interface02 import *

import sys

# Custom widgets

from Custom_Widgets import Widgets

# main class
class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(200, 140, 0, 0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        # APPLY JSON STYLESHEET
        changeRandom()
        Widgets.loadJsonStyle(self, self.ui)

        # creating folder 
        createPath()
        displayListe()       
        if not os.path.exists(Chemin('rootdb')) :
            defaulf_root('ste' , 'ste')
           

        #Connect variable
        self.C=['connected',' ']
        self.table='enable'
        
        # admin connexion function
        def root_con() :
            self.C=rootlogin(C=self.C , nameEd = self.ui.rootnameEd , 
                    passwEd=self.ui.rootpassEd ,msg=self.ui.msgLab ,
                    stack=self.ui.centralStacked , page=self.ui.homePage)
            
        # users connexion function
        def users_con() :
            self.C=userslogin(C=self.C , nameEd = self.ui.usersnameEd , 
                    passwEd=self.ui.userspassEd ,msg=self.ui.msgLab ,
                    stack=self.ui.centralStacked , page=self.ui.homePage)     


        # FUNCTIONS as root and as users Button Connection
        def as_root() :
            logBtnConn(nameEd=self.ui.rootnameEd , passEd=self.ui.rootpassEd ,
                stack=self.ui.loginSubPage , page=self.ui.root)
        def as_users() : 
            logBtnConn(nameEd=self.ui.usersnameEd , passEd=self.ui.usersnameEd ,
                stack=self.ui.loginSubPage , page=self.ui.users)

     
        # FUNCTIONS slide menu Button Connection
        def homeCon() :
            Conn(self.C , self.ui.centralStacked , self.ui.homePage)
        def formCon():
            Conn(self.C , self.ui.centralStacked , self.ui.formPage)
        def tableCon():
            Conn(self.C , self.ui.centralStacked , self.ui.tablePage)
            Conn(self.C , self.ui.stackedWidget_2 , self.ui.dbPage)
            display(data=Chemin('datab_c'), table=self.ui.dataBase)
        def articleCon() :
            Conn(self.C , self.ui.centralStacked , self.ui.articlePage)
            display(data=Chemin('datab_aritcle'),table=self.ui.articleDB)
        def saveCon():
            Conn(self.C , self.ui.centralStacked , self.ui.savePage)
        def usersCon():
            Conn(self.C , self.ui.centralStacked , self.ui.signPage)
            Conn(self.C , self.ui.stackedWidget_3 , self.ui.usersSign)
        def infosCon():
            Conn(self.C , self.ui.centralStacked , self.ui.infosPage)
        def changeCon():
            Conn(self.C , self.ui.centralStacked , self.ui.changePage)

        # Formulaire FUNCTION 
        setdateheure (heurelab = self.ui.heureLab , datelab=self.ui.dateLab)
        def otherConn() :
            Conn(self.C , self.ui.stackedWidget , self.ui.Autre)
            display(data=Chemin('datab_other'),table=self.ui.otherTable)
        def tableAddArticle():
            insert_price(articl=self.ui.articleCon , nombre=self.ui.nbArticle ,
                prix=self.ui.prixTotal)
            insert_liste_article(articl=self.ui.articleCon ,
                nombre=self.ui.nbArticle , prix=self.ui.prixTotal)
            Cumule(lineEdit=self.ui.cumuleEd)
            display(data=Chemin('datab_liste_article') , table=self.ui.tablelisteAchat)
        def saveForm() :
            insert(name=self.ui.nameEd , male=self.ui.maleRad ,
                     female=self.ui.femaleRad,heure=self.ui.heureLab,
                     date=self.ui.dateLab , users=self.C[1])
            cancel(male=self.ui.maleRad ,
                     female=self.ui.femaleRad , articl=self.ui.articleCon  , 
                     nombre= self.ui.nbArticle , prix=self.ui.prixTotal)
            displayListe() 
            display(data=Chemin('datab_liste_article') , table=self.ui.tablelisteAchat)         
            self.ui.nameEd.setText('')
        def cancelForm() :
            cancel( male=self.ui.maleRad ,
                     female=self.ui.femaleRad , articl=self.ui.articleCon  , 
                     nombre= self.ui.nbArticle , prix=self.ui.prixTotal)
            displayListe() 
            display(data=Chemin('datab_liste_article') , table=self.ui.tablelisteAchat)
            self.ui.nameEd.setText('')           
        def removeROW() :
            remove_row(row=self.ui.lineNumber.value())
            Cumule(lineEdit=self.ui.cumuleEd)
            display(data=Chemin('datab_liste_article') , table=self.ui.tablelisteAchat)
        def addArticle() :
            atcl_insert(designationEd=self.ui.designationEd , prixUni=self.ui.prixUnitaireEd ,
                dispo=self.ui.disponibleEd)
            display(data=Chemin('datab_aritcle'),table=self.ui.articleDB)        
        def cancelArticle () :
            cancel_atcl(designationEd=self.ui.designationEd , prixUni=self.ui.prixUnitaireEd)   

        #AUTRE FUNCTION
        def saveOther():
            addOther(objet=self.ui.otherEd , prix=self.ui.otherPrice)
            display(data=Chemin("datab_other"),table=self.ui.otherTable)            
        ##TABLE PAGE FUNCTIONS
        def Display() :
            display(data=Chemin('datab_c'), table=self.ui.dataBase)
            display(data=Chemin('datab_aritcle'),table=self.ui.articleDB)

        # Users Page FUNCTION
        def changeRootInfo() :
            root_signin(name=self.ui.nRootNameEd , password=self.ui.nRootPassEd ,
                confirm=self.ui.nRootPassConfirm)
        def addUsers() :
            users_signin(name_=self.ui.nUsersNameEd , password_=self.ui.nUsersPassEd ,
                confirm_=self.ui.nUsersPAssConfirm)
                
        # Table Button FUNCTIONS
        def moreInfo():
            usersComboItem(Combo=self.ui.usersCombo)
            dateComboItem(Combo=self.ui.dateCombo)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.dbPageInfo)

        def displayMoreInfoTable() :
            df=generate(usersCombo=self.ui.usersCombo,
                 dateCombo=self.ui.dateCombo,label=self.ui.moreInfoLab)
            
            display(data=df , table=self.ui.moreInfoTable)
        
        ## NANO FUNCTIONS        
        def nano () :
            Display()
            #Login
            holder(lineEd=self.ui.usersnameEd , texte="Enter users name")
            holder(lineEd=self.ui.userspassEd , texte='Enter your password')
            holder(lineEd=self.ui.rootnameEd , texte="Enter users name")
            holder(lineEd=self.ui.rootpassEd , texte="Enter users passeword")
            
            #Sign up
            holder(lineEd=self.ui.nUsersNameEd , texte="Enter users name")
            holder(lineEd=self.ui.nUsersPassEd, texte='Enter your password')
            holder(lineEd=self.ui.nUsersPAssConfirm , texte='Confirm password')

            holder(lineEd=self.ui.nRootNameEd , texte="Enter users name")
            holder(lineEd=self.ui.nRootPassEd, texte='Enter your password')
            holder(lineEd=self.ui.nRootPassConfirm, texte='Confirm password')

            # setting up maximum spinBox Value
            max(self.ui.nbArticle)
            max(self.ui.prixTotal)
            max(self.ui.prixUnitaireEd)
            max(self.ui.disponibleEd)
            max(self.ui.otherPrice)

            hidetexte(self.ui.userspassEd)
            hidetexte(self.ui.rootpassEd)
            
            try :
                Completeur(lineEdit=self.ui.articleCon)
            except  FileNotFoundError : return 0
            PriceCompleter(lineEdit=self.ui.lineEdit)
        nano()
        
        # fist view
        self.ui.centralStacked.setCurrentWidget(self.ui.loginPage)
        self.ui.loginSubPage.setCurrentWidget(self.ui.users)
        
        # login_Button and authentification clicked connection
        self.ui.rootConBtn.clicked.connect(root_con)
        self.ui.usersConBtn.clicked.connect(users_con)

        # as root and as button clik connection
        self.ui.asRootBtn.clicked.connect(as_root )
        self.ui.asUsersBtn.clicked.connect(as_users)

        # hide widget Button connection 
        self.ui.formBtn.clicked.connect(formCon)
        self.ui.tableBtn.clicked.connect(tableCon)
        self.ui.articleBtn.clicked.connect(articleCon)  
        self.ui.saveBtn.clicked.connect(saveCon)
        self.ui.usersBtn.clicked.connect(usersCon)
        self.ui.infosBtn.clicked.connect(infosCon)  
        self.ui.changeBtn.clicked.connect(changeCon)  


        #Form Page Button Connecxion 
        self.ui.saveFormBtn.clicked.connect(saveForm)
        self.ui.annulerFormBtn.clicked.connect(cancelForm)
        self.ui.deleteLineBtn.clicked.connect(removeROW)
        self.ui.addBtn.clicked.connect(tableAddArticle)
        self.ui.otherBtn.clicked.connect(otherConn)

        #Other Page Button Connection
        self.ui.saveOtherBtn.clicked.connect(saveOther)
        self.ui.backToFormBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Formulaire))

        # Article Page Button Connexion
        self.ui.addArticleBtn.clicked.connect(addArticle)
        self.ui.cancelArticleBtn.clicked.connect(cancelArticle)

        # Table Page Button Cnnexion
        self.ui.moreInfos.clicked.connect(moreInfo)
        self.ui.backToTableBtn.clicked.connect(lambda : self.ui.stackedWidget_2.setCurrentWidget(self.ui.dbPage))
        
        self.ui.displayMoreInfoBtn.clicked.connect(displayMoreInfoTable)
        
        # USERS PAGE BTN CONNECTION
        self.ui.addUserBtn.clicked.connect(addUsers)
        self.ui.newRootBtn.clicked.connect(changeRootInfo)
        self.ui.goToRootSign.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentWidget(self.ui.rootSign))
        self.ui.backToUsersSign.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentWidget(self.ui.usersSign))

        ########################################################################
        #QSTARWiDgets Animation
        
        self.ui.nano.clicked.connect(nano)
        #Animation 
        
        

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.ui.heureLab.setText(label_time)
 

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())


#MainWindow.setMinimumSize(QSize(1000, 800))
#MainWindow.resize(1500, 800)

from pandas import DataFrame
data={'nom' : ["ste"]}
data=DataFrame(data , index=2)

data=read_csv("")
