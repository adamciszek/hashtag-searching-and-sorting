from T2_linked_list import *
from T2_bst import *
from T2_hash_table import *
import random



#=========================================================================
class Tweet(object):
    def __init__(self, text, hashtags):
        self.__text = text
        self.__hashtags = hashtags
    def get_text(self):
        return self.__text
    def get_hashtags(self):
        return self.__hashtags
    def __str__(self):
        return "{}: {}".format(self.__text, self.__hashtags)




#=========================================================================
class Hashtag_Record(object):
    def __init__(self, tag):
        self.__tag = tag
        self.__tweets = []
    def get_tag(self):
        return self.__tag
    def get_tweets(self):
        return self.__tweets
    def add_tweet(self, tweet):
        self.__tweets.append(tweet)
    def __hash__(self):
        return hash(self.__tag)
    def __repr__(self):
        return "{} ({} tweets)".format(self.__tag, len(self.__tweets))
    def __eq__(self, other):
        return other != None and self.__tag == other.__tag
    def __lt__(self, other):
        return other != None and self.__tag < other.__tag
    def __gt__(self, other):
        return other != None and self.__tag > other.__tag



#=========================================================================
class Hashtag_List(list):

    def sorted_by_num_tweets(self):
        '''
        H.sorted_by_num_tweets() --> Hashtag_List
        Returns a copy of this Hashtag_List, in order from most Tweets to least.
        '''
        
        return self.__quick_sort_helper(self)
        
    def __quick_sort_helper(self, values):
        '''
        This is a helper method for 'sorted_by_num_tweets()' which consists of the quick sort algorithm
        This sorts the tweets in order from most tweets to least
        '''
        sorted_tweets = Hashtag_List()
        
        if len(values) > 0:
        
            pivot = [values[-1]]    #this pivot is used to compare other values and decide whether they are smaller or larger
            left = []
            right = []
            
            for pos in range(0, len(values)-1):
                
                if len(values[pos].get_tweets()) > len(pivot[0].get_tweets()):
                    #larger terms are added to 'smaller' as smaller will be the left side of the pivot and it shoould be sorted by most tweets first
                    left.append(values[pos])
                    
                elif len(values[pos].get_tweets()) < len(pivot[0].get_tweets()):
                    #smaller terms are added to 'greater' as greater will be the right side of the pivot and it should be sorted by most tweets to least
                    right.append(values[pos])
                    
                else:
                    pivot.append(values[pos])
                    
            sorted_tweets.extend(self.__quick_sort_helper(left))
            sorted_tweets.extend(pivot)
            sorted_tweets.extend(self.__quick_sort_helper(right))
        
        return sorted_tweets
        


#=========================================================================
class Hashtag_LinkedList(LinkedList):

    def as_list(self):
        '''
        H.as_list() --> Hashtag_List
        Return a Hashtag_List containing all items in this structure, 
        in increasing order of hashtag.
        '''
        ht_LL_list = Hashtag_List()
        current = self.get_first()
        
        while current != None:
            ht_LL_list.append(current.get_data())
            current = current.get_next()
            
        ht_LL_list.sort()
        
        return ht_LL_list


   
    def get_top_hashtag(self):
        '''
        H.get_top_hashtag() --> Hashtag_Record
        Return the Hashtag_Record (or one of) that has the most Tweets,
        or None if the structure is empty.
        '''
        current = self.get_first()
        
        if current != None:
            largest = current.get_data()
            
            while current.get_next() != None:
                
                if len(current.get_data().get_tweets()) > len(largest.get_tweets()):
                    largest = current.get_data()
                current = current.get_next()
                
            return largest
        
        
        else:
            return None
            



    def reverse(self):
        '''
        H.reverse() --> None
        Reverse the order of all items in this Hashtag_LinkedList.
        '''
        hashtag  = self.get_first()
        reversed_LL = Hashtag_LinkedList()
        
        for i in range(0, super().size()):
            reversed_LL.insert(hashtag.get_data())
            hashtag = hashtag.get_next()
        
        self.set_first(reversed_LL.get_first())



    def get_nth(self, n):
        '''
        H.get_nth(int) --> Hashtag_Record
        Return the Hashtag_Record in the n-th position in this list,
        or None if there is no n-th position.
        '''
        
        pos = 0
        current = self.get_first()   
        
        while current != None and pos != n:
            pos += 1
            current = current.get_next()
            
          
        #must determine that the pos i finished in the while loop was the position that was asked for.  If not, i must return None  
        if pos == n:
            return current.get_data()
        
        else:
            return None
    


    def size(self):
        '''
        H.size() --> int
        Return the size of this Hashtag_LinkedList.
        Due to recursive implementation, may cause StackOverflowError on large lists.
        '''
        return self.__size_helper(self.get_first())
  
    def __size_helper(self, node):
        '''
        This is a helper method for the size() method
        Returns 0 if the node is None, or returns 1 and the size of the rest of the list
        '''
        
        if node == None:
            return 0
        
        else:
            return 1 + self.__size_helper(node.get_next())



