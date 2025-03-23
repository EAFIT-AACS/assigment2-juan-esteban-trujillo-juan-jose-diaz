def PDA(strings):
    
    acceptedStrings = []
    rejectedStrings = []

    for string in strings:

        stack = ["$"]
        state = "q0"

        for char in string:
            state,stack = transitions(state,stack,char)

        if state == "q2" and len(stack) == 1 and stack[0] == "$":
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

        if char == "a" and stack[-1] == "$":
            stack.append("a")
            state = "q1"
            return state,stack

        else:
            state = "q3"
            return state,stack

    elif state == "q1":

        if char == "a" and stack[-1] == "a":
            stack.append("a")
            state = "q1"
            return state,stack

        elif char == "b" and stack[-1] == "a":
            stack.pop()
            state = "q2"
            return state,stack

        else:
            state = "q3"
            return state,stack

    elif state == "q2":

        if char == "b" and stack[-1] == "a":
            stack.pop()
            state = "q2"
            return state,stack

        else:
            state = "q3"
            return state,stack

    else:
        stata = "q3"
        return state,stack