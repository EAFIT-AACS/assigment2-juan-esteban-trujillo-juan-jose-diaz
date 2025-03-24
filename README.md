# Assignment 2 - Pushdown Automata and Grammar Derivation

## Project Overview
This project focuses on **Pushdown Automata (PDA) and Context-Free Grammar (CFG) derivations**. The goal is to generate strings based on a given grammar, validate them using a **PDA**, and construct their **leftmost derivations and accepting configurations**.

## Team Members
- Juan Esteban Trujillo
- Juan José Díaz

Each team member contributed to the design, development, and testing of the algorithms.

## System and Tools Used

To ensure compatibility and efficiency, the following tools and environments were used:

- **Operating System**: Windows 11
- **Programming Language**: Python
- **Tools**: Git

## Execution Instructions
To run the implementation, you must execute all the files available in the GitHub repository. The project consists of three main algorithms:

1. **Algorithm 1**: Generates valid strings based on a given grammar.
2. **Algorithm 2**: Implements a Pushdown Automaton (PDA) to validate and process the generated strings.
3. **Algorithm 3**: Computes the accepting configurations and leftmost derivations for the strings.

### Steps to Run the Code
1. Clone the repository:
   ```sh
   git clone https://github.com/EAFIT-AACS/assigment2-juan-esteban-trujillo-juan-jose-diaz.git
   cd assigment2-juan-esteban-trujillo-juan-jose-diaz
   ```
2. Ensure you have Python installed (preferably version 3.x). You can check by running:
   ```sh
   python --version
   ```
   If Python is not installed, download and install it from [Python's official website](https://www.python.org/downloads/).

3. Since Algorithm 3 already integrates Algorithm 1 and Algorithm 2, you only need to run:
   ```sh
   python ALGORITHM_3_LFCO_2025_JET_JJD.py
   ```

   This will automatically:

   - Generate the strings (Algorithm 1).

   - Process them using the Pushdown Automaton (PDA) (Algorithm 2).

   - Compute the derivations and final configurations (Algorithm 3).

Each script must be executed in order to generate and validate the grammar-based strings successfully.

If you encounter any issues, verify that all necessary files are in the same directory and that you are running the scripts in the correct sequence.

