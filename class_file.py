class Node:
    def __init__(self,parent,value,node_list,children):
        self.parent=parent
        self.value=value
        self.children=children
        node_list.append(self)

    def add_child(self,child):
        self.children.append(child)


def BFS(node,s,g,path):
    current_node_list=[]
    current_node_list.append(node)
    explored_node_list=[]
    #print(current_node_list[0].value)
    path.append(current_node_list[0].value)
    while current_node_list!=[]:
        current_node=current_node_list[0]
        children=current_node.children
        for child in children[0]:
            current_node_list.append(child)
    #        print(child.value)
            path.append(child.value)
            if child.value==g:
                return path
        explored_node_list.append(current_node)
        del current_node_list[0]

def DFS(node,s,g,path):
    path.append(str(node.value))
    if node.value==g:
        return  True,path
    elif node.children==[]:
        return False,path
    else:
        for child in node.children[0]:
            signal,path=DFS(child,s,g,path)
            if signal==True:
                return True,path
        return False,path
