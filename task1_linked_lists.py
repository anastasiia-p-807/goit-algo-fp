class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return
        self.head = self.merge_sort_helper(self.head)

    def merge_sort_helper(self, head):
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort_helper(head)
        right = self.merge_sort_helper(next_to_middle)
        return self.sorted_merge(left, right)

    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sorted_lists(self, list1, list2):
        self.head = self.sorted_merge(list1.head, list2.head)


llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

merged_list = LinkedList()
merged_list.merge_sorted_lists(llist1, llist2)

print("Merge two lists:")
merged_list.print_list()

print("Reverse it:")
merged_list.reverse()
merged_list.print_list()

print("Sort it:")
merged_list.merge_sort()
merged_list.print_list()