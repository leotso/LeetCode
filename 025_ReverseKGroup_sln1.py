# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        pre.next = head
        while True:
            flag = True
            curr = pre
            for i in xrange(k):
                if curr.next == None:
                    flag = False
                    break
                curr = curr.next
            if not flag:
                break
            preEnd = pre.next
            for i in xrange(k-1):
                end = preEnd.next
                eNext = preEnd.next.next
                end.next = pre.next
                pre.next = end
                preEnd.next = eNext
            pre = preEnd

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

l = listToLinkList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sln = Solution()
printLinkList(sln.reverseKGroup(l, 2))