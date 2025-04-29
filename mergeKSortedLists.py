# Time Complexity : O(N*k), where N is the total number of nodes in all lists and k is the number of lists
# Space Complexity : O(1)

# Approach:
# We can iteratively merge the k sorted linked lists using a helper function.
# The helper function takes two sorted linked lists and merges them into one sorted linked list.
# We can use a dummy node to simplify the merging process.
# While merging, we compare the values of the two lists and append the smaller value to the merged list.
# We continue this process until one of the lists is empty.
# Finally, we append the remaining elements of the non-empty list to the merged list.
# We repeat this process until all k lists are merged into one sorted linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        # Helper function to merge two sorted linked lists
        # This function takes two sorted linked lists and merges them into one sorted linked list
        def merge(h1, h2):
            # Create a dummy node to simplify the merging process
            # The dummy node will be the head of the merged list
            dummy = ListNode(float("-inf"))
            # Initialize a curr pointer to keep track of the current node in the merged list
            curr = dummy
            # While both lists are not empty, compare the values and append the smaller value to the merged list
            # Move the curr pointer to the next node in the merged list
            # Move the pointer of the list from which the value was taken to the next node
            while h1 and h2:
                if h1.val <= h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next
            # If one of the lists is empty, append the remaining elements of the non-empty list to the merged list
            if h1:
                curr.next = h1
            elif h2:
                curr.next = h2
            # Return the merged list starting from the node next to the dummy node
            return dummy.next

        # If the input list is empty, we don't need to merge anything
        if not lists:
            return None
        # If the input list has only one list, we can return that list as the merged list
        if len(lists) == 1:
            return lists[0]
        # If the input list has more than one list, we can merge them iteratively
        n = 2
        # Start with the first two lists and merge them
        head1, head2 = lists[0], lists[1]
        merged = merge(head1, head2)
        # Merge the remaining lists one by one
        while n < len(lists):
            # Merge the merged list with the next list in the input list
            # Update the merged list to be the result of merging the merged list with the next list
            head = lists[n]
            merged = merge(merged, head)
            # Increment the index to move to the next list
            n += 1
        # Return the final merged list
        return merged

# Time Complexity : O(Nlogk), where N is the total number of nodes in all lists and k is the number of lists
# Space Complexity : O(k), for the heap

# Approach 2: Using a min heap
# We can also use a min heap to solve this problem.
# We push the head of each linked list into the min heap.
# The heap will contain the smallest element from each list.
# We pop the smallest element from the heap and add it to the merged list.
# After popping, we push the next element from the same list into the heap.
# We repeat this process until the heap is empty.
import heapq    
class Solution:
    def mergeKLists(self, lists):
        # Create a dummy node to simplify the merging process
        dummy = ListNode(float("-inf"))
        # Initialize a curr pointer to keep track of the current node in the merged list
        curr = dummy
        # Initialize a min heap to keep track of the smallest element from each list
        heap = []

        # Iterate through the input list and push the head of each linked list into the min heap
        for i in range(len(lists)):
            # If the list is not empty, push the head of the list into the heap
            if lists[i]:
                 # We can use a tuple (value, index, node) to keep track of the value, index of the list, and the node itself.
                # This is necessary to avoid comparison issues with ListNode objects in the heap.
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # While the heap is not empty, pop the smallest element from the heap and add it to the merged list
        # After popping, push the next element from the same list into the heap
        # Repeat this process until the heap is empty
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            # If the popped node has a next node, push it into the heap
            # This ensures that we always have the smallest element from each list in the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        # Return the merged list starting from the node next to the dummy node  
        return dummy.next