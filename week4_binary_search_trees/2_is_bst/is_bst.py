#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Trees:
  def __init__(self, tree):
    self.n = len(tree)
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.is_left_child_of = [-1 for i in range(self.n)]
    self.is_right_child_of = [-1 for i in range(self.n)]
    for i, item in enumerate(tree):
      self.key[i] = item[0]
      self.left[i] = item[1]
      self.right[i] = item[2]

  def inOrder(self):
    self.result = []
    self.inOrderTraversal(0)
    return self.result

  def inOrderTraversal(self,r):
    if r == -1:
        return
    self.inOrderTraversal(self.left[r])
    self.result.append(self.key[r])
    self.inOrderTraversal(self.right[r])

def IsBinarySearchTree(tree):
  if len(tree) == 0:
      return True
  treeorder = Trees(tree) 
  traversal = treeorder.inOrder()
  return traversal == sorted(traversal)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
