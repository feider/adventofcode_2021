import numpy as np
ip = 'input_test.txt'
ip = 'input.txt'



l = []
with open(ip, 'r') as f:
    for k in f:
        l.append([int(i) for i in k.strip()])

l = np.asarray(l)

weights = np.zeros([l.shape[0]+2, l.shape[1]+2])+np.inf
weights[1:-1, 1:-1] = l
weights[1,1]=0

distances = np.zeros([l.shape[0]+2, l.shape[1]+2])+np.inf
previous = []
for i in range(weights.shape[0]):
    row = []
    for j in range(weights.shape[1]):
        row.append(None)
    previous.append(row)

distances[1,1]=0
nopen = set()
nclosed = set()

#initialize
nopen.add((1, 2))
previous[1][2] = (1, 1)
distances[1,2] = weights[1,2]+weights[1,1]

nopen.add((2, 1))
previous[2][1] = (1, 1)
distances[2,1] = weights[2,1]+weights[1,1]

nclosed.add((1,1))

print(weights)


while len(nopen) > 0:
    nodes = list(nopen)
    dist = []
    for node in nodes:
        dist.append(distances[node[0], node[1]])
    i_dist = np.argmin(dist)
    dist = dist[i_dist]
    node = nodes[i_dist]
    if node[0] == weights.shape[0]-2 and node[1] == weights.shape[1]-2: break
    nclosed.add(node)
    nopen.remove(node)

    cnodes = [
            (node[0], node[1]-1),
            (node[0], node[1]+1),
            (node[0]-1, node[1]),
            (node[0]+1, node[1])
            ]

    for nnode in cnodes:
        #if not nnode in nclosed:
        destdist=distances[nnode[0], nnode[1]]
        newdist = dist+weights[nnode[0], nnode[1]]
        if newdist < destdist :
            nopen.add(nnode)
            distances[nnode[0], nnode[1]] = newdist 
            previous[nnode[0]][nnode[1]] = node
    
    #print(distances)
print(weights)
node = (weights.shape[0]-2, weights.shape[1]-2)
danger = 0
visited = np.zeros_like(weights)
while True:
    danger += weights[node[0], node[1]]
    visited[node[0], node[1]] = danger
    node = previous[node[0]][node[1]]
    v = visited[1:-1, 1:-1].copy()
    v.transpose()
    if node == None: break
print(v)
l.transpose()
l[v<1]=0
print(l)
print(int(danger))
