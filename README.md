# Pushdown Automaton (PDA) Simulator

This repository contains a simulation of a Pushdown Automaton (PDA) for two different languages. The program models the PDA's behavior for recognizing strings based on specified transition rules and simulates its acceptance process. It also generates a visual representation of the PDA's state transitions using a directed graph.

Features
1. PDA Simulation: Simulates the behavior of a PDA with stack operations based on transition rules.
2. Two Languages: The simulator supports two languages:
    - a**n b^n: Strings consisting of 'a's followed by an equal number of 'b's.
    - - a^n b^m c^n: Strings consisting of 'a's followed by any number of 'b's and 'c's, where the number of 'a's is equal to the number of 'c's.
3. Graphical Representation: Generates a graphical diagram of the PDA, showing the state transitions and stack operations.

Usage
1. Choose a Language: Select one of the two supported languages:
    - a^n b^n
    - a^n b^m c^n

2. Simulate a String: Input a string that you want the PDA to process. The PDA will simulate the string processing step by step and determine if the string is accepted or rejected by the automaton.

3. View Transition Diagram: The program will generate and display a graphical diagram representing the PDA's state transitions.

How to Run
1. Clone the repository or download the Python files.
2. Install the required dependencies:
    -pip install networkx matplotlib
   
4. Run the main Python script:
    - python pda_simulator.py
      
5.Follow the prompts in the terminal to choose the language and enter the input string.

Example
Language 1: a^n b^n
Input: aabbb
Output:
Starting simulation for input: 'aabbb'
Current state: q0, Current stack: ['Z']
Current state: q0, Current stack: ['A', 'Z']
Current state: q0, Current stack: ['A', 'A', 'Z']
Current state: q1, Current stack: ['A', 'Z']
Current state: q1, Current stack: ['Z']
Final state: q2, Final stack: ['Z']
Input: aabbb, Accepted: True
Language 2: a^n b^m c^n
Input: aabbbcc
Output:

Starting simulation for input: 'aabbbcc'
Current state: q0, Current stack: ['Z']
Current state: q0, Current stack: ['A', 'Z']
Current state: q0, Current stack: ['A', 'A', 'Z']
Current state: q1, Current stack: ['A', 'Z']
Current state: q1, Current stack: ['A', 'A', 'Z']
Final state: q3, Final stack: ['Z']
Input: aabbbcc, Accepted: True

Feel free to open issues or create pull requests to improve the PDA simulator. Contributions are welcome!
