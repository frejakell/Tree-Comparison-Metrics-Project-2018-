#!/usr/bin/python
from ete3 import Tree
import random

import sys


rfdist = 0
leaf_num = 0 

def dfs( tree):
    if tree is None:
        return []
    visited, stack = [], [tree]
    while stack:
        node = stack.pop()
        visited.append(node)
        
        node_l,node_r=[],[]
        if node.is_leaf() is False:
            
            node_l=node.children[0]
        
            node_r=node.children[1]
            stack.extend(filter(None, [node_l, node_r]))  
        # append right first, so left will be popped first
    return visited
    
def dfs_assign( tree,tree2):
    if tree is None:
        return []
    visited, stack = [], [tree]
    leaves=[]
    while stack:
        node = stack.pop()
        visited.append(node)
        
        node_l,node_r=[],[]
        if node.is_leaf():
             leaves.append(node)
             node.add_features(order=len(leaves))
             
             CurrentNode2=tree2&node.name
             CurrentNode2.name=str(len(leaves))
             node.name=str(len(leaves))
        elif node.is_leaf() is False:
            
            node_l=node.children[0]
        
            node_r=node.children[1]
            stack.extend(filter(None, [node_l, node_r]))  
        # append right first, so left will be popped first
    return visited
def main(arg1,arg2):
   
    tree1=Tree(arg1)
    
    tree2=Tree(arg2)
        
    node_midpoint = tree1.get_leaf_names()[0]
   
    tree1.set_outgroup(node_midpoint)
    
    tree2.set_outgroup(node_midpoint)
    
    
    t1, tree2=tree2.get_tree_root().children
    t1, tree1=tree1.get_tree_root().children
    count = 0
    tree1_order=dfs_assign(tree1,tree2)

    Num_splits1=0
    Num_splits2=0
    Num_shared=0
    shared=dict()
    for node in tree1_order:
       
        if(node.is_leaf()==False):
            Num_splits1+=1
            subtree=node.get_leaf_names()
            cmin=min(subtree)
            cmax=max(subtree)
            if((node.is_root()==False)):
                shared["["+str(cmin)+":"+str(cmax)+"]"]=1
    
    for node in dfs(tree2):
        if(node.is_leaf()==False):
            Num_splits2+=1
            cmin=float("+inf")    
            cmax=0
            size=0
            subtree=node.get_leaf_names()
            cmin=min(subtree)
            cmax=max(subtree)
            size=len(subtree)  
            if(size==(int(cmax)-int(cmin)+1)):
               if("["+str(cmin)+":"+str(cmax)+"]" in shared):
                   Num_shared+=1

   
    rf_dist=Num_splits1+Num_splits2-(2*Num_shared)
   
    print(rf_dist)
    return rf_dist
   

    

if __name__ == "__main__":
    main()