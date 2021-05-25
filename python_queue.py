import queue

#normal queue (fifo)
data_queue = queue.Queue()

data_queue.put("queue")
data_queue.put(1)

data_queue.qsize()

data_queue.get()

#LIFO Queue
data_lifoqueue = queue.LifoQueue()

data_lifoqueue.put("lifoqueue")
data_lifoqueue.put(2)

data_lifoqueue.qsize()
data_lifoqueue.get()

#PriorityQueue
data_pqueue = queue.PriorityQueue()

data_pqueue.put((10, "korea"))
data_pqueue.put((5, 1))
data_pqueue.put((15, "china"))

data_pqueue.qsize()

data_pqueue.get()

#implement enqueue(), dequeue() through list
list_ = list()

def enqueue(a):
  list_.append(a)
  
def dequeue():
  a = list_[0]
  del list_[0]
  return a
