import fitz  

def fusionner_pdf(chemin_fichier1, chemin_fichier2, chemin_fichier_sortie):
    pdf_merger = fitz.open()
    
    # Ouvrir les fichiers PDF
    pdf1 = fitz.open(chemin_fichier1)
    pdf2 = fitz.open(chemin_fichier2)
    
    pdf_merger.insert_pdf(pdf1)
    pdf_merger.insert_pdf(pdf2)
    
    pdf_merger.save(chemin_fichier_sortie)
    pdf_merger.close()
    pdf1.close()
    pdf2.close()

fichier1 = 'garde2.pdf'
fichier2 = 'main.pdf'
fichier_sortie = 'MEMOIRE.pdf'

fusionner_pdf(fichier1, fichier2,fichier_sortie)

