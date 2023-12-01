# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1 
  current_1 = head_1.next
  current_2 = head_2
  count = 0 
  
  while current_1 and current_2:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next 
    else:
      tail.next = current_1
      current_1 = current_1.next 
    tail = tail.next 
    count += 1
    
  if current_1:
    tail.next = current_1
  
  if current_2: tail.next = current_2
  
  return head_1

# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# # a -> b -> c

# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# x -> y -> z

# zipper_lists(a, x)
# a -> x -> b -> y -> c -> z