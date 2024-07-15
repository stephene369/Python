from json import load , dump


with open("dictionnaire.json" , "r") as j : 
    dictionnaire = load(j)

dictionary = { i['word'].replace(" ",''):i["definition"] for i in dictionnaire }


def translator_bariba_french(text) : 
    text_split = text.split(" ")
    translated = ''
    for text_split_ in text_split : 
        try : 
            translated = translated + " " + dictionary[text_split_]
        except Exception as e :
            print(e)
    return translated

translator_bariba_french('adaamisi')
