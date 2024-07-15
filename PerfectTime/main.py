import sqlite3 
from datetime import datetime 

DB = "journal.db"

conn = sqlite3.connect(DB)
curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS journals
            (days VARCHAR(16) PRIMARY KEY, 
            whatisup TEXT)
""")

curs.execute("SELECT * FROM journals").fetchall()


def add_content() :
    day = datetime.today().day
    month = datetime.today().month 
    year = datetime.today().year 
    hour = datetime.today().hour

    date = f"{day}-{month}-{year}-{hour}"
    print(date)
    
    journal= input("So what's up ? .. ")
    try : 
        curs.execute("""INSERT INTO journals VALUES (?,?) """ , (date , journal ) )
    except sqlite3.IntegrityError :  
        print("Already   done for today")
    conn.commit()
    curs.close()
    conn.close()

if input("oui ou non ?  ") == "oui" :
    add_content()

rest = datetime.today() - datetime(2031 , 6 , 13 , 21 , 31 )
print("Time left : ..  " , rest )
