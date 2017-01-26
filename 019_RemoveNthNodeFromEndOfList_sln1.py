# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        h = head
        while True:
            l.append(h)
            h = h.next
            if h == None:
                break
        length = len(l)
        l[length-1-n].next = l[length-n+1]
        return head

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

l1 = [1,2,3,4,5]
n = 2
sln = Solution()
printLinkList(sln.removeNthFromEnd(listToLinkList(l1), n))