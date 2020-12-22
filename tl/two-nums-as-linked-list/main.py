from time import sleep
from solution import *

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = AddTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next()
# 7 0 8