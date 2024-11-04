import csv

# Creates hash table
class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts data into the hash table
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates key if already in the bucket
        for item in bucket_list:
            if item[0] == key:
                item[1] = value
                return True

        bucket_list.append([key,value])
        return True

    # Looks for item with matching key
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == key:
                return item[1]
            return None

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

        #def __str__(self):
            #return f"ID: {self.package_id}, Address: {self.address}, {self.city}, {self.state}, {self.zip_code}, Deadline: {self.deadline}, Weight: {self.pk_weight}, Status: {self.status}"

class Truck:
    def __init__(self, truck):
        self.truck = truck


def loadPackageData(filename):
    with open(filename) as wgupsPackageFile:
        packageData = csv.reader(wgupsPackageFile, delimiter=',')
        next(packageData)
        for packages in packageData:
            pID = int(packages[0])
            pAddress = packages[1]
            pCity = packages[2]
            pState = packages[3]
            pZipcode = int(packages[4])
            pDeadline = packages[5]
            pWeight = int(packages[6])
            pStatus = packages[7]

            # Package object
            packages = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            # Insert into the hash table
            myHashTable.insert(pID, packages)


# Hash Table instance
myHashTable = HashTable(40)

# Load packages into Hash Table
loadPackageData('WGUPSPackageFile.csv')

print('Delivery Information:')

# Remove after debugging
total = 0

for i in range (1, len(myHashTable.table)+1):
    package = myHashTable.lookup(i)
    if package is not None:

        print("Package Details: {}".format(package))

