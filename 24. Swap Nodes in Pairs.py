#     https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1416056794/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = first.next
            
            # Performing the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev to the next pair
            prev = first
        
        # Return the new head
        return dummy.next

# Helper function to convert a list to a linked list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
sol = Solution()

# Example 1
head1 = create_linked_list([1, 2, 3, 4])
result1 = sol.swapPairs(head1)
print(linked_list_to_list(result1))  # Output: [2, 1, 4, 3]

# Example 2
head2 = create_linked_list([])
result2 = sol.swapPairs(head2)
print(linked_list_to_list(result2))  # Output: []

# Example 3
head3 = create_linked_list([1])
result3 = sol.swapPaclass ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = first.next
            
            # Performing the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev to the next pair
            prev = first
        
        # Return the new head
        return dummy.next

# Helper function to convert a list to a linked list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
sol = Solution()

# Example 1
head1 = create_linked_list([1, 2, 3, 4])
result1 = sol.swapPairs(head1)
print(linked_list_to_list(result1))  # Output: [2, 1, 4, 3]

# Example 2
head2 = create_linked_list([])
result2 = sol.swapPairs(head2)
print(linked_list_to_list(result2))  # Output: []

# Example 3
head3 = create_linked_list([1])
result3 = sol.swapPairs(head3)
print(linked_list_to_list(result3))  # Output: [1]

# Example 4
head4 = create_linked_list([1, 2, 3])
result4 = sol.swapPairs(head4)
print(linked_list_to_list(result4))  # Output: [2, 1, 3]
irs(head3)
print(linked_list_to_list(result3))  # Output: [1]

# Example 4
head4 = create_linked_list([1, 2, 3])
result4 = sol.swapPairs(head4)
print(linked_list_to_list(result4))  # Output: [2, 1, 3]
