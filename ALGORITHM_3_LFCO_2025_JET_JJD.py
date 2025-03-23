from ALGORITHM_1_LFCO_2025_JET_JJD import createstringsGrammar, createStringsNoGrammar
from ALGORITHM_2_LFCO_2025_JET_JJD import PDA, transitions

def leftmost_derivation(string):
    """
    Genera la derivación más a la izquierda de la cadena según la gramática:
    S → aSb | ε
    """
    derivations = ["S"]
    current = "S"
    
    for char in string:
        if char == "a":
            current = current.replace("S", "aSb")  # Expande el primer S encontrado
        elif char == "b":
            current = current.replace("S", "")  # Reemplaza S por vacío
        derivations.append(current)
    
    return derivations

def compute_accepting_configurations(string):
    """
    Construye la secuencia de configuraciones de M en un cómputo de aceptación con entrada x.
    """
    stack = ["$"]
    state = "q0"
    configurations = [("ε", state, list(stack))]  # Configuración inicial (antes de leer)

    for char in string:
        state, stack = transitions(state, stack, char)
        configurations.append((char, state, list(stack)))  # Agregar transición

    return configurations

def main():
    # Generar cadenas con el algoritmo 1
    strings_grammar = createstringsGrammar(4)

    # Obtener cadenas aceptadas sin imprimir resultados del PDA
    accepted, _ = PDA(strings_grammar)

    # Construir y mostrar las configuraciones de aceptación y derivación más a la izquierda
    print("\n--- Configuraciones de aceptación de M y derivación más a la izquierda ---\n")
    
    for string in accepted:
        configurations = compute_accepting_configurations(string)
        derivations = leftmost_derivation(string)
        
        print(f"\nPara la cadena: '{string}'\n")
        print(f"{'Derivación más a la izquierda':<35} || {' Entrada | Estado  | Pila'}")
        print("-" * 75)

        # Asegurar que ambas listas tengan la misma longitud
        max_len = max(len(configurations), len(derivations))
        configurations += [("", "", [""])] * (max_len - len(configurations))
        derivations += [""] * (max_len - len(derivations))

        # Imprimir en columnas alineadas
        for i, (derivation, (char, state, stack)) in enumerate(zip(derivations, configurations)):
            pila_str = "".join(stack)
            print(f"{derivation:<35} || {char:7} | {state:5}  | {pila_str:<10}")



if __name__ == "__main__":
    main()