import random
SIZE_OF_HASH_TABLE = 4

def ord_sum_hash(element):
    """Takes in a string and spits out a number between 0 and 9."""
    modulus = SIZE_OF_HASH_TABLE
    ord_list = [ord(char) for char in element]
    return sum(ord_list) % modulus

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for i in range(size)]

    def add(self, value):
        hash_key = ord_sum_hash(value)
        self.table[hash_key].add(value)
        """print "Adding value:", value, ", hash key:", hash_key"""

    def __str__(self):
        output = ""
        for i in range(self.size):
            output += "Bucket " + str(i) + ": " + str(self.table[i]) + "\n"
        return output

        
class Node:
    def __init__(self, value):
        self.before = None
        self.after = None
        self.value = value

    def __str__(self):
        return str(self.value)

class LinkedList:
    """Defines an object that iterates through nodes."""
    def __init__(self, first = None):
        self.first = first
        self.last = first

    def add(self, element):
        new_node = Node(element)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.after = new_node
            new_node.before = self.last
            self.last = new_node
        return True

    def delete(self, element):
        if self.first == None:
            return False
        curr_node = self.first
        while curr_node.after != None:
            curr_node = curr_node.after
            if curr_node == element:
                curr_node.before.after = curr_node.after
                curr_node.after.before = curr_node.before
                return True
        return False

    def __str__(self):
        if self.first == None:
            return "Empty"
        curr_node = self.first
        output = "| "
        output += str(curr_node)
        while curr_node.after != None:
            curr_node = curr_node.after
            output += " --> " + str(curr_node)
        output += " |"
        return output


hash_table = HashTable(SIZE_OF_HASH_TABLE)
"""
hash_table.add("first node")
hash_table.add("testify!")
hash_table.add("the code is working, hurray!")
hash_table.add("if i add enough of these, there will be a collision!")
hash_table.add("moar text here")
hash_table.add("laser babies")
hash_table.add("last node")
hash_table.add("a few more nodes...")
hash_table.add("testeses")
hash_table.add("woohoo!")
"""
a_to_z_upper_range = range(65, 90)
a_to_z_lower_range = range(97, 122)
shuffled_letters = a_to_z_lower_range + a_to_z_upper_range
random.shuffle(shuffled_letters)
for i in shuffled_letters:
    hash_table.add(chr(i))

print hash_table

"""
first_node = Node('first node')
ll = LinkedList(first_node)
ll.add(Node('second node'))
"""

#print ll
