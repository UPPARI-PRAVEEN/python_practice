# Sample list
lst = [10, 20, 30, 40]

# 1. append() → adds element at end
lst.append(50)
print(lst)  # [10, 20, 30, 40, 50]


# 2. extend() → adds multiple elements
lst.extend([60, 70])
print(lst)  # [10, 20, 30, 40, 50, 60, 70]


# 3. insert() → insert at specific index
lst.insert(1, 15)
print(lst)  # [10, 15, 20, 30, 40, 50, 60, 70]


# 4. remove() → removes first occurrence
lst.remove(30)
print(lst)  # [10, 15, 20, 40, 50, 60, 70]


# 5. pop() → removes by index (default last)
lst.pop()
print(lst)  # [10, 15, 20, 40, 50, 60]

lst.pop(2)
print(lst)  # [10, 15, 40, 50, 60]


# 6. clear() → removes all elements
temp = [1, 2, 3]
temp.clear()
print(temp)  # []


# 7. index() → returns index of element
print(lst.index(40))  # 2


# 8. count() → count occurrences
lst2 = [1, 2, 2, 3, 2]
print(lst2.count(2))  # 3


# 9. sort() → sorts list (in-place)
lst3 = [5, 2, 8, 1]
lst3.sort()
print(lst3)  # [1, 2, 5, 8]

# descending
lst3.sort(reverse=True)
print(lst3)  # [8, 5, 2, 1]


# 10. reverse() → reverses list
lst4 = [1, 2, 3]
lst4.reverse()
print(lst4)  # [3, 2, 1]


# 11. copy() → shallow copy
lst5 = [1, 2, 3]
new_lst = lst5.copy()
print(new_lst)  # [1, 2, 3]