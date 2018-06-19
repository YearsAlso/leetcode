import random

class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
    
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            return False
        else:
            self.list.append(val)
            return True
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            self.list.remove(val)
            return True
        return False
    
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.list)==0:
            return None
        print(random.randint(0,len(self.list)))
        return self.list[random.randint(0,len(self.list)-1)]
    
obj = RandomizedSet()
param = []
param.append(obj.insert(1))
param.append(obj.remove(2))
param.append(obj.insert(2))
param.append(obj.getRandom())
param.append(obj.remove(1))
param.append(obj.insert(2))
param.append(obj.getRandom())
print(param)