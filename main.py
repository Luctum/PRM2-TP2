import tika
from tika import parser

parsed = ""
parsed += " " + parser.from_file('Buffer-in/01089-stage predicsis storm.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01106-Développeur Base de données (HF).pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01128-Ingenieur informatique-Telemedecine.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01135-ISTIC_310550_ficheStage2013-2014_Cartographie_reseaux_telemedecine.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01170-Dev web plateforme clients.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01180-SFF - Stage Informatique.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01199-Stage _ Outils java et C_C__.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01212-Offre de stage développeur Eliga.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01229-Annonce Stagiaire MASTER 2 MIAGE.pdf')['content']
parsed += " " + parser.from_file('Buffer-in/01250-Integrateur_Developpeur web-Visibility.pdf')['content']

split=parsed.split ()

words = {}
ignore = ["de", ":", ",", ";", ".", "et", "est", "à", "a", "des", "les", "du", "la", "le", " ", "un", "au", "aux", "une", "vous", "ils", "par", "avec", "une", "□", "ou", "où", "date", "ce", "ca", "cela", "ça", "fin", "debut", "fax", "nos", "temps", "mission", "recrute", "qui", "que", "ces", "stagiaire", "afin", "que"]

for word in split:
    word_low = word.lower()
    if word_low not in words:
        words[word_low] = 0


file = open("words.csv","w", encoding="utf-8") 


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


for w in sorted(words, key=words.get, reverse=True):
    if w not in ignore and is_number(w) == False:
        file.write(w + '\n');
    
  


