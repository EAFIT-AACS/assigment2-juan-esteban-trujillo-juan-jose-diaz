# mport the functions from the other files
from ALGORITHM_1_LFCO_2025_JET_JJD import createstringsGrammar
from ALGORITHM_2_LFCO_2025_JET_JJD import PDA, transitions,test2

# Function to generate the leftmost derivation of the string
def leftmost_derivation(string):
    
    #Generates the leftmost derivation of the string according to the grammar: S → aSb | ε
    # Initialize the list of derivations with the start symbol
    derivations = ["S"]
    current = "S"
    
    # Iterate over each character in the string
    for char in string:
        
        if char == "a":
            # Expands the first S found
            current = current.replace("S", "aSb")

        elif char == "b":
            # Expands the first S found
            current = current.replace("S", "")
        
        # Add the current derivation to the list
        derivations.append(current)
    
    # Return the list of derivations
    return derivations

# Function to compute the accepting configurations of the PDA
def compute_accepting_configurations(string):
    
    #Constructs the sequence of M configurations in an accepting computation with input x.
    # Define the initial state and stack
    stack = ["$"]
    state = "q0"

    # Initial configuration (before reading)
    configurations = [("ε", state, string, stack)]

    # Iterate over each character in the string
    for i, char in enumerate(string):

        # Perform the transition
        state, stack = transitions(state, stack, char)

         # Remaining input string
        remaining_input = string[i + 1:]

        # Add the configuration to the list
        configurations.append((char, state, remaining_input, list(stack)))

    # Return the list of configurations
    return configurations

def main():
    # Generate strings using Algorithm 1
    stringsOutput2 = test2()

    # Extract only the list of strings (accepted + rejected) from test2()
    all_strings = stringsOutput2[0] + stringsOutput2[1]  # Combine both lists

    # Run the PDA to accept the strings
    accepted, _ = PDA(all_strings)

    # Display the output of Algorithm 3 beutifully
    print("\n" + "="*60)
    print("🌳🔄 Output of Algorithm 3: Derivation & PDA Config 🔄🌳".center(55))
    print("="*60 )

    # Build and display accepting configurations and leftmost derivation
    print("--- Accepting Configurations of M and Leftmost Derivation ---")
    
    # Iterate over each accepted string
    for string in accepted:

        # Compute the accepting configurations and leftmost derivation
        configurations = compute_accepting_configurations(string)
        derivations = leftmost_derivation(string)
        
        # Print the leftmost derivation and accepting configurations
        print(f"\nFor the string ➜ '{string}'")
        print(f"{'Leftmost Derivation':<36} || {' State |    Remaining   | Stack'}")
        print("-" * 100)

        # Ensure both lists have the same length
        max_len = max(len(configurations), len(derivations))
        configurations += [("", "", "", [""])] * (max_len - len(configurations))
        derivations += [""] * (max_len - len(derivations))

        # Print aligned columns
        for i, (derivation, (char, state, remaining, stack)) in enumerate(zip(derivations, configurations)):
            stack_str = "".join(stack)
            print(f"🔹 {derivation:<33} || {state:5}  | {remaining:14} | {stack_str:<10}")

# Run the main function that contains all of the 3 algorithms whith the output of each one
if __name__ == "__main__":
    main()