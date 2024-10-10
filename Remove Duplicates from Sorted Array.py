# Problem Statement

'''
Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relat
elements should be kept the same. Then return the number of unique elements in nums .
Consider the number of unique elements of nums to be k , to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaini
nums are not important as well as the size of nums .
Return k .
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
 assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 re
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

#  Solution

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  # Pointer for unique elements

        # Traverse through the array starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1  # Move i to the next position
                nums[i] = nums[j]  # Update the element at i with the new unique value

        return i + 1  # i is index-based, so the length is i + 1
# Testing with some examples:
nums1 = [1, 1, 2]
solution = Solution()
k1 = solution.removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]}")  # Expected: 2, nums = [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]}")  # Expected: 5, nums = [0, 1, 2, 3, 4]
