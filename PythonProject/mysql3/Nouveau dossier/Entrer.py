from tkinter import Tk , Entry

Entrer=Tk()
Entrer.geometry("300x200")
nom=Entry(Entrer,font="Helvetica 11 bold", width=8, bg='lavender')
nom.pack(padx=5, pady=5, side=['bottom'],fill='both')
nom.focus_set()

nbproduits=Entry(Entrer,font="Helvetica 11 bold", width=8, bg='lavender')
nbproduits.pack(padx=5, pady=5, side=['bottom'],fill='both')
nbproduits.focus_set()

Entrer.mainloop()
