from cryptography.fernet import Fernet

key = Fernet.generate_key() ; key 

# Créer un objet Fernet avec la clé
fernet = Fernet(key) 

# Texte à chiffrer
text = "Ceci est un texte secret"

# Chiffrer le texte
encrypted_text = fernet.encrypt(text.encode())

# Afficher le texte chiffré
print(encrypted_text)

# Déchiffrer le texte
decrypted_text = fernet.decrypt(encrypted_text).decode()

# Afficher le texte déchiffré
print(decrypted_text)

vc = 'jy8c-n9y=pf##!2^jae-l_5iafq6q%wfq8gdb6c0r5d52su+9y'