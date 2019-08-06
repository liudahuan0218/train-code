class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def ReverseList(pHead):
        # write code here
         
 
        # write code here
        if not pHead or not pHead.next:
            return pHead
          
        last = None
          
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

head = None
for count in range(1,6):
    head = Node(count, head)

H=ReverseList(head)
while H != None:
    print(H.data)
    
    H = H.next

