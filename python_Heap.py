class Max_heap:
  def __init__(self, data):
    self.heap_array = list()
    self.heap_array.append(None)
    self.heap_array.append(data)
    
  def move_up(self, insearted_idx):
    if insearted_idx < 2:
      return False
    parent_idx = insearted_idx // 2
    if self.heap_array[insearted_idx] > self.heap_array[parent_idx]:
      return True
    else:
      return False
  def move_down(self, popped_idx):
    left_child = popped_idx * 2
    right_child = popped_idx * 2 + 1
    
    if left_child >= len(self.heap_array):
      return False
    ====================#need add
    
  def insert(self, data):
    if len(self.heap_array) == 0:
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True

    self.heap_array.append(data)
    insearted_idx = len(self.heap_array) - 1
    
    while self.move_up(insearted_idx):
      parent_idx = insearted_idx // 2
      self.heap_array[insearted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[insearted_idx]
      inseated_idx = parent_idx
      
    return True
  
  def delete(self):
    if len(self.heap_array) <= 1:
      return None
    return_data = self.heap_array[1]
    self.heap_array[1] = self.heap_array[-1]
    del self.heap_array[-1]
       ====================#need add 
    
