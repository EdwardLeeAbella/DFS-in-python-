adj_list = {
  "A":["B", "C"],
  "B":["D", "E"],
  "C":["B", "F"],
  "D":[],
  "E":["F"],
  "F":[]
}
#print(adj_list)

color = {} # white, green, black 
parent = {}
trav_time = {} # start = green , end = black
dfs_traversal_output = []

#initialize
for node in adj_list.keys():
  color[node] = "white"
  parent[node] = None
  trav_time[node] = [-1, -1]
print(color)
print(parent)
print(trav_time)

time = 0
def util_dfs(u):
  global time
  color[u] = "green"
  trav_time[u][0] = time
  dfs_traversal_output.append(u)
  time += 1

  for v in adj_list[u]:
    if color[v] == "white":
      parent[v] = u
      util_dfs(v)
  color[u] = "black"
  trav_time[u][1] = time
  time += 1

util_dfs("A")
print(dfs_traversal_output)
print(parent)
print(trav_time)















