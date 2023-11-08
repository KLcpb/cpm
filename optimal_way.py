# A B C D E F
letters = ["A","B","C","D","E","F"]
path = []
for i in letters:
    a = input(f"print connections with node {i} -> ").split(" ")
    a = map(int,a)
    path.append(list(a))
#path = [[0,3,6,-1,1,7],[3,0,2,9,5,-1],[6,2,0,10,8,13],[-1,9,10,0,3,2],[1,5,8,3,0,6],[7,-1,13,2,6,0]]
ans = []
ways = []
def voyage(curr_node,already_gone,dont_go,way):
    
    if path.index(curr_node) == len(path)-1:
        ans.append(already_gone)
        ways.append(way)
        return
    for i in range(len(curr_node)):
        if curr_node[i] == -1 or curr_node[i] == 0 or i in dont_go:
            continue
        voyage(path[i],already_gone + curr_node[i],dont_go + [i],way+[i])

voyage(path[0],0,[],[0])

print("the shortest way is", min(ans))


for i in ways[ans.index(min(ans))]:
    print("-> ",letters[i])