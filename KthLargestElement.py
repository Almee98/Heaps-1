import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        ans = heapq.nlargest(k, nums)
        return ans[-1]

# Time Complexity : O(NlogK), where N is the number of elements in the array and K is the size of the heap
# Space Complexity : O(K), for the heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach 2: Using a min heap of size k
# We use a min heap to keep track of the k largest elements seen so far.
# When the size of the heap exceeds k, we remove the smallest element (the root of the min heap).
# We can be sure that the root of the min heap will not be one of the k largest elements.
# Once we have processed all the elements, the root of the min heap will be the k-th largest element.
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # Initialize a min heap
        heap = []
        # Iterate through the numbers
        for n in nums:
            # Add the number to the heap
            heapq.heappush(heap, n)
            # If the size of the heap exceeds k, remove the smallest element
            if len(heap) > k:
                heapq.heappop(heap)
        # The root of the min heap is the k-th largest element
        return heap[0]

# Time Complexity : O(Nlog(N-K)), where N is the number of elements in the array and K is the size of the heap
# Space Complexity : O(K), for the heap
# Approach:
# We can also use a max heap to solve this problem.
# Here, we pop the largest element from the heap once we have n-k elements in the heap.
# We compare the popped element with the current maximum and update the maximum if necessary.
# The final result will be the maximum of all popped elements.
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # Initialize a max heap
        heap = []
        # Initialize the result to negative infinity
        # This is because we are using a max heap and we want to find the maximum of the popped elements
        res = float('-inf')

        # Iterate through the numbers
        for n in nums:
            # Add the negative of the number to the heap
            # This is because heapq in Python is a min heap by default
            heapq.heappush(heap, -n)
            # If the size of the heap exceeds len(nums)-k, pop the largest element
            if len(heap) > len(nums)-k:
                # And update the result if necessary
                res = max(res, heapq.heappop(heap))
        # The result will be the maximum of all popped elements
        # Since we stored the negative of the numbers in the heap, we need to negate the result
        return res * -1