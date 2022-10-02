
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        init_val = (l1.val + l2.val) % 10
        addlist = ListNode(val =  init_val)
        carry = (l1.val + l2.val)//10
        curr_node = addlist

        while(l1.next and l2.next):

            l1 = l1.next
            l2 = l2.next

            curr_node.next = ListNode(val = (l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry)//10
            curr_node = curr_node.next

        while(l1.next):

            l1 = l1.next
            curr_node.next = ListNode(val = (l1.val + carry) % 10)
            carry = (l1.val + carry)//10
            curr_node = curr_node.next

        while(l2.next):

            l2 = l2.next
            curr_node.next = ListNode(val = (l2.val + carry) % 10)
            carry = (l2.val + carry)//10
            curr_node = curr_node.next

        if carry > 0:
            curr_node.next = ListNode(val=1)

        return addlist



""" #Uncomment to test the code

l1 = ListNode(val = 2)
l1.next = ListNode(val=6)
l1.next.next = ListNode(val=3)


l2 = ListNode(val=5)
l2.next = ListNode(val=6)
l2.next.next = ListNode(val=4)

ad = Solution()
add = ad.addTwoNumbers(l1,l2)

print(l1.next.next.val,l1.next.val,l1.val, " + ",l2.next.next.val,l2.next.val,l2.val, "=" , add.next.next.val,add.next.val,add.val)  
 """



