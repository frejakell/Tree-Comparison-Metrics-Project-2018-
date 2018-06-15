import time
import string
from itertools import combinations, permutations, product
import re
import random


def Insert_Current_Leaf(tree, label):
  yield [label, tree]
  if len(tree)== 2:
    for left in Insert_Current_Leaf(tree[0], label):
      new_node=[left, tree[1]]
    
      yield new_node
    for right in Insert_Current_Leaf(tree[1], label):
      new_node=[tree[0], right]
 
      yield new_node
 
def All_possible_rooted(labels):     
  leaf=labels.pop()
  if len(labels) == 0:
    yield leaf
  else:
    for tree in All_possible_rooted(labels):
      for new_tree in Insert_Current_Leaf(tree, leaf):
        yield new_tree
    
def main(arg1=5,arg2="R"):
   
    start=time.time()
    list1=[]
    list2=[]    
    tree_set=[]
    leaves=list(string.ascii_lowercase)[0:arg1]
    leaf_list=leaves
    if arg2=="R" or arg2=="r":
        for stree in All_possible_rooted((leaf_list)):
        
        
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
        out_g=leaf_list.pop()
        for stree in All_possible_rooted((leaf_list)):
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
