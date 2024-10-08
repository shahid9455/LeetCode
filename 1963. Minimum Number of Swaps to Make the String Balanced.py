'''Link for this problem is here 
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
99% beats in memory
'''

class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0  # Tracks the balance between '[' and ']'
        max_imbalance = 0  # Tracks the deepest imbalance (max unmatched closing brackets)

        # Traverse the string character by character
        for char in s:
            if char == '[':
                balance += 1  # Opening bracket increases the balance
            else:
                balance -= 1  # Closing bracket decreases the balance

            # If the balance becomes negative, we track the max imbalance
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)

        # The number of swaps needed is half of the maximum imbalance
        return (max_imbalance + 1) // 2

# Instantiate the Solution class
sol = Solution()

# Test cases
print(sol.minSwaps("][]["))  # Output: 1
print(sol.minSwaps("]]][[["))  # Output: 2
print(sol.minSwaps("[]"))  # Output: 0
