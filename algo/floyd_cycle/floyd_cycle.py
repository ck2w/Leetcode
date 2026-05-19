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



def floyd_full(head):
    """返回 (环入口节点, 环长度)，无环返回 (None, 0)"""
    # 阶段一：检测环
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None, 0  # 无环

    # 阶段二：找环入口
    a, b = head, slow
    while a != b:
        a = a.next
        b = b.next

    # 阶段三：从入口数一圈
    length = cycle_length(slow)  # 相遇点和入口在同一个环里，从哪里数都一样

    return a, length