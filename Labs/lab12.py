from ChainingHashTableMap import *
from DoublyLinkedList import *


def most_frequent(lst):
    freq = ChainingHashTableMap()
    common = lst[0]
    for i in lst:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
        if freq[i] > freq[common]:
            common = i
    return common


def first_unique(lst):
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    for i in freq.keys():
        if freq[i] == 1:
            return i
    return None


def two_sum(lst, target):
    hash_table = ChainingHashTableMap()
    for i in range(len(lst)):
        hash_table[lst[i]] = i
    for i in range(len(lst)):
        dif = target - lst[i]
        if dif in hash_table:
            if i != hash_table[dif]:
                return i, hash_table[dif]
    return None, None


class PlayList:
    def __init__(self):
        self.data = ChainingHashTableMap()
        self.order = DoublyLinkedList()

    def add_song(self, new_song_name):
        self.order.add_last(new_song_name)
        self.data[new_song_name] = self.order.trailer.prev

    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.data:
            raise KeyError("Song doesn't exist in playlist")
        song_node = self.data[song_name]
        self.order.add_after(song_node, new_song_name)
        self.data[new_song_name] = song_node.next

    def play_song(self, song_name):
        if song_name not in self.data:
            raise KeyError("Song doesn't exist in playlist")
        print("Playing " + song_name)

    def play_list(self):
        current = self.order.header.next
        while current != self.order.trailer:
            print('Playing ' + current.data)
            current = current.next


class ChainingHashTableSet:
    def __init__(self, N=64):
        self.N = N
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)
    def rehash(self, new_size):
        #modify this to support the set ADT
        old = [key for key in self]
        self.__init__(new_size)
        for key in old:
            self.add(key)
    def __iter__(self):
        for i in self.table:
            for key in i:
                yield key
    def __contains__(self, key):
        #imodify this to support the set ADT
        for i in self:
            if i == key:
                return True
        return False
    def add(self, key): #replace __setitem__
        """   Adds a key to the set. If the key already exists, do
        nothing. You may want to refer to the __setitem__
        implementation of the ChainingHashTableMap. """
        i = self.h(key)
        buckets = self.table[i]
        for e in buckets:
            if e == key:
                return
        buckets.add_last(key)
        self.n += 1
        if self.n > self.N:
            self.rehash(2*self.N)
    def remove(self, key): #replace __delitem__
        """   Removes a key from the set. If the key doesn't exist, raise
        a KeyError. You may want to refer to the __delitem__
        implementation of the ChainingHashTableMap  """
        i = self.h(key)
        buckets = self.table[i]
        current = buckets.header.next
        has_key = False
        while current is not buckets.trailer:
            if current.data == key:
                buckets.delete_node(current)
                self.n -= 1
                has_key = True
                break
        if not has_key:
            raise KeyError("Key doesn't exist")
        if self.n < self.N // 4:
            self.rehash(self.N //2)
def print_hash_table(hset):
    #modify this to support the set A
    print('{' + ', '.join([str(key) for key in hset]) + '}')


def main():
    my_lst1 = [5, 9, 2, 9, 0, 5, 9, 7]
    print(most_frequent(my_lst1))
    print(first_unique(my_lst1))
    my_lst2 = [-2, 11, 15, 21, 20, 17]
    print(two_sum(my_lst2, 22))

    p1 = PlayList()
    p1.add_song("Jana Gana Mana")
    p1.add_song("Kimi Ga Yo")
    p1.add_song("The Star-Spangled Banner")
    p1.add_song("March of the Volunteers")
    p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
    p1.add_song_after("Kimi Ga Yo", "Aegukga")
    p1.add_song("Arise, O Compatriots")
    p1.add_song("Chant de Ralliement")
    p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
    p1.add_song_after("Jana Gana Mana", "God Save The Queen")
    p1.play_song("The Star-Spangled Banner")
    p1.play_song("Jana Gana Mana")
    p1.play_list()

    set1 = ChainingHashTableSet()
    set1.add(1)
    set1.add(2)
    set1.add(3)
    set1.add("apple")
    set1.add("banana")

    set2 = ChainingHashTableSet()
    set2.add(1)
    set2.add(3)
    set2.add("orange")

    print_hash_table(set1)
    print_hash_table(set2)


main()
