import time
import string
from itertools import combinations, permutations, product
import re
import random


def Insert_Current_Leaf(tree, C_leaf):
  yield [tree,C_leaf]
  if len(tree)== 2:
    for node in Insert_Current_Leaf(tree[0], C_leaf):
      new_node=[tree[1],node]
      yield new_node
    for node in Insert_Current_Leaf(tree[1], C_leaf):
      new_node=[node,tree[0]]
      yield new_node
 
def All_possible_rooted(LeafNum): 
  if LeafNum <= 0: yield 'a'
  else:
      Leaf_List=list(string.ascii_lowercase)[LeafNum:LeafNum+1]
      leaf=Leaf_List[0]
      if(Leaf_List):
          for tree in All_possible_rooted(LeafNum-1):
              new_trees=Insert_Current_Leaf(tree, leaf)
              for C_tree in new_trees:
                  yield C_tree 
  
    
def main(arg1=5,arg2="R"):
   
    start=time.time()
    list1=[]
    list2=[]    
    tree_set=[]
   
    if arg2=="R" or arg2=="r":
        tree_struct= All_possible_rooted(arg1-1)
        for stree in tree_struct:
            treeNewick=""
            string_tree=str(stree)
            for i in range(0,len(string_tree)) :
                treeNewick=treeNewick+string_tree[i]
               
            treeNewick=treeNewick+';'
            treeNewick=re.sub(r"\s+", '', treeNewick)
            treeNewick=treeNewick.replace("[", "(")
            treeNewick=treeNewick.replace("]", ")")
            treeNewick=treeNewick.replace("'", "")
            tree_set.append(treeNewick)
           
    
    elif arg2=="U" or arg2=="u":
        out_g=list(string.ascii_lowercase)[0:arg1].pop()
        for stree in All_possible_rooted(arg1-2):
            treeNewick=""
            string_tree=str(stree)
            for i in range(0,len(string_tree)) :
                treeNewick=treeNewick+string_tree[i]
           
            treeNewick=re.sub(r"\s+", '', treeNewick)
            treeNewick=treeNewick.replace("[", "(")
            treeNewick=treeNewick.replace("]", ")")
            treeNewick=treeNewick.replace("'", "")
              
            treeNewick='('+treeNewick+ ','+out_g +');'
            tree_set.append(treeNewick)
           
         
   

    return tree_set
   
    
if __name__ == '__main__':
    
    main()
