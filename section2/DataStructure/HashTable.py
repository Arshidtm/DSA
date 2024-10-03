class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size  # Initialize the size of the hash table
        self.hashList = [None] * self.size  # Create a list to hold the buckets

    def _hash(self, key):
        # Compute a hash value for the given key
        return hash(key) % self.size  # Return the index in the hash table

    def __setitem__(self, key, value):
        ind = self._hash(key)  # Get the index for the key

        if not self.hashList[ind]:
            # If the bucket is empty, create a new list
            self.hashList[ind] = [[key, value]]
        else:
            # Otherwise, check if the key already exists
            sublist = self.hashList[ind]
            for pair in sublist:
                if pair[0] == key:
                    pair[1] = value  # Update the value if the key is found
                    return
            # If the key is not found, append the new key-value pair
            self.hashList[ind].append([key, value])

    def __getitem__(self, key):
        ind = self._hash(key)  # Get the index for the key
        sub = self.hashList[ind]
        if not sub:
            return None  # Return None if the bucket is empty
        else:
            # Search for the key in the bucket
            for pair in sub:
                if pair[0] == key:
                    return pair[1]  # Return the value if the key is found
        raise KeyError(f"Key {key} not found")  # Raise error if key is not found

    def __delitem__(self, key):
        ind = self._hash(key)  # Get the index for the key

        if self.hashList[ind]:
            # If the bucket is not empty, search for the key
            for index, pair in enumerate(self.hashList[ind]):
                if pair[0] == key:
                    del self.hashList[ind][index]  # Delete the key-value pair
                    return
        raise KeyError(f"{key} not found")  # Raise error if key is not found
    
    def keys(self):
        # Return a list of all keys in the hash table
        key_list = []
        for sublist in self.hashList:
            if sublist:
                for pair in sublist:
                    key_list.append(pair[0])
        return key_list

    def values(self):
        # Return a list of all values in the hash table
        value_list = []
        for sublist in self.hashList:
            if sublist:
                for pair in sublist:
                    value_list.append(pair[1])
        return value_list

# Example usage of HashTable class
hashLis = HashTable()
# hashLis['Name'] = 'Arshid'
# hashLis['Age'] = 23
print(hashLis.keys())  # Output: ['Name', 'Age']
print(hashLis.values())  # Output: ['Arshid', 23]
# print('before delete')
# print(hashLis.hashList)
# del hashLis['Age']
# print('After delete')
# print(hashLis.hashList)

