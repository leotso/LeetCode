# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if None in (l1, l2):
            return l1 or l2
        
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

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

sln = Solution()
l1 = [1, 5, 8, 15]
l2 = [3, 7, 13, 22]
printLinkList(sln.mergeTwoLists(listToLinkList(l1),listToLinkList(l2)))