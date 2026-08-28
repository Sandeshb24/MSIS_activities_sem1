class Node:

  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None


class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_head(self, data):
    """O(1) Insertion at the beginning."""
    new_node = Node(data)
    if not self.head:
      self.head = self.tail = new_node
      return

    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

  def insert_at_tail(self, data):
    """O(1) Insertion at the end."""
    new_node = Node(data)
    if not self.tail:
      self.head = self.tail = new_node
      return

    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

  def delete_node(self, node):
    """O(1) Deletion of a given node reference."""
    if not node:
      return

    # Update head pointer if deleting the first node
    if node == self.head:
      self.head = node.next

    # Update tail pointer if deleting the last node
    if node == self.tail:
      self.tail = node.prev

    # Unlink references
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev

    node.prev = None
    node.next = None

  def reverse(self):
    """O(N) In-place reversal of the list by swapping pointers."""
    current = self.head
    self.tail = self.head  # Old head becomes new tail

    temp = None
    while current:
      # Swap prev and next pointers
      temp = current.prev
      current.prev = current.next
      current.next = temp
      # Advance along the original list (now stored in current.prev)
      current = current.prev

    # Update new head
    if temp:
      self.head = temp.prev

  def display_forward(self):
    """O(N) Traversal from head to tail."""
    elements = []
    curr = self.head
    while curr:
      elements.append(str(curr.data))
      curr = curr.next
    print(" None <-> " + " <-> ".join(elements) + " <-> None")


# --- Demonstration ---
dll = DoublyLinkedList()

# Insertions
dll.insert_at_tail(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.insert_at_head(5)

dll.display_forward()
# Output:  None <-> 5 <-> 10 <-> 20 <-> 30 <-> None

# Reversal
dll.reverse()
dll.display_forward()
# Output:  None <-> 30 <-> 20 <-> 10 <-> 5 <-> None

# O(1) Deletion given a node reference (deleting node with value 20)
target_node = dll.head.next  # Node containing 20 after reversal
dll.delete_node(target_node)
dll.display_forward()
# Output:  None <-> 30 <-> 10 <-> 5 <-> None