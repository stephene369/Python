import speech_recognition as sr

# Créez un objet Recognizer
recognizer = sr.Recognizer()

# Chargez le fichier audio
audio_file = r"D:\Projects\Python\PythonProject\speech recognition\Dax\sub_60-70.wav"

with sr.AudioFile(audio_file) as source:
    # Enregistrez l'audio du fichier
    audio_data = recognizer.record(source)

    try:
        # Utilisez le moteur de reconnaissance vocale pour transcrire le texte
        recognized_text = recognizer.recognize_google(audio_data)  # Utilisez un autre moteur si nécessaire
        print("Texte reconnu : " + recognized_text)
    except sr.UnknownValueError:
        print("La reconnaissance vocale n'a pas pu comprendre l'audio")
    except sr.RequestError as e:
        print(f"Erreur lors de la demande : {e}")
