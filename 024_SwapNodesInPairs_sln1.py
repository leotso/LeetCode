# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(sefl, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        curr.next = head
        while curr.next and curr.next.next:
            curr.next, curr.next.next, curr.next.next.next = curr.next.next, curr.next, curr.next.next.next
            curr = curr.next.next
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

l1 = listToLinkList([1, 2, 3, 4])
l2 = listToLinkList([1, 2, 3, 4, 5, 6, 7])
sln = Solution()
printLinkList(sln.swapPairs(l1))
printLinkList(sln.swapPairs(l2))