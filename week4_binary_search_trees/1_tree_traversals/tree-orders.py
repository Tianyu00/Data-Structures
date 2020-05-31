# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

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

  def preOrderTraversal(self,r):
    if r == -1:
        return
    self.result.append(self.key[r])
    self.preOrderTraversal(self.left[r])
    self.preOrderTraversal(self.right[r])

  def postOrderTraversal(self,r):
    if r == -1:
        return
    self.postOrderTraversal(self.left[r])
    self.postOrderTraversal(self.right[r])
    self.result.append(self.key[r])

  def preOrder(self):
    self.result = []
    self.preOrderTraversal(0)
    return self.result

  def postOrder(self):
    self.result = []
    self.postOrderTraversal(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
