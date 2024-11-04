# Jearad Percy
#C950 Task 2
# Student ID: 011359908
import csv

# Creates hash table
class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts data into the hash table
    def insert(self, package_id, package):
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates key if already in the bucket
        for item in bucket_list:
            if item[0] == package_id:
                item[1] = package
                return True

        bucket_list.append([package_id,package])
        return True

    # Looks for item with matching key
    def lookup(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == package_id:
                return item[1]
            return None

class Package:
    statuses = ["At Hub", "In Transit", "Delivered"]

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

# Address list initialization
addressData = []

# Read address csv and loads into list
def loadAddressData(filename):
    with open(filename, 'r') as addressDataFile:
        address = csv.reader(addressDataFile, delimiter=',')
        next(address)

        for row in address:
            addressData.append(row)

# Read distance csv and loads into list
datafile = open ('WGUPSDistanceTable.csv', 'r')
distance = csv.reader(datafile, delimiter=',')
next(distance)
# Initializes 2D list for distances
distanceData = []
for row in distance:
    distanceData.append(row)

loadAddressData('Address.csv')
#print(addressData)

# Hash Table instance
myHashTable = HashTable(40)

# Load packages into Hash Table
loadPackageData('WGUPSPackageFile.csv')

print('Delivery Information:')
for i in range (1, len(myHashTable.table)+1):
    package = myHashTable.lookup(i)
    if package is not None:

        print("Package Details: {}".format(package))