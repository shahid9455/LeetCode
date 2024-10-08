#    https://leetcode.com/problems/reverse-nodes-in-k-group/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Function to reverse a portion of the linked list
        def reverseLinkedList(start: ListNode, end: ListNode) -> ListNode:
            prev = None
            current = start
            while current != end:
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp
            return prev  # New head of the reversed portion

        # Count the number of nodes in the linked list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        # Dummy node to handle edge cases and a pointer to track the previous group end
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while count >= k:
            group_start = group_prev.next
            group_end = group_start
            
            # Move to the end of the current group
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group_start = group_end.next
            
            # Reverse the current group
            group_end.next = None  # Temporarily terminate the current group
            group_prev.next = reverseLinkedList(group_start, None)  # Reverse and connect to the previous part
            group_start.next = next_group_start  # Connect the end of the reversed group to the next part
            
            # Move the group_prev pointer forward for the next group
            group_prev = group_start
            
            # Decrease the count by k
            count -= k
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list back to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
sol = Solution()

# Example 1
head1 = create_linked_list([1, 2, 3, 4, 5])
result1 = sol.reverseKGroup(head1, 2)
print(linked_list_to_list(result1))  # Output: [2, 1, 4, 3, 5]

# Example 2
head2 = create_linked_list([1, 2, 3, 4, 5])
result2 = sol.reverseKGroup(head2, 3)
print(linked_list_to_list(result2))  # Output: [3, 2, 1, 4, 5]
