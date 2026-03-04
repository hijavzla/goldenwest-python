# Implement an Array data structure as a simplified type of list. 

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0                # No items in array initially

   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items
   
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds
      
   def insert(self, item):             # Insert item at end
      self.__a[self.__nItems] = item   # Item goes at current end
      self.__nItems += 1               # Increment number of items

   def find(self, item):               # Find index for item
      for j in range(self.__nItems):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.__nItems):   # of an item
         if self.__a[j] == item:       # Found item
            self.__nItems -= 1         # One fewer at end
            for k in range(j, self.__nItems):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item   

   def traverse(self, function=print): # Traverse all items
      for j in range(self.__nItems):   # and apply a function
         function(self.__a[j])
   
   def removeDupes(self):                 # Removes dupes from self list by returning new list without dupes 
      newList = []                        # Create new list         
      for i in range(self.__len__()):     # Scan each item in self list 
         if self.get(i) not in newList: # if item from self list not found in newList, append it to newList
           newList = newList + [self.get(i)]
      newArray = Array(len(newList))                 # create new array
      newArray.traverse()                 # print newArray without any items 
      for j in range(len(newList)):       # for j in newList, add item to newArray 
         newArray.insert(newList[j])      # insert value into the newArray
      newArray.traverse()                 # traverse the new array
      return newArray                     # return the newArray without dupes

   def median(self):                      # The method should return the median value in the array

      return 1 

