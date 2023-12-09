class BreadthFirstSearch:
    def __init__(self, data: dict):
        self.data = data
        self.queue = list()
        self.visited = list()
        self.paths = {node: [] for node in data}

    @staticmethod
    def create_queue(data):
        queue = [data.get(key) for key in data.keys() if len(data.get(key)) != 0]
        return queue

    def add_to_queue(self, value):
        self.queue.append(value)

    def remove_from_queue(self):
        return self.queue.pop(0)

    def run(self, start, destination):
        self.visited.append(start)
        self.queue.append(start)
        while self.queue:
            current_node = self.remove_from_queue()
            for neighbour in self.data[current_node]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)
                    self.paths[neighbour] = self.paths[current_node] + [current_node]

                    if neighbour == destination:
                        print(
                            f"Shortest Path to {destination}: {self.paths[neighbour] + [neighbour]}"
                        )
                        return


class DepthFirstSearch:
    def __init__(self, data: dict):
        self.data = data
        self.visisted = list()
        self.queue = list()

    def add_to_queue(self, value):
        self.queue.append(value)

    def remove_from_queue(self):
        value = self.queue.pop()
        self.visited.append(value)

    def run(self):
        pass


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E", "F"],
        "C": ["G"],
        "D": [],
        "E": [],
        "F": ["H"],
        "G": ["I"],
        "H": [],
        "I": [],
    }

    bfs = BreadthFirstSearch(graph)

    start_node = "A"
    destination_node = "G"

    bfs.run(start_node, destination_node)
