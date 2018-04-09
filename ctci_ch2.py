# Chapter 2 - Linked Lists
from LinkedList import Node, LinkedList

# Problem 1 - Remove Dups
def removeDups(list1):
    dupDict = {}
    current = list1.head

    while current is not None:
        if current.get_data() in dupDict:
            list1.delete(current.get_data())
        else:
            dupDict[current.get_data()] = 1
        current = current.get_next()

    return list1

def returnKthToLast(list1, k):
    count = 1
    current = list1.head
    if list1.size() - k < 0:
        return None

    while count < list1.size() - k:
        current = current.get_next()
        count = count+1
    return current.get_data()

#Main Function
def main():
    linkedlist = LinkedList(5)
    linkedlist.insert(6)
    linkedlist.insert(7)
    linkedlist.insert(4)
    linkedlist.insert(3)
    linkedlist.insert(1)
    linkedlist.insert(7)
    linkedlist.insert(4)
    print returnKthToLast(linkedlist, 1)
    # print removeDups(linkedlist).toString()

if __name__ == "__main__":
    main()
