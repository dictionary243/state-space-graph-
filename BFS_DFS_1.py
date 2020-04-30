from class_file import *
char_index_dict={}#{'a':0}
index_char_dict={}#{0:'a'}
node_dict={}#{0:node_a,......}

parent_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
children_dict={'a':['b','c','d'],'b':['e','f'],'c':['g','h'],'d':['i','j'],'e':['k','l'],'f':['m'],'g':['n'],'h':['o'],'i':['p','q'],'j':['r'],'k':['s'],'l':['t'],'p':['u']}

for i in range(len(parent_list)):
    ch=parent_list[i]
    char_index_dict[ch]=i
    index_char_dict[i]=ch
    node=Node(ch,[])
    node_dict[i]=node

for key in children_dict.keys():
        index=char_index_dict[key]
        children=children_dict[key]
        child=[]
        node=node_dict[index]
        for ch in children:
            node_index=char_index_dict[ch]
            child.append(node_dict[node_index])
        node.add_child(list(child))

start='a'
goal='n'

root=node_dict[char_index_dict[start]]

path_BFS=BFS(root,'a','n',[])
result,path_DFS=DFS(root,'a','n',[])

print("----------------------------------------------------------------")
print("In BFS the path is : "+"->".join(str(x) for x in path_BFS) )
print("total visited_nodes in BFS is :"+str(len(path_BFS)))
print("--------------------------------------------------------")
print("In DFS the path is : "+"->".join(str(x) for x in path_DFS) )
print("total visited_nodes in DFS is:"+str(len(path_DFS)))
print("---------------------------------------------------------")