#=========================================================================
class Hashtag_BSTree(BSTree):

    def as_list(self):
        '''
        H.as_list() --> Hashtag_List
        Return a Hashtag_List containing all items in this structure, 
        in increasing order of hashtag.
        '''
        ht_BS_list = self.__as_list_helper(self.get_root())
        return ht_BS_list
    
    def __as_list_helper(self, subroot):
        '''
        This is a helper method for the as_list method for a binary search tree
        returns a list of all the values in the tree in order (from left to right)
        '''
        ht_BS_list = Hashtag_List()
        
        if subroot != None:
            
            left = self.__as_list_helper(subroot.get_left())
            ht_BS_list.extend(left)
            
            ht_BS_list.append(subroot.get_data())
            
            right = self.__as_list_helper(subroot.get_right())
            ht_BS_list.extend(right)
            
        return ht_BS_list



    def get_top_hashtag(self):
        '''
        H.get_top_hashtag() --> Hashtag_Record
        Return the Hashtag_Record (or one of) that has the most Tweets,
        or None if the structure is empty.
        ''' 
        if self.get_root() != None:
            return self.__top_hashtag_helper(self.get_root()).get_data()
        else:
            return None
    
    def __top_hashtag_helper(self, node):
        '''
        This is a helper method for get_top_hashtag() method
        This loops through each value in the tree and updates the largest value when the current value is greater then the previous largest value
        '''
        largest = node
        
        if node.get_left() != None:
            left = self.__top_hashtag_helper(node.get_left())
            
            if len(left.get_data().get_tweets()) > len(largest.get_data().get_tweets()):
                largest = left  
                
        if node.get_right() != None:
            right = self.__top_hashtag_helper(node.get_right())
            
            if len(right.get_data().get_tweets()) > len(largest.get_data().get_tweets()):
                largest = right              
                  
        
        return largest
        

    def balance(self):
        '''
        H.balance() --> None
        Balances the tree to minimize the depth, and make each level as full
        as possible.
        '''
        values = self.as_list()
        
        #after getting the list of values in the original list, I make the tree empty and insert values in order to fill the tree symetrically
        self.empty()
        self.__balance_helper(values)
        
    def __balance_helper(self, values):
        '''
        This is a helper method for the balance() method
        This method makes a list of the values, creates an empty list, and inserts the middle value of each list and sublist        
        '''
        if len(values) > 0:
            
            middle = len(values)//2
            
            self.insert(values[middle])
            self.__balance_helper(values[0:middle])
            self.__balance_helper(values[middle+1:])



    def get_leaves(self):
        '''
        H.get_leaves() --> Hashtag_List
        Returns a Hashtag_List of all the Hashtable_Records that are in the leaves.
        '''
        if self.get_root() != None:
            return self.__get_leaves_helper(self.get_root())
        else:
            return Hashtag_List()
           
    def __get_leaves_helper(self, node):
        '''
        This is a helper method for the get_leaves() method
        This returns a Hashtag_List() with all the leaves.  If there is no node after this current node, it appends it into this Hashtag_List()
        '''
        
        all_leaves = Hashtag_List()
        
        if node.get_left() == None and node.get_right() == None:
            #if there are no nodes following this node, it is added to the Hashtag_List() 
            all_leaves.append(node)
            
        else:
            
            if node.get_left() != None:
                left = self.__get_leaves_helper(node.get_left())
                all_leaves.extend(left)
                
            if node.get_right() != None:
                right = self.__get_leaves_helper(node.get_right())
                all_leaves.extend(right)
            
        return all_leaves
            



    def count_one_child(self):
        '''
        H.count_one_child() --> int
        Returns the number of nodes that have exactly one child.
        The larger this number is, the (potentially) more unbalanced it is.
        '''        
        return self.__one_child_helper(self.get_root())
    
    def __one_child_helper(self, node):
        '''
        This is a helper method for the coun_one_child() method
        This will return a number of one childs by having a counter...If there is only one child, it adds one to that counter and continues to go through the list
        '''
        
        num_one_childs = 0
        
        if node == None:
            return num_one_childs
        
        elif (node.get_left() == None and node.get_right() != None) or (node.get_left() != None and node.get_right() == None):
            #if the node has one child it adds one to the counter
            num_one_childs += 1
           
        #these if statements figure out if there is a child, and if there is, it checks if that node has one child 
        if node.get_left() != None:
            num_one_childs += self.__one_child_helper(node.get_left())
                
        if node.get_right() != None:
            num_one_childs += self.__one_child_helper(node.get_right())
                
        return num_one_childs




