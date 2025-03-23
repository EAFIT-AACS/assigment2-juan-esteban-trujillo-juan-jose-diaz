from ALGORITHM_1_LFCO_2025_JET_JJD import createstringsGrammar, createStringsNoGrammar
from ALGORITHM_2_LFCO_2025_JET_JJD import PDA, transitions

def leftmost_derivation(string):
    """
    Generates the leftmost derivation of the string according to the grammar:
    S → aSb | ε
    """
    derivations = ["S"]
    current = "S"
    
    for char in string:
        if char == "a":
            current = current.replace("S", "aSb")  # Expands the first S found
        elif char == "b":
            current = current.replace("S", "")  # Replaces S with empty string
        derivations.append(current)
    
    return derivations

def compute_accepting_configurations(string):
    """
    Constructs the sequence of M configurations in an accepting computation with input x.
    """
    stack = ["$"]
    state = "q0"
    configurations = [("ε", state, list(stack))]  # Initial configuration (before reading)

    for char in string:
        state, stack = transitions(state, stack, char)
        configurations.append((char, state, list(stack)))  # Add transition

    return configurations

def main():
    # Generate strings using Algorithm 1
    strings_grammar = createstringsGrammar(4)

    # Get accepted strings without printing PDA results
    accepted, _ = PDA(strings_grammar)

    # Build and display accepting configurations and leftmost derivation
    print("\n--- Accepting Configurations of M and Leftmost Derivation ---\n")
    
    for string in accepted:
        configurations = compute_accepting_configurations(string)
        derivations = leftmost_derivation(string)
        
        print(f"\nFor the string: '{string}'\n")
        print(f"{'Leftmost Derivation':<35} || {' Input | State  | Stack'}")
        print("-" * 75)

        # Ensure both lists have the same length
        max_len = max(len(configurations), len(derivations))
        configurations += [("", "", [""])] * (max_len - len(configurations))
        derivations += [""] * (max_len - len(derivations))

        # Print aligned columns
        for i, (derivation, (char, state, stack)) in enumerate(zip(derivations, configurations)):
            stack_str = "".join(stack)
            print(f"{derivation:<35} || {char:7} | {state:5}  | {stack_str:<10}")

if __name__ == "__main__":
    main()
