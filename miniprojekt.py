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

