graph = {
    'Siantar': ['Tebing', 'Perdagangan', 'Parapat', 'Raya'],
    'Tebing': ['Medan', 'Binjai'],
    'Perdagangan': ['Asahan', 'Sipirok'],
    'Parapat': ['Balige'],
    'Raya': [],
    'Medan': [],
    'Binjai': [],
    'Asahan': ['Kisaran'],
    'Sipirok': ['Tanjung'],
    'Balige': [],
    'Kisaran': [],
    'Tanjung': []
}

def dls(start, goal, path, level, maxD):
  print("Level Sekarang --> ", level)
  print("Node yang sedang dicek ", start)
  
  path.append(start)
  
  if start == goal:
    print("Simpul Tujuan")
    return path
  
  print("Bukan simpul tujuan")
  
  if level == maxD:
    return False
  
  print("\nLanjutan dari simpul ", start)
  
  for child in graph[start]:
    
    if dls(child, goal, path, level + 1, maxD):
      return path
  return False

start = input('Kota Awal : ')
goal = input('Kota Tujuan : ')
maxD = int(input("Maximum depth limit : "))
print()

path = []
res = dls(start, goal, path, 0, maxD)

if (res):
  print("Jalur ke kota tujuan telah ditemukan")
  print("Path", path)
else:
  print("Jalur ke kota tujuan tidak ditemukan dalam depth limit tsb.")