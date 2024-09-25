import heapq

jalur = {}

class PriorityQueue:
    def __init__(self) -> None:
        self.cities = []
    
    def isEmpty(self):
        return len(self.cities) == 0
    
    def check(self):
        print(self.cities)

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
        
    def pop(self):
        return heapq.heappop(self.cities)[1]

class CityNode:
    def __init__(self, city, distance) -> None:
        self.city = str(city)
        self.distance = int(distance)

def makeDict():
    filejalan = "E:\\OneDrive\\Desktop\\python\\Sistem Cerdas\\minggu 4\\jatimjalan.txt"
    with open(filejalan, "r") as file:
        for line in file:
            delimeter = line.split(', ')
            city1 = delimeter[0].strip()
            city2 = delimeter[1].strip()
            dist = int(delimeter[2].strip())
            jalur.setdefault(city1, []).append(CityNode(city2, dist))
            jalur.setdefault(city2, []).append(CityNode(city1, dist))

def makeHeuristicDict():
    h = {}
    fileheuristicjalan = "E:\\OneDrive\\Desktop\\python\\Sistem Cerdas\\minggu 4\\jatimheuristic.txt"
    with open(fileheuristicjalan, "r") as file:
        for line in file:
            delimeter = line.strip().split(', ')
            node = delimeter[0].strip()
            sld = int(delimeter[1].strip())  # Straight Line Distance (Heuristic)
            h[node] = sld
    return h

def heuristic(node, values):
    return values.get(node, float('inf'))  # Return infinity if the node is not found

def get_neighbors(v):
    if v in jalur:
        return [(neighbor.city, neighbor.distance) for neighbor in jalur[v]]
    return []

def aStarAlgo(start_node, stop_node):
    open_set = PriorityQueue()
    open_set.push(start_node, 0)
    closed_set = set()
    
    h = makeHeuristicDict()  # Heuristic values
    g = {start_node: 0}  # Cost from start to each node
    parents = {start_node: None}

    while not open_set.isEmpty():
        n = open_set.pop()

        if n == stop_node:
            path = []
            while n is not None:
                path.append(n)
                n = parents[n]
            path.reverse()
            print(f'Path found: {path}')
            return path
        
        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m in closed_set:
                continue

            tentative_g = g[n] + weight
            if m not in g or tentative_g < g[m]:
                g[m] = tentative_g
                f = tentative_g + heuristic(m, h)
                open_set.push(m, f)
                parents[m] = n

    print('Path does not exist!')
    return None

def main():
    makeDict()
    aStarAlgo('Surabaya', 'Madiun')

if __name__ == "__main__":
    main()
