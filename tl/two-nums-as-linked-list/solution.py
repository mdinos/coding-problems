class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers:
    def __init__(self, l1: ListNode, l2: ListNode):
        self.l1 = self._generate_integer(l1)
        self.l2 = self._generate_integer(l2)
        self.total = str(self.l1 + self.l2)
        self.next()

    def next(self):
        len_total = len(self.total)
        if len_total != 0:
            self.val = self.total[-1]
            self.total = self.total[0:len_total - 1]
            return self
        else:
            return None

    def _generate_integer(self, l: ListNode):
        l_string = ''
        while True:
            l_string += str(l.val)
            if l.next == None:
                break
            l = l.next
        l_string = l_string[::-1]
        return int(l_string)