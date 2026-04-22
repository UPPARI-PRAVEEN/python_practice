a = [1, 2, 3]
b = a
b.append(4)

print(a)[1,2,3,4]
print(b)[1,2,3,4]

a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)[1,2,3]
print(b)[1,2,3,4]

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
[[1, 2, 99], [3, 4]]
[[1, 2, 99], [3, 4]]
print(a)
print(b)


import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)
[[1, 2], [3, 4]]
[[1, 2, 99], [3, 4]]
print(a)
print(b)

x = 10

def func():
    print(x)
    x = 20
UnboundLocalError: local variable 'x' referenced before assignment
func()

Fix the above code so it prints 10 without removing x = 20.
x = 10
def func():
    global x
    print(x)
    x = 20
func()

def func(a, b=[]):
    b.append(a)
    return b
[1]
[1, 2]
[1, 2, 3]
print(func(1))
print(func(2))
print(func(3))

print(bool('False'))
print(bool(''))
print(bool(0))
print(bool(None))
True
False
False
False

a = [1, 2, 3]
b = [a] * 3

b[0].append(4)

print(b)
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(0.1 + 0.2 == 0.3) #False
print(0.1 + 0.2)#0.30000000000000004

a = "hello"
b = "hello"

print(a is b)
print(a == b)

True
True

a = "hello world"
b = "hello world"

print(a is b)
print(a == b)
False
True

a = (1, 2, [3, 4])
a[2].append(5)

print(a)#(1, 2, [3, 4, 5])

a = (1, 2, [3, 4])
a[2] = [5, 6]

print(a)#TypeError: 'tuple' object does not support item assignment

print([i for i in range(3)])#[0, 1, 2]
print((i for i in range(3)))#<generator object <genexpr> at 0x7f8b8c0e5c80>

a = [1, 2, 3]
print(a[::-1])#[3, 2, 1]
print(a[::2])#[1, 3]

a = [1, 2, 3]
print(a[-1])#3
print(a[-2])#2
print(a[-3])#1

a = [1, 2, 3, 4]
print(a[1:-1])#[2, 3]
print(a[1:3])#[2, 3]

a = [1, 2, 3]
b = a[:]#it will create a new list with the same elements as a and assign it to b.

b[0] = 100

print(a)#[1, 2, 3]
print(b)#[100, 2, 3]


a = [1, 2, 3]
b = a

a = a + [4]#i will create a new list with the elements of a and 4 and assign it to a.
[1, 2, 3, 4]
[1, 2, 3]
print(a)
print(b)


a = [1, 2, 3]
b = a

a += [4]#it will modify the list a in place and add 4 to it. don't create a new list.
[1, 2, 3, 4]
[1, 2, 3, 4]

print(a)
print(b)

a = (1, 2, 3)
b = a

a += (4,)

print(a)#(1, 2, 3, 4)
print(b)#(1, 2, 3)

print([] == False)#True epty list is not equal to False
print([] is False)#False empty list is not the same object as False

#all the empty data structures are considered False in boolean context but they are not the same object as False.
print(bool([]))
print(bool({}))
print(bool(()))

a = [1, 2, 3]
print(id(a))

a = a + [4]
print(id(a))
#id means the memory address of the object. when we do a + [4] it creates a new list and assigns it to a, so the memory address of a changes.

a = [1, 2, 3]
b = a

print(id(a), id(b))

a += [4]

print(id(a), id(b))


def outer():
    x = 10
    def inner():
        print(x)
    x = 20
    return inner

f = outer()
f()#20 because when we call f() it will print the value of x which is 20. even though x is defined before the inner function, it will use the value of x at the time of the call, not at the time of the definition.


funcs = []

for i in range(3):
    def f():
        return i
    funcs.append(f)

print([fn() for fn in funcs])#[2, 2, 2] because when we call fn() it will return the value of i which is 2 at the end of the loop. all the functions in funcs will return the same value of i which is 2. to fix this we can use a default argument in the function definition.

funcs = []
for i in range(3):
    def f(i=i):
        return i
    funcs.append(f) 
print([fn() for fn in funcs])#[0, 1, 2] because now each function will have its own value of i as a default argument. when we call fn() it will return the value of i that was passed as a default argument at the time of the function definition.


def func():
    res = []
    for i in range(3):
        res.append(lambda: i)
    return res

f1, f2, f3 = func()

print(f1(), f2(), f3())#2 2 2 because when we call f1(), f2(), f3() it will return the value of i which is 2 at the end of the loop. all the functions in res will return the same value of i which is 2. to fix this we can use a default argument in the lambda function definition.


def outer():
    x = 10
    def inner():
        x += 1
        return x
    return inner

