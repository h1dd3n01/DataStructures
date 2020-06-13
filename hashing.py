class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        hash_item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                h = (h + 1) % self.size
                break
        if self.slots[h] is None:
            self.count += 1
            print(h)
            self.slots[h] = hash_item

    def get(self, key):
        h = self._hash(key)
        # print(h)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                print('Found {} at index {}'.format(self.slots[h], h))
                return self.slots[h].value
            h = (h + 1) % self.size
            # print(h)
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        self.get(item)


if __name__ == '__main__':
    c = HashTable()
    c.put('name', 'john')
    c.put('name', 'Joseph')
    c.put('last_name', 'Josy')
    # for key in ('name', 'last_name'):
    #     ht = c.get(key)
    #     print(ht)
    # print(c.get('name'))
    print(c.get('name'))
    # for i in c.slots:
    #     print(i)
