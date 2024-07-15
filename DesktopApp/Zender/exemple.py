import tkinter as tk

def afficher_question(question, reponse, explication):
    root = tk.Tk()
    root.title("Questionnaire")

    question_label = tk.Label(root, text=question, font=('Helvetica', 14, 'bold'))
    question_label.pack(pady=10)

    reponse_label = tk.Label(root, text="Votre réponse : " + reponse, font=('Helvetica', 12))
    reponse_label.pack(pady=10)

    explication_label = tk.Label(root, text="Explication : " + explication, font=('Helvetica', 10, 'italic'))
    explication_label.pack(pady=10)

    root.mainloop()

# Exemple d'utilisation
question = "1. Question\nA company has deployed Amazon RedShift for performing analytics on user data..."
reponse = "1,3"
explication = "RedShift always keeps three copies of your data and provides continuous/incremental backups..."

afficher_question(question, reponse, explication)
