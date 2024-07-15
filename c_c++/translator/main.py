from mtranslate import translate as trs

texte_a_traduire = "ce script python permet la tranduction hors ligne apres installation des packages approprier"
langue_source = "fr"
langue_cible = "en"

texte_traduit = trs(texte_a_traduire, langue_cible, langue_source)

print(texte_traduit)