#=========================================================================
class Hashtag_HashTable(HashTable):
    
    def __init__(self, size, scalable=False):
        '''
        __init__(int, bool)
        Construct a custom HashTable, with 'size' buckets.
        When scalable is True, this table will double in size when the
        load factor exceeds 1.0 from an insert.
        '''           
        HashTable.__init__(self, size)  #construct parent
        buckets = []                    #temporary holder
        for i in range(size):
            #these buckets are Hashtag_LinkedLists
            buckets.append(Hashtag_LinkedList())
        self.set_empty_buckets(buckets)       #update parent property
        self.__scalable = scalable


    def as_list(self):
        '''
        H.as_list() --> Hashtag_List
        Return a Hashtag_List containing all items in this structure, 
        in increasing order of hashtag.
        '''
        hs_HT_list = Hashtag_List()
        for bucket in self.get_buckets():
            
            current = bucket.get_first()
            while current != None:
                hs_HT_list.append(current.get_data())
                current = current.get_next()
                
        hs_HT_list.sort()
        return hs_HT_list
    
    
    
    def get_top_hashtag(self):
        '''
        H.get_top_hashtag() --> Hashtag_Record
        Return the Hashtag_Record (or one of) that has the most Tweets,
        or None if the structure is empty.
        ''' 
        buckets = self.get_buckets()
        if len(buckets) != 0:
        
            largest = buckets[random.randrange(0, len(buckets))].get_first()    
            #largest bucket must be assigned a value, therefore, a random bucket is chosen (hence the 'randrange' used)
            
            while largest == None:
                largest = buckets[random.randrange(0, len(buckets))].get_first()            
            
            for bucket in buckets:
                
                current = bucket.get_first()
                while current != None:
                    
                    if len(current.get_data().get_tweets()) > len(largest.get_data().get_tweets()):
                        largest = current
                        
                    current = current.get_next()
                    
            return largest.get_data() 
        
        
        else:
            return None
    
    
    
    def get_largest_bucket(self):
        '''
        H.get_largest_bucket() --> Hashtag_LinkedList
        Return the largest bucket in this table, or None if the structure is empty.
        ''' 

        buckets = self.get_buckets()
        
        if len(buckets) != 0:
            
            largest = buckets[0]
            
            for bucket in self.get_buckets():
                
                if bucket.size() > largest.size():
                    #if the current bucket size is larger then the previous bucket size then largest bucket will update
                    largest = bucket
                    
            return largest    
        
        else:
            return None
            

    

    def get_percent_above_load_factor(self):
        '''
        H.get_percent_above_load_factor() --> float
        Return the decimal percentage of buckets whose size is more
        than the load factor (in other words, more than the average).
        ''' 
        total = 0
        load_factor = self.load_factor()
        
        for bucket in self.get_buckets():
            
            if bucket.size() > load_factor:
                total += 1  #counter for total buckets above the load factor
        
        return "{:.2f}".format(total/len(self.get_buckets()))




    def insert(self, ht_record):
        '''
        H.insert(Hashtag_Record) --> None
        Insert the given record in this table.  Scale the table size if necessary.
        ''' 
        if self.__scalable == True and self.load_factor() > 1:  #must check if table is scalable and if the load factor allows it to be scaled
            
            hashtags = self.as_list()
            buckets = []    
            
            #bucket size is doubled if the table is scalable
            for i in range((len(self.get_buckets()))*2):    #in the list of buckets, each position must have a linked_list()
                buckets.append(Hashtag_LinkedList())
                
            self.set_empty_buckets(buckets) #must reset the bucket list to the new Hashtag_List() that has empty buckets    
              
            #after creating an empty hashtable, we re-insert all the values  
            super().insert(ht_record)   #inserts the term that was given
            
            for hashtag in hashtags:    #this loop inserts all the previous values
                super().insert(hashtag)
            
        else:
            super().insert(ht_record)
