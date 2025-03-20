# Description: This file contains the algorithm 1 for the LFCO 2025 project.

# Importing libraries
import random

# Function to create strings that the grammar accepts, the strings are generated randomly
# The function receives the number of strings to generate
def createstringsGrammarGrammar(NumStringsGenerated):

    # Define the alphabet
    alphabet = ['a', 'b']

    # List to store the strings
    stringsGrammar = []

    # Loop to generate the strings
    while len(stringsGrammar)<NumStringsGenerated:

        n = random.randint(-1, 7)

        # If n is -1, the grammar accepts the empty string
        if n==-1:
            string = ""
            # Verify if the string is not in the list to avoid duplicates
            if string not in stringsGrammar:
                stringsGrammar.append(string)

        # Form the string with the number of repetitions of the letters
        else:
            string = ""
            for letter in alphabet:
                string += letter*n
            
            # Verify if the string is not in the list to avoid duplicates
            if string not in stringsGrammar:
                    stringsGrammar.append(string)

    # Return the list of strings tha the grammar accepts
    return stringsGrammar

# Function to create strings that the grammar does not accept, the strings are generated randomly
# The function receives the number of strings to generate
def createStringNoGrammar(NumStringsGenerated):

    # Define the alphabet
    alphabet = ['a', 'b']

    # List to store the strings
    stringsNoGrammar = []

    # Loop to generate the strings
    while len(stringsNoGrammar)<NumStringsGenerated:

        # Are three types of errors that the grammar does not accept, and the error is chosen randomly
        NoGrammar = ["Unbalanced", "WrongOrder", "LetterInterchange"]
        typeError= random.choice(NoGrammar)

        # Unbalanced strings
        if typeError == "Unbalanced":
            Na = random.randint(0, 7)
            Nb = random.randint(0, 7)

            # Verify if the number of repetitions of the letters are different
            while Na == Nb:
                Nb = random.randint(0, 7)

            # Generate the string
            string = alphabet[0]*Na + alphabet[1]*Nb

            # Verify if the string is not in the list to avoid duplicates
            if string not in stringsNoGrammar:
                stringsNoGrammar.append(string)
        
        # Wrong Order
        elif typeError == "WrongOrder":
            Na = random.randint(0, 7)
            Nb = random.randint(0, 7)

            # Generate the string
            string = alphabet[1]*Nb + alphabet[0]*Na

            # Verify if the string is not in the list to avoid duplicates
            if string not in stringsNoGrammar:
                stringsNoGrammar.append(string)
        
        # Letter Interchange
        elif typeError == "LetterInterchange":
            string = ""

            # Generate the string randomly
            for i in range(0, 5):

                # Generate the number of repetitions of the letters
                NumRepLetter= random.randint(1, 3)
                # Select the letter
                NumRandAlphabet = random.randint(0, 1)

                # Generate the string
                string += alphabet[NumRandAlphabet]*NumRepLetter
            
            # Verify if the string is not in the list to avoid duplicates
            if string and string not in stringsNoGrammar:
                stringsNoGrammar.append(string)     
    
    # Return the list of strings that the grammar does not accept
    return stringsNoGrammar