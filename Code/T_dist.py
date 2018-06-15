
from ete3 import Tree,TreeStyle
from itertools import combinations
def prepostorder(self):
        _leaf = self.__class__.is_leaf
        to_visit = [self]
        

        while to_visit:
            node = to_visit.pop(-1)
            try:
                node = node[1]
            except TypeError:
              
                yield (False, node)
                if not _leaf(node):
                   
                    to_visit.extend(reversed(node.children + [[1, node]]))
            else:
           
                yield (True, node)
                
                
                
def path_from_root_to_node(t):
    d_node=dict()
    d_children=dict()
    edge = 0
    for node in t.traverse():
       if not node.is_leaf():
          node.name = edge
          edge += 1


    current_path = [t]
    for postorder, node in prepostorder(t):
        
        
        if postorder:
            
            current_path.pop(-1)
        else:
            if not node.children:
                
                
                d_node[node.name]=[]
                d_children[node.name]=[]
               
                for i in range(1,len(current_path)):  
              
                 
                    if current_path[i] !=0:
                        d_node[node.name].append(current_path[i])
                pass
                
            else:
                current_path.append(node.name)
                d_children[node.name]=[node.children[0].name,node.children[1].name]
    return d_node,d_children
def descendant_iterator(node, d_children, subtree):
    
    if len(d_children[node])!=0:
       
       for child in d_children[node]:
            if(isinteger(child)==False and child is not "[...]"):
                subtree.append(child)
                
            else:
                subtree=descendant_iterator(child, d_children, subtree)
    return subtree
    
def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
def main(arg1, arg2):              

    s2 = str(arg1)
    s1 = str(arg2)
    shared=0
    d_node=dict()
    d_path=dict()
    d_children=dict()
    t1 = Tree(s1)
    t2 = Tree(s2)
    L=[]
    for leaf in t1:
        L.append(leaf.name)
  
    d_node,d_children=path_from_root_to_node(t1)
    d_node2,d_children2=path_from_root_to_node(t2)
    
  
   
    d_node,d_children=path_from_root_to_node(t1)
    d_node2,d_children2=path_from_root_to_node(t2)
    
    Red=[]
    Blue=[]
    for node in t1.traverse("levelorder"):
         if not node.is_leaf():
            subtree1=[]
            subtree2=[]
            children=d_children[node.name]
            if(isinteger(children[0])==False):
                subtree1.append(children[0])
               
            if(isinteger(children[1])==False):
                subtree2.append(children[1])
                
            subtree1=descendant_iterator(children[0],d_children,subtree1)
            subtree2=descendant_iterator(children[1],d_children,subtree2)
 
            red=subtree1
            blue=subtree2
            for node in t2.traverse("levelorder"):
              if not node.is_leaf():
                subtree1=[]
                subtree2=[]
                children=d_children2[node.name]
                if(isinteger(children[0])==False ):
                    subtree1.append(children[0])
                    
                if(isinteger(children[1])==False):
                    subtree2.append(children[1])
                   
                subtree1=descendant_iterator(children[0],d_children2,subtree1)
                subtree2=descendant_iterator(children[1],d_children2,subtree2)
                subtree1_blue= list(set(subtree1).intersection(blue))
                subtree1_red=list(set(subtree1).intersection(red))
                subtree2_blue=list(set(subtree2).intersection(blue))
                subtree2_red =list(set(subtree2).intersection(red))
                sub1_b2= len( list(combinations(subtree1_blue,2)))
                sub1_r2= len( list(combinations(subtree1_red,2)))
                sub2_b2= len( list(combinations(subtree2_blue,2)))
                sub2_r2= len( list(combinations(subtree2_red,2)))
                shared=shared +sub1_b2*len(subtree2_red)+ sub1_r2*len(subtree2_blue)+sub2_r2*len(subtree1_blue)+sub2_b2*len(subtree1_red)
                
                
             
    dist=len( list(combinations(L,3)))-shared
    return dist


if __name__ == '__main__':

    main()