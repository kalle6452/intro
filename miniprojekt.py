from dataclasses import dataclass
from operator import contains
from typing import List
import pdb
# Håll koll på vad Linus har gjort, var beredd på att svara på frågor
# om bst.
from dataclasses import dataclass
from typing import Any

@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0
    counter: int = 0
    def init(self):
        self.buckets = [[] for i in range(8)]
        self.size = 0
        self.counter = 0
    def get_hash(self, word):
        hash = sum(ord(character) for character in repr(word))
        length = len(self.buckets)
        hashing = hash % length
        return hashing
    # Insert values into hash map
    def rehash(self):
        temp = self.buckets
        length = len(self.buckets)
        self.buckets = [[] for i in range(length*2)]  # Placeholder code ==> to be replaced
        for i in temp:
            self.add(i)
        print(f'length: {length}')
        return self.buckets

    def add(self, element):
        h = self.get_hash(element)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]
        #current.append(element)
        found_key = False
        for index, record in enumerate(current):
            record_key = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == element:
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            current[index] = (element)
        else:
            current.append((element))
            self.size += 1
            if self.size == len(self.buckets):
                self.counter += 1
                print(f'count: {self.counter}')
                self.rehash()
        return self.buckets
    def contains(self, element):
        h = self.get_hash(element)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]
        found_key = False
        for index, record in enumerate(current):
            record_key = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == element:
                print(element)
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            return False
        else:
            return True
    def get_size(self):
        return int(self.size/2)
        #self.buckets = [[] for i in range(len(self.buckets))*2]
        #s = 1
        #return self.buckets
        pass
    
    def bucket_list_size(self):
        return self.size
  
    # Remove a value with specific key
    def remove(self, element):
        
        h = self.get_hash(element)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]
        found_key = False
        for index, record in enumerate(current):
            record_key = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == element:
                print(element)
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            return False
        else:
            return True
    def to_string(self):
        return self.buckets
        #return "".join(str(item) for item in self.hash_table)
    # To print the items of hash map
  
    def max_bucket_size(self):
        return 't'
    def zero_bucket_ratio(self):
        pass 
    def get_val(self, element):
        h = self.get_hash(element)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]  
        found_key = False
        if element in current:
            return True
        else:
            return current
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        
  
# insert some values


#hash_table.set_val('gfg@example.com')
#print(hash_table.to_string())
'''print() 
  
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
  
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
  
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)'''
