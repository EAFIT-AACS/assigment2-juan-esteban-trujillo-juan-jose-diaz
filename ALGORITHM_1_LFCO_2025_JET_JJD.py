import random
def createstringsGrammarGrammar(NumStringsGenerated):
    alphabet = ['a', 'b']
    stringsGrammar = []
    while len(stringsGrammar)<NumStringsGenerated:
        n = random.randint(-1, 7)
        if n==-1:
            string = ""
            if string not in stringsGrammar:
                stringsGrammar.append(string)
        else:
            string = ""
            for letter in alphabet:
                string += letter*n
            
            if string not in stringsGrammar:
                    stringsGrammar.append(string)
        
    
    print(stringsGrammar)
    return stringsGrammar

def createStringNoGrammar(NumStringsGenerated):
    alphabet = ['a', 'b']
    stringsNoGrammar = []

    while len(stringsNoGrammar)<NumStringsGenerated:

        NoGrammar = ["Unbalanced", "WrongOrder", "LetterInterchange"]
        typeError= random.choice(NoGrammar)

        # Unbalanced strings
        if typeError == "Unbalanced":
            Na = random.randint(0, 7)
            Nb = random.randint(0, 7)

            while Na == Nb:
                Nb = random.randint(0, 7)
    
            string = alphabet[0]*Na + alphabet[1]*Nb

            if string not in stringsNoGrammar:
                stringsNoGrammar.append(string)
        
        # Wrong Order
        elif typeError == "WrongOrder":
            Na = random.randint(0, 7)
            Nb = random.randint(0, 7)

            string = alphabet[1]*Nb + alphabet[0]*Na

            if string not in stringsNoGrammar:
                stringsNoGrammar.append(string)
        
        elif typeError == "LetterInterchange":
            string = ""

            for i in range(0, 5):
                NumRepLetter= random.randint(1, 3)

                NumRandAlphabet = random.randint(0, 1)

                string += alphabet[NumRandAlphabet]*NumRepLetter
            
            if string and string not in stringsNoGrammar:
                stringsNoGrammar.append(string)     
    
    print(stringsNoGrammar)
    return stringsNoGrammar


createstringsGrammarGrammar(2)
createStringNoGrammar(2)