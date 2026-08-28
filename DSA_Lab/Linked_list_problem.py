class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


def solve_queue_split():
  n = int(input("Enter total people: "))

  if n <= 0:
    print("Number must be greater than 0")
    return

  head = None
  tail = None
  for i in range(1, n + 1):
    new_node = Node(i)
    if not head:
      head = new_node
      tail = new_node
    else:
      tail.next = new_node
      tail = new_node

  print("\n Original Queue:")
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.data))
    curr = curr.next
  print("-->".join(elements))

  if n == 1:
    print("\n Window 1 : 1")
    print("\nWindow 2: Empty")
    return

  mid = n // 2
  curr = head
  for _ in range(mid - 1):
    curr = curr.next

  head1 = head
  head2 = curr.next
  curr.next = None

  print(f"\n Window 1 (1 to {mid}):")
  curr = head1
  elements1 = []
  while curr:
    elements1.append(str(curr.data))
    curr = curr.next
  print("->".join(elements1))

  print(f"\n Window 2 ({mid + 1} to {n}):")
  curr = head2
  elements2 = []
  while curr:
    elements2.append(str(curr.data))
    curr = curr.next
  print("->".join(elements2))


# Make sure this call has 0 indentation (at the very left margin)
solve_queue_split()