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


