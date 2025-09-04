import networkx as nx


def create_graph() -> nx.DiGraph:
    graph = nx.DiGraph()

    # Node "one"
    input_one = ["one_1", "one_2"]
    output_one = ["out_1"]
    node_type_one = "agent"

    graph.add_node(
        "one",
        type=node_type_one,  # programmatic use
        input=input_one,  # programmatic use
        output=output_one,  # programmatic use
        label=f"one\nType: {node_type_one}\nInput: {input_one}\nOutput: {output_one}"  # visualization
    )

    # Node "two"
    input_two = ["out_1"]
    output_two = ["final_result"]
    node_type_two = "tool"

    graph.add_node(
        "two",
        type=node_type_two,
        input=input_two,
        output=output_two,
        label=f"two\nType: {node_type_two}\nInput: {input_two}\nOutput: {output_two}"
    )

    # Connect nodes
    graph.add_edge("one", "two")

    return graph


if __name__ == "__main__":
    nx.drawing.nx_pydot.write_dot(create_graph(),"../", "workflow.dot")
    print("DOT file created: workflow.dot")