f = outer()
print(f())#UnboundLocalError: local variable 'x' referenced before assignment because when we try to modify x inside the inner function, it creates a new local variable x which is not defined before. to fix this we can use the nonlocal keyword to tell Python that we want to use the x defined in the outer function.


def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner
f = outer()
print(f())#11 because now we are using the x defined in the outer function and modifying

def outer():
    x = 10
    def inner():
        print(x)
    x = 50
    return inner

x = 100
f = outer()
f()#50 because when we call f() it will print the value of x which is 50. even though x is defined before the inner function, it will use the value of x at the time of the call, not at the time of the definition. and it will use the value of x from the outer function, not from the global scope.


class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        print("B init")

obj = B()#B init because when we create an object of class B, it will call the __init__ method of class B, not class A. to call the __init__ method of class A we can use super() function in the __init__ method of class B.

class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

obj = B()#A init
#B init because now we are calling the __init__ method of class A using super()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

obj = B()
obj.show()#B because when we call obj.show() it will call the show method of class B, not class A. to call the show method of class A we can use super() function in the show method of class B.

#method overriding
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

obj = B()
obj.show()#A
#B because now we are calling the show method of class A using super() in the show method of class B, and then printing B.

class A:
    x = 10

obj1 = A()
obj2 = A()

obj1.x = 20

print(obj1.x)#20 because when we assign a value to obj1.x it creates an instance variable x for obj1 and assigns it the value 20. it does not affect the class variable x which is still 10. when we print obj1.x it will print the instance variable x which is 20.
print(obj2.x)#10 because when we print obj2.x it will look for the instance variable x in obj2, but it does not find it, so it will look for the class variable x in class A and print its value which is 10.

class A:
    x = 10

obj1 = A()
obj2 = A()

A.x = 50

print(obj1.x)#50 because when we assign a value to A.x it changes the value of the class variable x for all the instances of class A. when we print obj1.x and obj2.x it will look for the instance variable x in obj1 and obj2, but it does not find it, so it will look for the class variable x in class A and print its value which is 50.
print(obj2.x)#50 because when we assign a value to A.x it changes the value of the class variable x for all the instances of class A. when we print obj1.x and obj2.x it will look for


class A:
    x = []

obj1 = A()
obj2 = A()

obj1.x.append(1)

print(obj1.x)
print(obj2.x)#[1] because when we append a value to obj1.x it modifies the class variable x which is a list. since obj2.x is also referring to the same class variable x, it will also reflect the change and print [1]. to avoid this we can use an instance variable instead of a class variable for x.

class A:
    x = 10
    def __init__(self):
        self.x = 20

obj = A()
print(obj.x)#20 because when we create an object of class A, it will call the __init__ method which assigns the value 20 to the instance variable x. when we print obj.x it will print the instance variable x which is 20. when we print A.x it will print the class variable x which is 10.
print(A.x)#10 because when we print A.x it will print the class variable x which is 10. the instance variable x does not affect the class variable x.

class A:
    x = 10

class B(A):
    pass

obj = B()
print(obj.x)#10 because when we create an object of class B, it will look for the attribute x in class B, but it does not find it, so it will look for the attribute x in class A and print its value which is 10. when we print obj.x it will print the value of x from class A since class B does not have its own x attribute.

B.x = 50
print(obj.x)#50 because when we assign a value to B.x it creates a new class variable x for class B and assigns it the value 50. when we print obj.x it will look for the attribute x in class B and find it, so it will print its value which is 50. the class variable x in class A is still 10, but it does not affect the value of x in class B.

A.x = 100
print(obj.x)#50 because when we assign a value to A.x it changes the value of the class variable x in class A, but it does not affect the class variable x in class B since class B has its own x attribute. when we print obj.x it will look for the attribute x in class B and find it, so it will print its value which is 50. the class variable x in class A is now 100, but it does not affect the value of x in class B.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()#B because when we create an object of class D and call the show method, it will look for the show method in class D, but it does not find it, so it will look for the show method in class B and find it, so it will print "B". if class B did not have a show method, it would look for the show method in class C and print

"C". if class C also did not have a show method, it would look for the show method in class A and print"A". the method resolution order (MRO) for class D is D -> B -> C -> A, so it will look for the show method in that order.   

what is method resolution order (MRO) in Python?
Method resolution order (MRO) is the order in which Python looks for a method in a
class hierarchy when a method is called on an object. it determines which method will be executed when there are multiple methods with the same name in different classes in the hierarchy. the MRO is determined by the C3 linearization 
algorithm, which ensures a consistent and predictable order of method resolution. you can view the MRO of a class using the __mro__ attribute or the mro() method.
print(D.__mro__)#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
