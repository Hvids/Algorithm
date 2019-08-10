def find_lowes_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def decst(graph, costs, parents):
    processed = []
    node = find_lowes_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbohors = graph[node]
        for n in neighbohors.keys():
            new_cost = cost + neighbohors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowes_cost_node(costs, processed)
    return costs

# алгоритм дейкстры

    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    infinity = float("inf")
    costs = {
        "a": 6,
        "b": 2,
        "fin": infinity
    }
    paretns = {
        "a": "start",
        "b": "start",
        "fin": None
    }
    print(decst(graph, costs, paretns))


if __name__ == "__main__":
    # алгоритм дейкстры

    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    infinity = float("inf")
    costs = {
        "a": 6,
        "b": 2,
        "fin": infinity
    }
    paretns = {
        "a": "start",
        "b": "start",
        "fin": None
    }
    print(decst(graph, costs, paretns))
