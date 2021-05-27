hash_table = list([i for i in range(10)]) #implement hash table as list

def hash_func(key):
  return key % 5 #Division

def storage_data(key_str, value):
  hash_address = hash_func(ord(key_str[0])
  hahs_table[hash_address] = value
  
def get_data(key_str):
  hash_address = hash_func(ord(key_str[0])
  return hash_table[hash_address]
#ord() == return ASCII
#use a key as first of string
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

get_data('Andy')
