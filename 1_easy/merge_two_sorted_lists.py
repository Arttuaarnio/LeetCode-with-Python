# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import Optional

# ListNode-luokka
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Itse ratkaisu
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = dummy_node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next
        current_node.next = list1 if list1 else list2
        return dummy_node.next

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

list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)
print_linked_list(merged)  # Output: [1, 1, 2, 3, 4, 4]