
# list
sum([[2,3], [1,2]], []) # flatten [2,3,1,2]


# set
a = set([2,4])
a.add(3)
a.remove(4)

a & b  # intersection
a.intersection(b)  # intersection
a | b  # union
a.union(b)  # union


# heapq
import heapq

c = Counter(nums)
maxheap = []
heapq.nlargest(k, c.keys(), key=c.get)
heapq.nsmallest(k, c.keys(), key=c.get)
heapq.heappush(maxheap, [distance, point])
heapq.heappop(maxheap)


# Counter
from collections import Counter

c1 = Counter(nums1)
c2 = Counter(nums2)
c1 - c2
c1 & c2  # get min
c2 | c2  # get max
top_three = c1.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


# Queue
from queue import Queue

q = Queue()
q.put(i)
q.get(i)


# deque
from collections import deque

q = deque()
q.append('o')
q.appendleft('h')
q.pop()
q.popleft()
q.extend([1,2,3])
q.extendleft([1,2,3])



def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    from collections import Counter
    import heapq

    c = Counter(nums)
    # return [x[0] for x in c.most_common(k)]
    return heapq.nlargest(k, c.keys(), key=c.get)


# binary search
def binarySearch(nums, target):
    # find val (whatever first/last)
    if len(nums) == 0:
        return -1

    low, hi = 0, len(nums) - 1
    while low <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # End Condition: left > right
    return -1 # exact solution
    return hi # floor solution
    return lo # ceil solution

def binarySearch(nums, target):
    # find first (vals duplicate)
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (hi + lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    if lo == len(nums) or nums[lo] != target :
        return -1
    else:
        return lo

def binarySearch(nums, target):
    # find last
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (hi + lo) // 2
        if nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid
    if lo == len(nums) or nums[lo] != target :
        return -1
    else:
        return lo



def maxSubArray(self, nums: List[int]) -> int:
    # Kadane's Algorithm
    # Initialize our variables using the first element.
    current_subarray = max_subarray = nums[0]

    # Start with the 2nd element since we already used the first one.
    for curr in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        # two rolling max
        current_subarray = max(curr, current_subarray + curr)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray


# Floyd's determined cycle exists
def hasCycle(self, head: ListNode) -> bool:
    if not head: return False
    
    tor = head
    hare = head.next
    while tor != hare:
        if hare is None or hare.next is None:
            return False
        tor = tor.next
        hare = hare.next.next
    return True


# Floyd's find cycle start
def cycleStart(self, nums: List[int]) -> int:
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]] # hare is twice faster
        if tortoise == hare:
            break
    
    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]  # all move with tortoise speed
    
    return hare

# quick sort
def quickSort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists


# binary tree serialize and deserialize
class Codec:
    def serialize(self, root):        
        def do_serialize(root, s):
            if not root:
                s = s + 'None,'

            else:
                s = s + str(root.val) + ','
                s = do_serialize(root.left, s)
                s = do_serialize(root.right, s)
            return s
        return do_serialize(root, '')

    def deserialize(self, data):
        def do_deserialize(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            else:
                new_root = TreeNode(int(lst[0]))
                lst.pop(0)
                new_root.left = do_deserialize(lst)
                new_root.right = do_deserialize(lst)

                return new_root
        
        data_lst = data.split(',')
        root = do_deserialize(data_lst)
        return root


# binary tree traversal
# inorder: left->node->right, dfs

def preorderTraversal(self, root):
    if root is None:
        return []
    
    stack, output = [root, ], []
    
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    
    return output

def preorderTraversal(self, root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:  
                res.append(node.val)
            else:  # preorder: root -> left -> right
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
    return res

def inorderTraversal(self, root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res

def inorder(self, r: TreeNode):
    return self.inorder(r.left) + [r.val] + self.inorder(r.right) if r else []
        

def postorderTraversal(self, root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # postorder: left -> right -> root
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res

def levelOrder(self, root):
    levels = []
    if not root:
        return levels
    
    def helper(node, level):
        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
        
    helper(root, 0)
    return levels


# bfs-graph
from collections import deque
def bsf_graph(root):
    if not root:
        return
    queue = deque([root])    
    visited = set([root])
    while queue:
        node = queue.popleft()
        # do somethings with the head node or neighbors
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return xxx

# dfs-graph
def dfs_graph(root):
    if not root:
        return
    stack = [root]
    visited = set([root])
    while stack:
        node = stack.pop()
        # do somethings with the head node or neighbors
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return xxx


