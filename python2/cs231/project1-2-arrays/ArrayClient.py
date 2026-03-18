import Array
maxSize = 10                    # Max size of the array
arr = Array.Array(maxSize)      # Create an array object
   
arr.insert(77)                  # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("Test case with array = [9, 8, 9]")
newArr = Array.Array(3)
newArr.insert(9)
newArr.insert(8)
newArr.insert(9)
newArr.traverse()
newArrWithoutDupes = newArr.removeDupes()

print("Another test case with array = []")
newArr_1 = Array.Array(0)
newArr_1.traverse()
newArr_1WithoutDupes = newArr_1.removeDupes()

print("Another test case with array = [1, 2, 3, 1]")
newArr_2 = Array.Array(4)
newArr_2.insert(1)
newArr_2.insert(2)
newArr_2.insert(3)
newArr_2.insert(1)
newArr_1.traverse()
newArr_2WithoutDupes = newArr_2.removeDupes()