#Sets key-value pair and pointer for next node in hash table
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Creates self adjusting hash table
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    # Map values to key
    def _hash(self, key):
        return hash(key) % self.capacity

# Inserts data into the hash table
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Package(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

# Search function
    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

class Package:
    def __init__(self, package_id, address, deadline, city, state, zip_code, pk_weight, status, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.deadline = deadline
        self.zip_code = zip_code
        self.pk_weight = pk_weight
        self.status = status
        self.special_notes = special_notes

class Truck:
    def __init__(self, truck):
        self.truck = truck

