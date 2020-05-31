# python3

from collections import namedtuple

Contact = namedtuple('Contact', ['name','number'])


class HashTable:
    def __init__(self):
        self.a = 10
        self.b = 10
        self.p = 100003
        self.m = 1000
        self.array = [[] for i in range(self.m)]
    def add(self, query):
        h = self._hashFunction(query.number)
        for item in self.array[h]:
            if item.number == query.number:
                item.name = query.name
                return  
        self.array[h].append(Contact(query.name, query.number))
    def delete(self, query):
        h = self._hashFunction(query.number) 
        for idx, item in enumerate(self.array[h]):
            if item.number == query.number:
                self.array[h].pop(idx)
                return
    def find(self, query):
        h = self._hashFunction(query.number)
        for item in self.array[h]:
            if item.number == query.number:
                return item.name
        return "not found"
    def _hashFunction(self, number):
        return ((self.a*number + self.b) % self.p) % self.m


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    hashTable = HashTable()
    for cur_query in queries:
        if cur_query.type == 'add':
            hashTable.add(cur_query)
        elif cur_query.type == 'del':
            hashTable.delete(cur_query)
        else:
            result.append(hashTable.find(cur_query))
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

