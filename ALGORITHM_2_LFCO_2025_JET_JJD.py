import ALGORITHM_1_LFCO_2025_JET_JJD as algo1

def PDA(strings):
    
    acceptedStrings = []
    rejectedStrings = []

    for string in strings:

        stack = ["$"]
        state = "q0"

        if string == "":
            state = "q1"

        for char in string:
            state,stack = transitions(state,stack,char)
            if state == "Rule Not Define":
                break

        if state == "q1" and len(stack) == 1 and stack[0] == "$":
            acceptedStrings.append(string)
            
        else:
            rejectedStrings.append(string)

    for string in acceptedStrings:
        print("The string "+string + " is accepted by the PDA")

    for string in rejectedStrings:
        print("The string "+string + " is rejected by the PDA")

    return acceptedStrings,rejectedStrings
 
def transitions(state,stack,char):

    if state == "q0":
        if char == "a" and (stack[-1] == "$" or stack[-1] == "A"):
            stack.append("A")
            state = "q0"
            return state,stack
        
        elif char == "b" and stack[-1] == "A":
            stack.pop()
            state = "q1"
            return state,stack

    elif state == "q1":
        
        if char == "b" and stack[-1] == "A":
            stack.pop()
            state = "q1"
            return state,stack
    
    return "Rule Not Define", stack

def test2():
    strings = algo1.createstringsGrammar(2)+algo1.createStringsNoGrammar(2)
    PDA(strings)



# Run the test function
test2()