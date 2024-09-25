import sys
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

# untuk menyimpan nama kota dan kostnya
class CityNode:
  def __init__(self, city, distance) -> None:
    self.city = str(city)
    self.distance = int(distance)

# untuk menjadikan isi file txt menjadi dict
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
            sld = int(delimeter[1].strip()) 
            h[node] = sld
    return h

def heuristic(node, values):
  return values.get(node, float('inf'))

# Breadth-First Search (BFS)

def bfs(graph, start, end):
    queue = [start]  
    visited = set()  
    parents = {start: None}  

    while queue:
        node = queue.pop(0)  

        if node == end:  
            
            final_path = []
            while node is not None:
                final_path.append(node)
                node = parents[node]
            final_path.reverse()  
            return final_path  
        
        if node not in visited:
            visited.add(node)  

            for neighbor in graph[node]:
                if neighbor.city not in visited and neighbor.city not in queue:
                    queue.append(neighbor.city)  
                    parents[neighbor.city] = node  
    return []

# Depth-First Search (DFS)

def dfs(graph, start, end):
    stack = []
    stack.append(start)
    path = []
    visited = set()  

    while stack:
        node = stack.pop()

        if node == end:
            return path + [node]

        if node not in visited:
            visited.add(node)  
            path.append(node)  

            
            for neighbor in reversed(graph.get(node, [])):
                if neighbor.city not in visited:  
                    stack.append(neighbor.city)
    return []  

# Uniform-Cost Search (UCS)

def ucs(graph, start, end):
    queue = PriorityQueue()
    queue.push(start, 0)
    
    path_cost = {start: 0}
    path = {}
    
    while not queue.isEmpty():
        node = queue.pop()
        
        if node == end:
            final_path = []
            while node is not None:
                final_path.append(node)
                node = path.get(node)
            final_path.reverse()
            return final_path
        
        for neighbor in graph.get(node, []):
            new_cost = path_cost[node] + neighbor.distance
            
            if neighbor.city not in path_cost or new_cost < path_cost[neighbor.city]:
                path_cost[neighbor.city] = new_cost
                queue.push(neighbor.city, new_cost)
                path[neighbor.city] = node
                
    return None

# Greedy Best Fisrt Search (GBFS)

def greedyBFS(start, end):
  path = {}
  q = PriorityQueue()
  h = makeHeuristicDict()
  
  q.push(start, 0)
  path[start] = None
  expandList = []
  
  while q.isEmpty() == False:
    curr = q.pop()
    expandList.append(curr)
    
    if curr == end:
      break
    
    for new in jalur[curr]:
      if new.city not in path:
        f_cost = heuristic(new.city, h)
        q.push(new.city, f_cost)
        path[new.city] = curr
        
  printOutput(start, end, path, expandList)
  
def printOutput(start, end, path, expandList):
  finalPath = []
  i = end
  
  while (path.get(i) != None):
    finalPath.append(i)
    i = path[i]

  finalPath.append(start)
  finalPath.reverse()
  
  print("Program Greedy Best First Search")
  print(start + " -> " + end)
  print("Kota yg dilewati dg jarak terpendek\t: " + str(finalPath))

# A* (A-Star)

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

# pilhan menu dan kode dijalankan diawah ini

def menu(): 
  print("===== Menu =====")
  print("1. Breadth-First Search (BFS)")
  print("2. Depth-First Search (DFS)")
  print("3. Uniform-Cost Search (UCS)")
  print("4. Greedy Best Fisrt Search (GBFS)")
  print("5. A* (A-Star)")
  print("0. Exit")
  
def pilihanKembali():
  pilihan = input("Apakah ingin kembali ke menu utama? (y/n): ")
  while True:
    if pilihan.lower() == "y":
      main()
    elif pilihan.lower() == "n":
      sys.exit()
    else:
      print("Masukkan pilihan yang sesuai")

def main():
  makeDict()
  while True:
    menu()
    
    kotaAsal = str(input("Masukkan Kota Asal: "))
    kotaTujuan = str(input("Masukkan Kota Tujuan: "))
    
    pilih = int(input("Pilih Meotde pencarian : "))
    
    if pilih == 1:
      path = bfs(jalur, kotaAsal, kotaTujuan)  
      if path:
        print("Hasil Algoritma Breadth-First Search: ")
        print(" -> ".join(path))  
      else:
        print("Path tidak ditemukan!")
      pilihanKembali()
    elif pilih == 2:
      path = dfs(jalur, kotaAsal, kotaTujuan)
      if path:
          print("Hasil Algoritma Depth-First Search: ")
          print(" -> ".join(path))        
      else:
          print("Path tidak ditemukan!")
      pilihanKembali()
    elif pilih == 3:
      path = ucs(jalur, kotaAsal, kotaTujuan)
      if path:
        print("Jalur terpendek : ", " -> ".join(path))
      else:
        print("Tidak ada jalur yang ditemukan.")
      pilihanKembali()
    elif pilih == 4:
      greedyBFS(kotaAsal, kotaTujuan)
      pilihanKembali()
    elif pilih == 5:
      aStarAlgo(kotaAsal, kotaTujuan)
      pilihanKembali()
    elif pilih == 0:
      print("Exit")
      break
    else:
      print("Pilihan Tidak Tersedia")

if __name__ == "__main__":
  main()
