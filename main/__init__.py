import csv

# Creates hash table
class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = [None] * initial_capacity
        #for i in range(initial_capacity):
            #self.table.append([])

    # Maps values to key
    def hash_function(self, key):
        return hash(key) % self.size

    # Inserts data into the hash table
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates key if already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Looks for item with matching key
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
            return None


def load_package_data(filename):
    with open(filename) as wgupsPackageFile:
        packageData = csv.reader(wgupsPackageFile, delimiter=',')
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = int(package[4])
            pDeadline = package[5]
            pWeight = int(package[6])
            pStatus = package[7]

            # Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            # Insert into the hash table
            myHashTable.insert(pID, p)


# Hash Table instance
myHashTable = HashTable()


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, pk_weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.pk_weight = pk_weight
        self.status = status

        def __str__(self):
            return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zip_code, self.deadline, self.pk_weight,
            self.status)


class Truck:
    def __init__(self, truck):
        self.truck = truck


# Load packages into Hash Table
load_package_data('WGUPSPackageFile.csv')

print('Packages:')

for i in range(len(myHashTable.table)):
    package = myHashTable.lookup(myHashTable.table[i])
    if package is not None:
        print('Package ID: {}'.format(package))

