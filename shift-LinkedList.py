"""
arr = [7,8,9], so len(arr) = 3.
If shift=1, right_moves=3-1=2, arr=[9,7,8]; shifting=5=(5%3)=2,new_tail_pos=3-2=1, arr=[];
If shift=-1,new_tail_pos=1, arr = [8,9,7];
"""

class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None


def array_to_LL(array):
    nxt = None
    for i in range(len(array) - 1, -1, -1):
        head = LinkedList(array[i])
        head.next = nxt
        nxt = head
    return head


def print_LL(head):
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    print(result)


def shift_LL(head, k):
    n = 1
    old_tail = head
    while old_tail.next is not None:
        n += 1
        old_tail = old_tail.next

    offset = abs(k) % n
    if offset == 0:
        return head
    right_moves = n - offset if k > 0 else offset
    new_tail = head
    for i in range(1, right_moves):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    old_tail.next = head
    return new_head

if __name__ == "__main__":
    arr1 = [7,8,9]
    head1 = array_to_LL(arr1)
    print("Before shifting: ")
    print_LL(head1)
    print("After shifting: ")
    result11 = shift_LL(head1, 1)
    print_LL(result11)

    head1 = array_to_LL(arr1)
    result12 = shift_LL(head1, 5)
    print_LL(result12)

    head1 = array_to_LL(arr1)
    result13 = shift_LL(head1, -1)
    print_LL(result13)

    head1 = array_to_LL(arr1)
    result14 = shift_LL(head1, -5)
    print_LL(result14)
