from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import SelectField, SubmitField , StringField , IntegerField 
from wtforms.validators import DataRequired , Length , NumberRange
from wtforms import FormField , FieldList 
import json
from pathlib import Path
import sqlite3
import random
import uuid
import os

class GetModuleForm(FlaskForm):
    label = 'Ajouter un module'
    
    module_name = StringField('Module', 
                validators=[DataRequired(),Length(min=4)] )
    
    module_id = StringField('Id Module', validators=[DataRequired(),
                        Length(min=2)])
    
    submit = SubmitField('Ajouter')
    
class CreateField(FlaskForm) :
    
    new_int_field = IntegerField()
    
    def IntFieldList(self , number) :        
        return [IntegerField("UnNumbre",validators=[NumberRange(min=0 , max=20)]) for i in range(number)]

class SavedGrades(FlaskForm) :
    
    write = StringField(validators=[DataRequired(), Length(min=3,max=3,message="Yes") ])
    save = SubmitField("Enregistrer")


class GetSubModuleForm(FlaskForm) : 
    

    label = 'Ajouter un sous-module' 

    module_name = StringField('Entrer le nom du module', 
                validators=[DataRequired(),Length(min=4)] )
    
    sub_module = StringField("Sous-Module",
                    validators=[DataRequired(),
                                Length(min=4)] )
    
    sub_module_id = StringField('Id Sub-Module', 
                    validators=[DataRequired(),Length(min=2)])
    
    sub_module_coef = IntegerField("Coefficient du Sous-Module", 
                    validators=[DataRequired(),NumberRange(min=1)])
    
    level = StringField('Classe', 
                    validators=[DataRequired(),Length(min=2)])
    
    submit = SubmitField("Ajouter")


class GetStudentForm(FlaskForm) :
    label = 'Ajouter un étudiant' 
    
    first_name = StringField('Prénom', 
                validators=[DataRequired(),Length(min=4)] )
    
    last_name = StringField('Nom', 
                validators=[DataRequired(),Length(min=4)] )
    
    email = StringField('Email', 
                validators=[DataRequired(),Length(min=4)] )
    
    classe = StringField("Classe", 
                validators=[DataRequired(),Length(min=2)])
    
    submit = SubmitField("Ajouter")



class GetGradeForm(FlaskForm) : 
    id_ = StringField("Id Etudiant", 
            validators=[DataRequired(),Length(min=6)  ]  )
    
    classe = StringField(
        "Classe",
        validators=[DataRequired()]
    )
    
    module = StringField("Module", 
            validators=[DataRequired(),Length(min=4)  ]  )
    
    sub_module = StringField("Sous-Module", 
            validators=[DataRequired(),Length(min=4)  ]  )
    
    note = IntegerField("Note", 
            validators=[DataRequired(),NumberRange(min=0,max=20)]  )
    
    submit = SubmitField("Ajouter")




