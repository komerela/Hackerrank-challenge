
# Initialize an empty linked list using the method
class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class SinglyLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :  ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    # 2
    def count_nodes(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            n = 0
            print("Number of Nodes is:  " ,n)
            p = self.start

            while p is not None: 
                n+=1
                p = p.link
    # 3
    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            else:
                print(x," not found in the list")
                return False


    # 4
    def insert_node_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    # 5
    def insert_node_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
            p.link =temp



    # 6
    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_node_end(data)

    # 7
    def insert_after_specific_node(self, data, x):
        pass

    # 8
    def insert_before_specific_node(self, data, x):
        pass

    # 9
    def insert_node_specific_position(self, data, k):
        pass

    # 10
    def delete_node(self, x):
        pass

    # 11
    def delete_first_node(self):
        pass

    # 12
    def delete_last_node(self):
        pass

    #13
    def reverse_list(self):
        pass

    # 14
    def bubble_sort_by_exchanging_data(self):
        pass

    # 15
    def bubble_sort_by_exchanging_links(self):
        pass

    # 16
    def cycle(self):
        pass

    # 17
    def find_cycle(self):
        pass

    # 18
    def remove_cycle(self):
        pass

    # 19
    def insert_cycle(self, x):
        pass

    # 20
    def merge2(self, list2):
        pass

    # 21
    def _merge2(self, p1, p2):
        pass

    # 22
    def merge_sort(self):
        pass

    # 23
    def merge_sort_rec(self, listStart):
        pass

    # 24
    def divide_list(self, p):
        pass

# Create a new singly list instance
list = SinglyLinkedList()

# Create an empty list
list.create_list()

while True:
    print("1. Display list")
    print("2. Count the number of nodes")
    print("3. Search for an element")
    print("4. Insert node in an empty list/ Insert in the beginning of the list")
    print("5. Insert node at the end of the list")
    print("6. create_list")
    print("7. Insert node after a specified node")
    print("8. Insert node before a specified node")
    print("9. Insert node at a given position k")
    print("10. Delete first node")
    print("11. Delete last node")
    print("12. Delete any node")
    print("13. Reverse the list")
    print("14. Bubble sort by exchanging data")
    print("15. Bubble sort by exchanging links")
    print("16. MergeSort")
    print("17. Insert Cycle")
    print("18. Detect Cycle")
    print("19. Remove cycle")
    print("20. Quit")

    option = int(input("Enter your choice : " ))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        list.search()
    elif option == 4:
        list.insert_node_in_beginning()
    elif option == 5:
        list.insert_node_end()
    elif option == 6:
        list.create_list()
    elif option == 7:
        list.insert_after_specific_node()
    elif option == 8:
        list.insert_before_specific_node()
    elif option == 9:
        list.insert_node_specific_position()
    elif option == 10:
        list.delete_node()
    elif option == 11:
        list.delete_first_node()
    elif option == 12:
        list.delete_last_node()
    elif option == 13:
        list.reverse_list()
    elif option == 14:
        list.bubble_sort_by_exchanging_data()
    elif option == 15:
        list.bubble_sort_by_exchanging_links()
    elif option == 16:
        list.cycle()
    elif option == 17:
        list.find_cycle()
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        list.insert_cycle()
    elif option == 20:
        break
    else:
        print("Wrong option")

    print()