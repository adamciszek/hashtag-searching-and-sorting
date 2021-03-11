import unittest
from random import *
from hashtag_structures import *

class Hashtag_Linkedlist_test(unittest.TestCase):
    #testing size() method
    
    def test_size_zero(self):
        #empty linked list
        
        expected = 0
        actual = Hashtag_LinkedList().size()    #getting size() of an empty list
        self.assertEqual(expected, actual)
        
    def test_size_one(self):
        #linked list with a single value (border case)
        expected = 1
        
        HTLL = Hashtag_LinkedList()
        HTLL.insert(randrange(0,10))    #one value is inserted into the linked list
        
        actual = HTLL.size()
        self.assertEqual(expected, actual)
        
    def test_size_double(self):
        #linked list with a two values (border case)
        expected = 2
        
        HTLL = Hashtag_LinkedList()
        for i in range(0,2):    #this for loop inserts 2 values into the linked list
            HTLL.insert(randrange(0,10))    #a random number from 1-10 (excluding 10) is inserted
        
        actual = HTLL.size()
        self.assertEqual(expected, actual)   
        
    def test_size_many(self):
        #linked list with many values(no border cases to worry about)
        expected = 10
        
        HTLL = Hashtag_LinkedList()
        for i in range(0,10):   #ten valyes are inserted into the list
            HTLL.insert(randrange(0,10))
        
        actual = HTLL.size()
        self.assertEqual(expected, actual)        
    
    
class Hashtag_BSTree_test(unittest.TestCase):
    #testing count_one_child() method
    
    def test_count_one_child_empty(self):
        #tests when the tree is empty
        expected = 0
        
        HTBS = Hashtag_BSTree() #empty tree is created
        
        actual = HTBS.count_one_child()
        self.assertEqual(expected, actual)
        
    def test_count_one_child_root(self):
        #tests when the tree only has a root/head
        expected = 0
        
        HTBS = Hashtag_BSTree()
        HTBS.insert(randrange(0,10))    #one value is in the tree (this is the root/head)
        
        actual = HTBS.count_one_child()
        self.assertEqual(expected, actual)
        
    def test_count_one_child_single(self):
        #tests when the tree has one child when there is only a root and subroot
        expected = 1
        
        HTBS = Hashtag_BSTree()
        for i in range(0,2):    #this loop inserts 2 values into the tree (therefore it will make a parent with one child)
            HTBS.insert(randrange(0,10))    
        
        actual = HTBS.count_one_child()
        self.assertEqual(expected, actual)
        
    def test_count_one_child_double(self):
        #test when tree has 2 subroots
        expected = 0
        
        HTBS = Hashtag_BSTree()
        HTBS.insert(5)
        HTBS.insert(1)
        HTBS.insert(10) #this is a tree with a head, and 2 subroots, therefore shouldm't be any one childs
        
        actual = HTBS.count_one_child()
        self.assertEqual(expected, actual)   

    def test_count_one_child_many(self):
        #tests when tree has multiple single child
        expected = 5
        
        HTBS = Hashtag_BSTree()
        HTBS.insert(10)
        HTBS.insert(7)
        HTBS.insert(13)        
        HTBS.insert(4)
        HTBS.insert(12)
        HTBS.insert(15)
        HTBS.insert(2)
        HTBS.insert(5)
        HTBS.insert(11)
        HTBS.insert(18)
        HTBS.insert(1)
        HTBS.insert(6)      #this is a large tree specifically made to have 5 'parents with one child' randomly placed in the tree
        
        actual = HTBS.count_one_child()
        self.assertEqual(expected, actual)  
    
    
unittest.main()