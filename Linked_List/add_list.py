# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. 
# The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; 
# this means that the least significant digit of the number is the head. 
# The function should return the head of a new linked listed representing the sum of the input lists. 
# The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  current_1 = head_1
  current_2 = head_2
  carry = 0
  dummy = Node(None)
  current = dummy
  while current_1 or current_2 or carry == 1:
    value_1 = current_1.val if current_1 else 0
    value_2 = current_2.val if current_2 else 0
    sum = value_1 + value_2 + carry
    
    if sum >= 10:
      carry = 1
      sum -= 10
    else:
      carry = 0
    current_1 = current_1.next if current_1 else None
    current_2 = current_2.next if current_2 else None
    current.next = Node(sum)
    current = current.next
  
    
  return dummy.next

# -------Test--------
#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

add_lists(a1, b1)
# 5 -> 7 -> 9

#   999
#  +  6
#  ----
#  1005

a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)
# 6

add_lists(a1, b1)
# 5 -> 0 -> 0 -> 1