class ModuleDb : 
    def __init__(self) -> None:
            
        self.connection()

        # Création de la table modules
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS modules (
                id_module TEXT PRIMARY KEY,
                module_name TEXT UNIQUE )
        """)
        self.close()
    
    def addModule(self, module_name , module_id) : 
        try : 
            self.connection()
            self.cur.execute("""INSERT INTO modules (id_module, module_name) 
                            VALUES (?,?) """, (module_id, module_name))
            self.close()
            return True 
        except Exception : 
            self.close()
            return False
        
    def getModules(self) :
        self.connection()
        modules = self.cur.execute("SELECT * FROM modules").fetchall()
        self.close()
        return modules
    
    def getModulesNames(self) :
        self.connection()
        modules = self.cur.execute("SELECT module_name FROM modules").fetchall()
        self.close()
        return modules
    
    def connection(self) :
        self.conn = sqlite3.connect("database/modules/modules.db")
        self.cur = self.conn.cursor()
    
    def close(self) : 
        self.cur.close()
        self.conn.commit()
    


class SubModuleDb : 

    def __init__(self) -> None:
            
        self.connection()

            # Création de la table modules
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS subModules (
                id_sub_module TEXT PRIMARY KEY,
                sub_module_name TEXT ,
                module_name TEXT,
                coefficient INTEGER,
                level TEXT
            )
        """)
        self.close()    
    
    def addSubmodule(self, id_sub_module , sub_module_name, 
                    module_name, coefficient,level) :
        self.connection()
        try : 
            self.cur.execute("""INSERT INTO subModules (id_sub_module, sub_module_name, module_name, coefficient, level) VALUES (?,?,?,?,?) """, (id_sub_module, sub_module_name, module_name, coefficient,level))
            self.close()
            return True
        except Exception as e: 
            print(e)
            self.close()
            return False

    def getSubModule(self) : 
        self.connection()
        subModules = self.cur.execute("""SELECT * FROM subModules""").fetchall()
        self.close()
        return subModules
    
    def getModuleAndSub(self ,classe) :   
        self.connection()
        ModulesAndSub = self.cur.execute("""SELECT module_name , sub_module_name  , coefficient FROM subModules WHERE level = ?""",(str(classe), )).fetchall()
        self.close()
        return ModulesAndSub

    def getSubModuleLevel(self ,classe,module) :   
        self.connection()
        SubModulesLevel = self.cur.execute("""SELECT sub_module_name  , coefficient FROM subModules WHERE level = ? AND module_name = ?""",(str(classe) , str(module), )).fetchall()
        self.close()
        return SubModulesLevel
    
    
    def connection(self) :
        self.conn = sqlite3.connect("database/modules/modules.db")
        self.cur = self.conn.cursor()
    
    
    def close(self) : 
        self.cur.close()
        self.conn.commit()
    


class StudendDb :
    def __init__(self) -> None:
        self.connection()
        
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                first TEXT ,
                last TEXT ,
                mail TEXT UNIQUE,
                classe TEXT
            )
                         """)
        self.close()

    def connection(self) :
        self.conn = sqlite3.connect("database/studentInfos/student.db")
        self.cur = self.conn.cursor() 
        
    def close(self) :
        self.cur.close()
        self.conn.commit() 
    
    def getIds(self) : 
        self.connection()
        ids = self.cur.execute("SELECT id FROM students").fetchall()
        self.close()
        return [i[0] for i in ids]
        
    
    def addStudents(self , first , last , classe ,mail) : 
        name = first + last + mail 
        id_ = "".join( random.sample( str(uuid.uuid4())+name, 10)  )
        id_ = str(id_)
        print(id_)
        
        self.connection()
        if self.cur.execute("SELECT * FROM students WHERE mail = ? OR id = ?", (mail,id_)).fetchall() : 
            self.close()
            return False 
        else :
            self.cur.execute("""INSERT INTO students (id , first , last , classe , mail) 
                             VALUES (?,?,?,?,?)""",(id_,first , last , classe ,mail) )
            
            self.close()
            return True
    
    def getStudents(self , classe=None) :
        students = []
        if classe == None: 
            print("None")
            try : 
                self.connection()
                students = self.cur.execute("SELECT * FROM students").fetchall()
                self.close()
                return students
            except Exception as e :
                print(e)
                return students
        else : 
            self.connection()
            try : 
                students = self.cur.execute("SELECT * FROM students WHERE classe = ?", (str(classe),) ).fetchall()
                self.close()
                return students
            except Exception as e :
                print(e)
                self.close()
                return students

    def getClasses(self) : 
        classes = []

        self.connection()
        try : 
            classes = self.cur.execute("SELECT classe FROM students").fetchall()
            self.close()
            return classes 
        except Exception as e : 
            print(e)
            self.close()
            return classes
    
    def getNames(self , student_id ) :
        self.connection()
        names = self.cur.execute("SELECT first, last , mail FROM students WHERE id=?", (student_id,)).fetchall()
        self.close()
        return names 


class GetGradesForm(FlaskForm) : 
    classe = StringField("Classe : ", 
                validators=[DataRequired(),Length(min=2)])
    submit = SubmitField("Ajouter") 
    