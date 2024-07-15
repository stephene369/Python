6# app.py
from functools import wraps
from flask import Flask, render_template, abort,redirect , session , url_for
from App.login import AdminForm, StudentForm , AdminDb
from App.modules import GetModuleForm , GetSubModuleForm , ModuleDb , SubModuleDb
from App.modules import GetStudentForm , StudendDb , GetGradesForm , CreateField , GetGradeForm
from App.modules import SavedGrades 
from flask import request
import pandas as pd
import numpy as np
from wtforms import IntegerField
from flask_wtf import FlaskForm 
import json 
from pathlib import Path


from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import SelectField, SubmitField , StringField , IntegerField 
from wtforms.validators import DataRequired , Length , NumberRange
from wtforms import FormField , FieldList 
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
@app.route('/admin', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def admin():
    admin_form = AdminForm()
    
    if admin_form.validate_on_submit():
        # Le formulaire admin a été soumis avec succès
        username = admin_form.username.data
        password = admin_form.password.data
        
        # Faire quelque chose avec les données (par exemple, vérification des informations d'identification)
        adminDb = AdminDb()
        if adminDb.authenticate(username=username, password=password):
            
            session['user_id'] = username
            return redirect(url_for("dashboard"))

        else : 
        # Si les informations d'identification sont incorrectes, affichez un message d'erreur
            admin_form.username.errors.append('Nom d\'utilisateur ou mot de passe incorrect')
            CONNECTED = False


    return render_template('login.html', form=admin_form, student_form=StudentForm(), form_type='admin')


@app.route('/student', methods=['GET', 'POST'])
def student():
    student_form = StudentForm()


    if student_form.validate_on_submit():
        # Le formulaire étudiant a été soumis avec succès
        student_id = student_form.student_id.data
        # Faire quelque chose avec les données (par exemple, vérification des informations d'identification étudiantes)

    return render_template('login.html', form=AdminForm(), student_form=student_form, form_type='student')



@app.route("/subjects",methods=['GET', 'POST']) 
def subjects() : 
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')

    module_form = GetModuleForm()
    modulesDb = ModuleDb()
    modules=modulesDb.getModules()
    
    
    if module_form.validate_on_submit() : 
        module_name = module_form.module_name.data 
        module_id = module_form.module_id.data 

        
        if modulesDb.addModule(module_name, module_id): 
            return render_template('dashboard/subjects.html',
                           module_form=module_form,
                           modules=modules)
            
        else :
            module_form.module_name.errors.append('Id ou Module existe deja')
            return render_template('dashboard/subjects.html',
                           module_form=module_form,
                           modules=modules)
            
    return render_template('dashboard/subjects.html',
                           module_form=module_form,
                           modules=modules)


@app.route("/subsubjects" , methods=["POST","GET"]) 
def subsubjects() : 
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')
    
    modules = [i[0] for i in ModuleDb().getModulesNames()]
    
    sub_module_form = GetSubModuleForm()
    subModuleDb = SubModuleDb()
    submodules = subModuleDb.getSubModule()
    
    if not sub_module_form.validate_on_submit() : 
        module_name = sub_module_form.module_name.data        
        sub_module_name = sub_module_form.sub_module.data 
        sub_module_id = sub_module_form.sub_module_id.data
        sub_module_coef = sub_module_form.sub_module_coef.data     
        level = sub_module_form.level.data
        
        if module_name not in modules :
            try : 
                sub_module_form.module_name.errors.append("Module n'existe pas(Verifiez l'orthographe)")
            except Exception as e : 
                print(e)
        
        else :
            print("Saved : ",
                subModuleDb.addSubmodule(
                    id_sub_module=sub_module_id,
                    sub_module_name=sub_module_name,
                    module_name=module_name,
                    coefficient=sub_module_coef,
                    level=level
                )
            )
    
        return render_template("dashboard/subsubjects.html",
                           sub_form=sub_module_form,
                           modules=modules,submodules=submodules)

    else : 
        return render_template("dashboard/subsubjects.html",
                           sub_form=sub_module_form,
                           modules=modules,submodules=submodules)
    

@app.route("/addStudents",methods=["POST","GET"]) 
def students() : 
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')    

    get_student_form = GetStudentForm() 
    studentDb = StudendDb() 
    students = studentDb.getStudents()
    
    if get_student_form.validate_on_submit() : 

        first = get_student_form.first_name.data 
        last = get_student_form.last_name.data 
        mail = get_student_form.email.data  
        classe = get_student_form.classe.data
                
        if studentDb.addStudents(first = first, last = last, mail = mail , classe=classe) : 

            return render_template("dashboard/addStudents.html",students = students,
                                form=get_student_form)
        else : 
            get_student_form.email.errors.append('Email existe deja')
    else : 
        return render_template("dashboard/addStudents.html",
                        students=students,
                        form=get_student_form)
        
    return render_template("dashboard/addStudents.html",
                        students=students,
                        form=get_student_form)



@app.route("/grades" ,methods=['GET', 'POST'] )
def grades() :
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')
    
    form = GetGradesForm()

    existed_classes = [i[0] for i in StudendDb().getClasses()]
    
    if form.validate_on_submit() or not form.validate_on_submit()  :
        classe = form.classe.data

        if not classe in existed_classes : 
            #form.classe.errors.append('Classe inexistante')
            return render_template("dashboard/grades.html",
                    form=form)
        else  : 
            students = StudendDb().getStudents(classe=classe)
            moduleAndSub = SubModuleDb().getModuleAndSub(classe=classe)
            
            taille = len(students)
            with open("settings.json" , 'w' ) as f : 
                data = {"Students":taille , 
                        "Classe":classe}
                json.dump(data, f)
                
            print("taille = " , taille)

        return redirect(url_for("gradesUpdate"))


@app.route("/grade" , methods=["GET", "POST"])
def grade(): 
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')
    
    form = GetGradeForm()
    
    if form.validate_on_submit() :
        id_ = form.id_.data
        classe = form.classe.data
        module = form.module.data 
        sub_module = form.sub_module.data
        note = form.note.data 
        
        ids = StudendDb().getIds()
        classes = set([p[0] for p in StudendDb().getClasses()])
        moduleAndSub = SubModuleDb().getModuleAndSub(classe=classe)
        matieres = [i[0] for i in moduleAndSub  ]
        matieres_modules = [[ i[0] , i[1] ] for i in moduleAndSub ]
        
        
        if id_ not in ids :
            form.id_.errors.append('Id inexistante')
            return render_template("dashboard/grade.html",
                    form=form)

        if classe not in classes : 
            form.classe.errors.append('Classe inexistante')
            return render_template("dashboard/grade.html",
                    form=form)
        
        if module not in matieres :
            form.module.errors.append('Module inexistante')
            return render_template("dashboard/grade.html",
                    form=form)
        
        if [module , sub_module] not in matieres_modules :
            form.sub_module.errors.append('Sub-module inexistante pour ce module')
            return render_template("dashboard/grade.html",
                    form=form)
        
        names = StudendDb().getNames(id_)
        nom , prenom , mail = names[0]
        
        file_path = f"database/grades/class-{classe}.csv"
        col = f"{module}-{sub_module}"
        if Path(file_path).exists() : 
            df = pd.read_csv(file_path ,index_col="Ids" )
            df.at[ id_ , col  ]= note
            df.to_csv(file_path)
            
            succes_message = f"Note ajouter avec succes pour {nom}  {prenom}"
            
            return render_template("dashboard/grade.html",
                        form=form, 
                        success_message=succes_message)
        else : 
            data = {
                "Nom":[nom],
                "Prenom":[prenom],
                "Email":[mail],
            }
            df = pd.DataFrame(data)
            df = df.rename( {0:id_} )
            df.loc[ id_, col  ]= note
            
            df.to_csv(file_path , index_label="Ids" )
            
            succes_message = f"Note ajouter avec succes pour {nom}  {prenom}"
            
            return render_template("dashboard/grade.html",
                        form=form, 
                        success_message=succes_message)
    
    
    
    return render_template("dashboard/grade.html",
                        form=form)
    


@app.route("/gradesUpdate" ,methods=['GET', 'POST'] )
def gradesUpdate() :
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')

    existed_classes = [i[0] for i in StudendDb().getClasses()]
    with open("settings.json" ,"r") as f : 
        data = json.load(f)        
        classe = data['Classe']

    students = StudendDb().getStudents(classe=classe)
    moduleAndSub = SubModuleDb().getModuleAndSub(classe=classe)
                
    ids = [i[0] for i in students]
    prenom = [i[1] for i in students]
    nom = [i[2] for i in students]
    classe_ = [i[3] for i in students]
    mail = [i[4] for i in students]
    
    matieres_modules = [ i[0]+f"-{i[1]}" for i in moduleAndSub ]
    coefficients = [i[2] for i in moduleAndSub] 
    
    col = ["Ids","Prenom","Nom","Email","Note"]
    for i in matieres_modules : col.append(i) 
    
    with open("settings.json" , "r+") as f : 
        data = json.load(f)
        data["matieres_modules"] = matieres_modules
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()
        
    
    class StudentNote(FlaskForm) : 
        note = IntegerField(validators=[DataRequired(),
                    NumberRange(min=0,max=20) ])

    class StudentsNote(FlaskForm) :
        pass 
    
    class StudentGradeForm(FlaskForm):
        student_id = StringField('ID de l\'étudiant')
        first_name = StringField('Prénom')
        last_name = StringField('Nom de famille')
        email = StringField('Email')
        
        with open("settings.json", "r") as f : 
            data = json.load(f)
            matieres_modules = data["matieres_modules"]
            f.close()

        notes = FieldList(FormField(StudentNote), min_entries=len(matieres_modules) )
        matieres_modules = matieres_modules
        print("Matieres - modules : " , matieres_modules)
        

    class StudentsGradeForm(FlaskForm):        
        try : 
            with open("settings.json" ,"r") as f : 
                data = json.load(f)
                n = data['Students']
                cls = data['Classe']
        except Exception as e : print (e) ; n = 0
        
        classe = StringField("Classe : ")
        students = FieldList(FormField(StudentGradeForm), min_entries=n)
        submit = SubmitField('Soumettre')

    form = StudentsGradeForm()
    
    
    data = {}
    value = [ids , prenom , nom , mail , classe_ , mail]
    for i in range(5) : 
        data[col[i]] = value[i]

    database_name = f"database/grades/class-{classe}.csv"    
    database_parameters_name = f"database/grades/class-{classe}.json"      
    

    if Path(database_name).exists() : 
        df = pd.read_csv(database_name , index_col="Ids")
        #print(df)
    
    form.students[0].notes[0].data['note'] = 1
    
    print(form.students[0].notes[0].data)


    for (i , student ) in enumerate(form.students )  : 
        student.student_id.data = ids[i]
        student.first_name.data = prenom[i]
        student.last_name.data = nom[i]
        student.email.data = mail[i]
        #student.notes[0].data = 1
        
    if not form.validate_on_submit() :
        print("Running")
        students_data = []
        for student_form in form.students:
            student_data = {
                'Ids': student_form.student_id.data,
                'Prenom': student_form.first_name.data,
                'Nom': student_form.last_name.data,
                'Email': student_form.email.data,
            }
            for i , note in enumerate(student_form.notes) :
                student_data[ matieres_modules[i] ] = note.data['note']
            students_data.append(student_data)

        # Créer un DataFrame pandas à partir des données
        df = pd.DataFrame(students_data)
        df.to_csv(database_name)
        with open(database_parameters_name , "w") as f :
            d = {
                "matieres" : matieres_modules , 
                "coefficients" : coefficients
            }
            json.dump(d,f,indent=4)
            f.close()
        
        return render_template("dashboard/gradesUpdate.html",
            form = form,matieres_modules=matieres_modules )        

    return render_template("dashboard/gradesUpdate.html",
            form = form,matieres_modules=matieres_modules)
    
    
@app.route("/search")
def search() :
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')

    return render_template("dashboard/search.html")



@app.route("/addAdmin")
def addAdmin() :
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')    
    
    return render_template("dashboard/addAdmin.html")



@app.route('/logout')
def logout():
    # Effacer la variable de session pour déconnecter l'utilisateur
    
    session.pop('user_id', None)
    return redirect(url_for('admin'))



@app.route('/dashboard')
def dashboard():
    # Ajoutez ici la logique pour empêcher le retour à la page de connexion une fois connecté
    # Cela Noneession utilisateur    
    if 'user_id' not in session:
        return render_template('login.html', form=AdminForm(), student_form=StudentForm(), form_type='admin')

    classes = set([p[0] for p in StudendDb().getClasses()])
    
    matiere = {}
    
    for classe in classes : 
        matiere.update({ classe : {} })
        modules = [i[1] for i in ModuleDb().getModules()]
        for module in modules : 
            #print(SubModuleDb().getSubModuleLevel(classe , module))
            matiere[classe].update({ module:{}  })
            for sub_coef in SubModuleDb().getSubModuleLevel(classe , module) : 
                matiere[classe][module].update(
                    {sub_coef[0]:sub_coef[1]} )
                
    #matiere= json.dumps(mati0
