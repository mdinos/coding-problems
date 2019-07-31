from time import sleep

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0):
        self.l1 = self._generate_integer(l1)
        self.l2 = self._generate_integer(l2)
        print('l1: {}  l2: {}'.format(self.l1, self.l2))
        self.total = str(self.l1 + self.l2)
        print('total: {}'.format(self.total))
        self.next = self._get_next()
        print('next: {}'.format(self.next))
        print('val: {}'.format(self.val))
        return self

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
        len_total = len(self.total)
        if len_total != 0:
            print('if\'d')
            print('val 01: {}'.format(self.val))
            print('total 01: {}'.format(self.total))
            self.total = self.total[1:len_total]
            self.val = self.total[-1]
            print('total 02: {}'.format(self.total))
            print('val 02: {}'.format(self.val))
            return self
        else:
            print('else\'d')
            return None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    print('sleeping 3s')
    sleep(3)
    result = result.next
    
# 7 0 8