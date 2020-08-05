from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node.previous_element = temp_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Checking to see if the list is empty,
        # if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            self.head_node.previous_element = None
            first_element.next_element = None
        return

    def delete(self, dt):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted
        if self.head_node.next_element.data == dt:
            self.delete_at_head()
            deleted = True

        temp_node = self.head_node.next_element
        previous_node = None

        # Traversing/Searching for Node to Delete
        while temp_node is not None and deleted is False:
            if dt == temp_node.data:
                previous_node.next_element = temp_node.next_element
                deleted = True
                break
            previous_node = temp_node
            temp_node = temp_node.next_element

        if deleted is False:
            print(dt,  " is not in List!")
        else:
            print(dt,  " is deleted!")
        return deleted

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while temp is not None:
            if (temp.data == dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None
