# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import Optional

# ListNode-luokka
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Itse ratkaisu
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node

# Apufunktio linked list rakentamiseen listasta
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Apufunktio tulostamaan linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)

head = build_linked_list([1, 2, 3, 4, 5])
solution = Solution()
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: [5, 4, 3, 2, 1]