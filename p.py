class HashTable:
    def __init__(self):
        self.key = ""
        self.value = 0
        self.isEmpty = True
        self.next = None

class Contacts:
    def __init__(self):
        self.num = 0
        self.phoneBook = None

    def ins(self):
        def hashing(name, n):
            # Calculating hash value
            sum = 0
            for char in name:
                sum += ord(char)
            return sum % n

        self.num = int(input("Enter number of entries: "))
        self.phoneBook = [HashTable() for _ in range(self.num)]

        print("Enter name and phone number respectively:")
        for _ in range(self.num):
            name, phoneNumber = input().split()
            phoneNumber = int(phoneNumber)
            index = hashing(name, self.num)

            if self.phoneBook[index].isEmpty:
                # If the slot is empty (no collision)
                self.phoneBook[index].key = name
                self.phoneBook[index].value = phoneNumber
                self.phoneBook[index].isEmpty = False
                self.phoneBook[index].next = None
            else:
                # In case of collision
                temp = self.phoneBook[index]
                while temp.next:
                    temp = temp.next

                newEntry = HashTable()
                newEntry.key = name
                newEntry.value = phoneNumber
                newEntry.isEmpty = False
                newEntry.next = None

                temp.next = newEntry

    def searchContact(self, name):
        def hashing(name, n):
            # Calculating hash value
            sum = 0
            for char in name:
                sum += ord(char)
            return sum % n

        check = hashing(name, self.num)

        if not self.phoneBook[check].next:
            # If there is no collision seen in the current block
            if self.phoneBook[check].key == name:
                print("Name:", self.phoneBook[check].key)
                print("Phone number:", self.phoneBook[check].value)
            else:
                print("Not found")
        else:
            # If collision is seen in the current block
            temp = self.phoneBook[check]
            while temp:
                if temp.key == name:
                    print("Name:", temp.key)
                    print("Phone number:", temp.value)
                    break
                else:
                    temp = temp.next
            if not temp:
                print("Not found")

    def __del__(self):
        del self.phoneBook

def main():
    d1 = Contacts()
    d1.ins()

    n = int(input("Enter number of names you want to search: "))
    print("Enter names:\n")
    for _ in range(n):
        name = input()
        d1.searchContact(name)
        print()

if __name__ == "__main__":
    main()

