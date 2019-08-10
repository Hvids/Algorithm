def persoin_is_seller(person):
    return person[-1] == "m"


def width_serch(graph, name):
    serch_queue = deque()
    serch_queue += graph[name]
    serched = []
    while serch_queue:
        person = serch_queue.popleft()
        if not person in serched:
            if persoin_is_seller(person):
                print(person + " is mango seller!")
            else:
                serch_queue += graph[person]
                serched.append(person)


if __name__ == "__main__":
    # поиск в ширину
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    width_serch(graph, "you")
