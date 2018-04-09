class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(head)

    def get_head(self):
        return self.head

    def insert(self, data):
        new_node = Node(data)
        n = self.head
        while (n.get_next() != None):
            n = n.get_next()
        n.set_next(new_node)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def toString(self):
        ret = ""
        temp = self.head
        while temp is not None:
            ret = ret + str(temp.get_data()) + " "
            temp = temp.get_next()
        return ret
