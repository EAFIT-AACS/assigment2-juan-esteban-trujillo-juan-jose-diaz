# Import the algorithm 1
from ALGORITHM_1_LFCO_2025_JET_JJD import test

# Function to simulate the PDA
# The function receives a list of strings
# The function returns the list of accepted and rejected strings
def PDA(strings):
    
    # Lists to store the accepted and rejected strings
    acceptedStrings = []
    rejectedStrings = []

    # Loop to verify each string    
    for string in strings:

        # Initial state and stack
        stack = ["$"]
        state = "q0"

        # If the string is empty, the initial state is q1 and the empty string is accepted
        if string == "":
            state = "q1"

        # Loop to verify each character of the string
        for char in string:
            state,stack = transitions(state,stack,char)
            if state == "Rule Not Define":
                break
        
        # If the state is q1 and the stack has only the initial symbol, the string is accepted
        if state == "q1" and len(stack) == 1 and stack[0] == "$":
            acceptedStrings.append(string)

        # If the state is different from q1 or the stack is different from the initial symbol, the string is rejected  
        else:
            rejectedStrings.append(string)

    # Return the list of accepted and rejected strings
    return acceptedStrings,rejectedStrings
 
# Function to simulate the transitions of the PDA
# The function receives the current state, the stack and the character
# The function returns the next state and the stack
def transitions(state,stack,char):

    # Transitions of the PDA
    if state == "q0":
        
        # If the character is "a" and the top of the stack is "$" or "A", the stack receives "A" and the state is q0
        if char == "a" and (stack[-1] == "$" or stack[-1] == "a"):
            stack.append("a")
            state = "q0"
            return state,stack
        
        # If the character is "b" and the top of the stack is "A", the stack pops the top and the state is q1
        elif char == "b" and stack[-1] == "a":
            stack.pop()
            state = "q1"
            return state,stack

    # If the state is q1
    elif state == "q1":
        
        # If the character is "b" and the top of the stack is "A", the stack pops the top and the state is q1
        if char == "b" and stack[-1] == "a":
            stack.pop()
            state = "q1"
            return state,stack
    
    # If the transitions are not defined, the state is "Rule Not Define"
    return "Rule Not Define", stack

# Function to test the PDA
def test2():

    # Generate strings using Algorithm 1
    stringsOutput1 = test()

    # Simulate the PDA
    accepted, notAccepted = PDA(stringsOutput1)

    # Print the output of the PDA beutifully
    print("\n" + "="*55)
    print("🤖✅ Output of Algorithm 2: PDA Processing ✅🤖".center(50))
    print("="*55 )

    # Print accepted strings
    for string in accepted:
        print(f"🔹 The string '{string}' is accepted by the PDA ✅")

    # Print rejected strings
    for string in notAccepted:
        print(f"🔹 The string '{string}' is rejected by the PDA ❌")

    # Return the list of accepted and rejected strings
    return accepted, notAccepted