# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next

# test
def listToLinkList(l):
    dummyHead = curr = ListNode(0)
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    return dummyHead.next

def printLinkList(listNode):
    l = []
    while True:
        l.append(listNode.val)
        if listNode.next == None:
            break
        listNode = listNode.next
    print(l)

lists = []
lists.append(listToLinkList([1, 5, 8, 15]))
lists.append(listToLinkList([3, 7, 13, 22]))
lists.append(listToLinkList([2, 4, 6, 20]))
lists.append(listToLinkList([4, 6, 19, 23]))
sln = Solution()
printLinkList(sln.mergeKLists(lists))