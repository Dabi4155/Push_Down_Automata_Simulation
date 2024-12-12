import networkx as nx
import matplotlib.pyplot as plt

# Transition definitions for different languages
def get_transitions(choice):
    if choice == "1":
        return {
            "transitions": [
                ("q0", "a", "Z", "q0", "AZ"),
                ("q0", "a", "A", "q0", "AA"),
                ("q0", "b", "A", "q1", ""),
                ("q1", "b", "A", "q1", ""),
                ("q1", "", "Z", "q2", "Z"),
            ],
            "final_state": "q2",
        }
    elif choice == "2":
        return {
            "transitions": [
                ("q0", "a", "Z", "q0", "AZ"),
                ("q0", "a", "A", "q0", "AA"),
                ("q0", "b", "A", "q1", "A"),
                ("q1", "b", "A", "q1", "A"),
                ("q1", "c", "A", "q1", ""),
                ("q1", "", "Z", "q3", "Z"),
            ],
            "final_state": "q3",
        }
    return {"transitions": [], "final_state": ""}

# PDA simulation function
def simulate_pda(input_string, transitions, final_state):
    stack = ["Z"]
    current_state = "q0"
    print(f"Starting simulation for input: '{input_string}'")
    print(f"Current state: {current_state}, Current stack: {stack}")

    for symbol in input_string:
        applied_transition = False
        for (start, inp, stack_top, end, push) in transitions:
            if current_state == start and symbol == inp and stack[-1] == stack_top:
                current_state = end
                stack.pop()
                stack.extend(reversed(push))
                applied_transition = True
                print(f"Current state: {current_state}, Current stack: {stack}")
                break
        if not applied_transition:
            print("No valid transition. Rejecting input.")
            return False

    # Check for empty input transitions
    while True:
        applied_transition = False
        for (start, inp, stack_top, end, push) in transitions:
            if current_state == start and inp == "" and stack[-1] == stack_top:
                current_state = end
                stack.pop()
                stack.extend(reversed(push))
                applied_transition = True
                print(f"Current state: {current_state}, Current stack: {stack}")
                break
        if not applied_transition:
            break

    print(f"Final state: {current_state}, Final stack: {stack}")
    return current_state == final_state and stack == ["Z"]

# Function to generate PDA diagram
def generate_pda_diagram(transitions, final_state):
    G = nx.DiGraph()

    # Add edges with labels for transitions
    edge_labels = {}
    for (start, inp, stack_top, end, push) in transitions:
        label = f"({inp}, {stack_top} → {push})"
        G.add_edge(start, end)
        if (start, end) not in edge_labels:
            edge_labels[(start, end)] = []
        edge_labels[(start, end)].append(label)

    # Combine multiple labels for the same edge
    for key in edge_labels:
        edge_labels[key] = "\n".join(edge_labels[key])

    # Draw the graph with positions
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue")
    nx.draw_networkx_nodes(G, pos, nodelist=["q0"], node_color="green", label="Start")
    nx.draw_networkx_nodes(G, pos, nodelist=[final_state], node_color="orange", label="Final")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Title and show plot
    plt.title("Pushdown Automaton Transition Diagram")
    plt.show()

# Main function1
if __name__ == "__main__":
    print("Choose which of these 2 languages you want to use:")
    print("1. a^n b^n")
    print("2. a^n b^m c^n")
    choice = input("Enter your choice (1/2): ").strip()
    data = get_transitions(choice)

    if not data["transitions"]:
        print("Invalid choice.")
    else:
        input_string = input("Enter the input string to simulate: ").strip()
        generate_pda_diagram(data["transitions"], data["final_state"])
        accepted = simulate_pda(input_string, data["transitions"], data["final_state"])
        print(f"Input: {input_string}, Accepted: {accepted}")