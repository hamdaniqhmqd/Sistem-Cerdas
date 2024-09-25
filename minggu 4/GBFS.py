'''
Program menghitung jarak terpendek antara dua kota
dari file yang berisi daftar kota menggunakan algoritma GBFS
'''

import heapq

jalur = {}

class PriorityQueue:
  def __init__(self) -> None:
    self.cities = []
  
  def isEmpty(self):
    if self.cities == []:
      return True
    return False
  
  def check(self):
    print(self.cities)

  def push(self, city, cost):
    heapq.heappush(self.cities, (cost, city))
    
  def pop(self):
    return heapq.heappop(self.cities)[1]

class CityNode:
  def __init__(self, city, distance) -> None:
    self.city = str(city)
    self.distance = str(distance)

def makeDict():
  filejalan = "E:\\OneDrive\\Desktop\\python\\Sistem Cerdas\\minggu 4\\jalan.txt"
  file = open(filejalan, "r")
  for str in file:
    delimeter = str.split(', ')
    city1 = delimeter[0]
    city2 = delimeter[1]
    dist = delimeter[2]
    jalur.setdefault(city1, []).append(CityNode(city2, dist))
    jalur.setdefault(city2, []).append(CityNode(city1, dist))
    
def makeHeuristicDict():
  h = {}
  fileheuristicjalan = "E:\\OneDrive\\Desktop\\python\\Sistem Cerdas\\minggu 4\\heuristicjalan.txt"
  file = open(fileheuristicjalan, "r")
  for str in file:
    delimeter = str.strip().split(', ')
    node = delimeter[0].strip()
    sld = int(delimeter[1].strip())
    h[node] = sld
  return h

def heuristic(node, values):
  return values[node]

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
  
def main():
  src = "Arad"
  dst = "Bucharest"
  
  makeDict()
  greedyBFS(src, dst)
  
if __name__ == "__main__":
  main()