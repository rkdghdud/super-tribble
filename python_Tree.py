class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class NodeMgmt:
  def __init__(self, head):
    self.head = head
    
  def insert(self, value):
    self.current_node = self.head
    while True:
      if value < self.current_node.value:
        if self.current_node.left != None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value)
          break
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break
          
  def search(self, value):
    self.current_node = self.head
    while self.current_node:
      if self.current_node.value == value:
        return True
      elif self.current_node.value < value:
        self.current_node = self.current_node.right
      else:
        self.current_node = self.current_node.left
      return False
    
  def delete(self, value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    
    while self.current_node;
      if self.current_node.value == value:
        searched = True
        break
      elif self.current_node.value < value:
        self.parent = self.current_node
        self.current_node = self.current_node.right
      else:
        self.parent = self.current_node
        self.current_node = self.current_node.left
        
    if searched == False:
      return False
    
		#삭제 목표 노드가 리프 노드일때
    if self.current_node.left == None and self.current_node.right == None:
      if self.parent.value < value:
        self.parent.right = None
      else:
        self.parent.left = None
      del self.current_node
    	return True
		
		#삭제 목표 노드에 자식노드가 한개 존재할 때
    elif self.current_node.left == None and self.current_node.right != None:
			if value < self.parent.value:
				self.parent.left = self.currnet_node.right
			else:
				self.parent.right = self.current_node.right
		elif self.current_node.right == None and self.current_node.left != None:
			if value < self.parent.value:
				self.parent.left = self.current_node.left
			else:
				self.parent.right = self.current_node.left
			
					
