# Import the required libraries
from tkinter import Tk , CENTER ,ttk
from pandas import read_csv

# Create an instance of tkinter frame
Imprimer= Tk()

df=read_csv('clients_db.csv')
total_rows = len(df)
total_columns = len(df.iloc[0])

# Set the size of the tkinter window
Imprimer.geometry("800x450")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
myliste = ttk.Treeview(Imprimer, column=("c1", "c2", "c3","c4"), show='headings', height=20)

myliste.column("# 1", anchor=CENTER)
myliste.heading("# 1", text="Id")
myliste.column("# 2", anchor=CENTER)
myliste.heading("# 2", text="Name")
myliste.column("# 3", anchor=CENTER)
myliste.heading("# 3", text="Hours")
myliste.column("# 4", anchor=CENTER)
myliste.heading("# 4", text="Date")

for i in range(total_rows):
        myliste.insert('', 'end', text="{i}", values=(f"{i}",df.iloc[i][0], df.iloc[i][1], df.iloc[i][2]))

myliste.pack()

import Entrer
Entrer

Imprimer.mainloop()

