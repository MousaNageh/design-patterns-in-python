

class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
    
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    def __str__(self) -> str:
        return str(self.value)
            
 
#   1
#  / \
# 2   3

# in order : 213 

class InorderIterator:
    
    def __init__(self, root: Node) -> None:
        self.root = root 
        self.current: Node = root
        self.yielded_start = False 
        while self.current.left:
            self.current = self.current.left
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
        if self.current:
            return self.current
        else:
            raise StopIteration
    

# or we can use a function
def traverse_in_order(root):
  def traverse(current):
    if current.left:
      for left in traverse(current.left):
        yield left
    yield current
    if current.right:
      for right in traverse(current.right):
        yield right
  for node in traverse(root):
    yield node


root = Node(1, left=Node(2), right=Node(3))


for n in InorderIterator(root=root):
    print(n)

for n in traverse_in_order(root=root): 
    print(n)