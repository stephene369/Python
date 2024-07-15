from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired , Length
import sqlite3
import random 
import uuid


class AdminForm(FlaskForm):
    label = 'Se connecte (Admin)'
    
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), 
                        Length(min=8)])
    
    password = PasswordField('Mot de passe', validators=[DataRequired(),
                        Length(min=8)])
    
    submit = SubmitField('Se connecter')




class StudentForm(FlaskForm):
    label = 'Se connecter (Étudiant)'
    
    student_id = StringField('Identifiant unique', validators=[DataRequired()])
    
    submit = SubmitField('Se connecter')
    


class AdminDb :
    def __init__(self ):
        self.connection()
        
        self.cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS admin (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
            """)
        if self.cur.execute("SELECT COUNT(*) FROM admin").fetchone()[0] == 0 : 
            self.conn.execute("insert into admin (username, password) VALUES('stephenew36' , 'stephenew36')")
            
            self.close()
    
    def connection(self) : 
        self.conn = sqlite3.connect("database/usersInfos/admin.db")
        self.cur = self.conn.cursor()
        
    def close(self) :
        self.cur.close()
        self.conn.commit()
        
    def authenticate(self, username, password):
        self.connection()
        admin = self.cur.execute("SELECT * FROM admin WHERE username =? AND password =?", (username, password)).fetchone()
        return admin is not None

class StudentDb :
    def __init__(self ):
        self.connection()
        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS identifiant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                student_id TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        """)
    
    def connection(self) :
        self.conn = sqlite3.connect("database/studentInfos/student.db")
        self.cur = self.conn.cursor()
    
    def close(self) :
        self.cur.close()
        self.conn.commit()
    
    def authenticate(self, unique_id ) :
        self.connection()
        student = self.cur.execute("SELECT * FROM student WHERE student_id =? ", (unique_id)).fetchone()
        return student is not None
    
    def add_student(self, first_name, last_name ) : 
        name = first_name+last_name
        student_id = "".join( random.sample( str(uuid.uuid4())+name, 10)  ) 
        
        self.conn.execute("""INSERT INTO identifiant (first_name, last_name, student_id) 
                          VALUES (?, ?, ?) """, (first_name, last_name, student_id))
        
        