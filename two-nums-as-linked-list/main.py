class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0):
        self.l1 = self._generate_integer(l1)
        self.l2 = self._generate_integer(l2)
        self.total = self.l1 + self.l2
        self.next = self._get_next()

    def _generate_integer(self, l: ListNode):
        l_string = ''
        while True:
            l_string += str(l.val)
            if l.next == None:
                break
            l = l.next
        l_string = l_string[::-1]
        return int(l_string)

    def _get_next(self):
        self.val = str(self.total)[-1]
        if len(str(self.total)) 
        int(str(self.total)[:-1])
        return True


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8