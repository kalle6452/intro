from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        #return hash(word) % 64
        hash = sum(ord(character) for character in repr(word))
        return hash
    # Doubles size of bucket list
    def rehash(self):
        self.buckets = [[] for i in range(16)]  # Placeholder code ==> to be replaced
        return self.buckets
    # Adds a word to set if not already added
    def add(self, word):
        n = self.get_hash(word)
        y = self.rehash()
        N = 16
        b = n % N
        current = self.buckets[b]
        for i in self.buckets:
            if i == word:
                return i
        else:
            current.append(word)
            return current, b

    # Returns a string representation of the set content
    def to_string(self):
        pass    # Placeholder code ==> to be replaced

    # Returns current number of elements in set
    def get_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns True if word in set, otherwise False
    def contains(self, word):
        pass    # Placeholder code ==> to be replaced

    # Returns current size of bucket list
    def bucket_list_size(self):
        pass    # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        pass    # Placeholder code ==> to be replaced

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass    # Placeholder code ==> to be replaced

    
    
    
    
    #from LinkedList1.py import *
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

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]
      
        #self.counter = 0
    # Computes hash value for a word (a string)
    
    
    # Vår kod
    def get_hash(self, word):
        #word1 = linked.LinkedList()
        hash = sum(ord(character) for character in repr(word))
        length = len(self.buckets)
        hashing = hash % length
        return hashing
    # Doubles size of bucket list
    def rehash(self):
        self.buckets = [[] for i in range(16)]  # Placeholder code ==> to be replaced
        return self.buckets

    # Adds a word to set if not already added
    # y är self.buckets
    # Sortera listan med sort
    def reset_counter(self):
        self.counter = 0
        return self.counter
    def inc_counter(self):
        self.counter += 1
        return self.counter

    def add(self, word):
        h = self.get_hash(word)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]
        current.append(word)
        found_key = True
        for i, r in enumerate(current):
            record_key, record_val = record_key
            if record_key == True:
                found_key == True
                break
        #self.inc_counter()
        return current
    
    
    
    def contains(self, word):
        h = self.get_hash(word)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]
        #print(current)
        #current.append(word)
        for word in current:
            if word not in current:
                current.append(word)
                boole = True
                return boole
            else:
                boole = False
                return boole
# self.buckets[1]
    # Returns a string representation of the set content
    def to_string(self):
        pass #return unique

    # Returns current number of elements in set
    def get_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns True if word in set, otherwise False
    
    # Returns current size of bucket list
    def bucket_list_size(self):
        pass    # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        pass    # Placeholder code ==> to be replaced

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        pass    # Placeholder code ==> to be replaced

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass    # Placeholder code ==> to be replaced

Påbörjad geeks:
    from dataclasses import dataclass
from typing import List
  
    # Create empty bucket list of given size
@dataclass
class HashSet:    
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    def get_hash(self, word):
        #word1 = linked.LinkedList()
        hash = sum(ord(character) for character in repr(word))
        length = len(self.buckets)
        hashing = hash % length
        return hashing
    # Insert values into hash map
    def add(self, word):
        
        # Get the index from the key
        # using hash function
        h = self.get_hash(word)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]   
  
        found_key = False
        for index, record in enumerate(current):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == word:
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            current[index] = (word, val)
        else:
            current.append((word, val))
  
    # Return searched value with specific key
    def get_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
  
    # Remove a value with specific key
    def delete_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
  
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
  


    
    
    
    
    
    
    
    
    
    
    
    
    
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
    def init(self):
        self.buckets = [[] for i in range(8)]
        self.size = 0
        
    def get_hash(self, word):
        hash = sum(ord(character) for character in repr(word))
        length = len(self.buckets)
        hashing = hash % length
        return hashing
    # Insert values into hash map
    def rehash(self):
        length = len(self.buckets)
        self.buckets = [[] for i in range(length*2)]  # Placeholder code ==> to be replaced
        print(f'length: {length}')
        return self.buckets

    def add(self, word):
        h = self.get_hash(word)
        N = len(self.buckets)
        b = h % N
        current = self.buckets[b]

        found_key = False
        for index, record in enumerate(current):
            #record_key = record
            
            # check if the bucket has same key as
            # the key to be inserted
            if record == word:
                found_key = True
                break
                #print(len(self.buckets))
                if self.size == len(self.buckets):
                    #print(self.size)
                    self.buckets.append(self.get_hash(self.buckets))
                
        
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            pass
            current[index] = (word)
        else:
            current.append(word)
            self.size += 1
        return 1
    def get_size(self):
        #self.buckets = [[] for i in range(len(self.buckets))*2]
        #s = 1
        #return self.buckets
        pass
    def contains(self, word):
        pass 
    def bucket_list_size(self):
        pass

    # Return searched value with specific key
    def get_val(self, word):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(word) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == word:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
  
    # Remove a value with specific key
    def remove(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    def to_string(self):
        pass
        #return "".join(str(item) for item in self.hash_table)
    # To print the items of hash map
  
    def max_bucket_size(self):
        pass
    def zero_bucket_ratio(self):
        pass 

  
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

import HashSet as hset

# Initialize word set
words = hset.HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set. Notice: a) contains duplicate names,
# b) more than eight names ==> will trigger rehash
names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]
for name in names:
    words.add(name)
    print(words.add(name))

print("\nto_string():", words.to_string())  # { Adam David Amer Ceve Owen Ella Jonas Morgan Fredrik Zoe Fred Albin Ola Simon }
print("get_size():", words.get_size())             # 14
print("contains(Fred):", words.contains("Fred"))   # True
print("contains(Bob):", words.contains("Bob"))     # False

# Hash specific data
mx = words.max_bucket_size()
print("\nmax bucket:", mx)                # 2
buckets = words.bucket_list_size()
print("bucket list size:", buckets)     # 16
zero_buckets_ratio = words.zero_bucket_ratio()
#print("zero bucket ratio:", round(zero_buckets_ratio, 2))  # 0.38

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
#for s in delete:
    #words.remove(s)
print("\nget_size:", words.get_size())   # 10
print("to_string():", words.to_string())   # { David Amer Owen Ella Morgan Fredrik Zoe Fred Albin Simon }
