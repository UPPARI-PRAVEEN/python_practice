# #inheritance:
# class A:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(self.name)
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def showAge(self):
#         print(self.age,self.name)

# obj = B("raveen",20)
# obj.show()


# #encapsulation:
# encapsulation is the process of hiding the internal details of an object and only exposing a public interface.
#  In Python, we can achieve encapsulation using private variables and methods.

# class A:
#     def __init__(self,name):
#         self.name = name;
#     def __show(self):
#         print(self.name);
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def showAge(self):
#         self.__show()

# obj = B("raveen",20)
# obj.showAge()

# #polymorphism

# #polymorphism

# class Remote:
#     def __init__(self,name):
#         self.name = name;
#     def controlTVAC(self):
#         print("i ma controlling ",self.name)
# class Tv(Remote):
    
#     def controlTVAC(self):
#         print("i am  Tvssss",self.name)
# class AC(Remote):
    
#     def controlTVAC(self):
#         print("i am acssss",self.name)
# acc = AC("ac")
# tvc = Tv("tv")
# acc.controlTVAC()
# tvc.controlTVAC()

# #Abstract class and methods
# from abc import ABC, abstractmethod

# class Abstract(ABC):

#     @abstractmethod
#     def showDetails(self):
#         pass


# class Child(Abstract):

#     def showDetails(self):
#         print("I am providing implementation")


# obj = Child()
# obj.showDetails()



# Good — saying “I don’t know” honestly is **much better than guessing** 👍
# Let’s cover it quickly (this is a **high-value interview concept** but easy once you get it).

# ---

# ### 💡 What is `@property`?

# > `@property` is a decorator that allows you to access a method **like an attribute (variable)** instead of calling it like a function.

# ---

# ### 🔥 Why we use it

# * To **encapsulate logic**
# * To **control access to variables**
# * To make code look **cleaner (no parentheses)**

# ---

# ### 📌 Normal Method vs Property

# #### ❌ Normal Method

# ```python
# class Demo:
#     def get_value(self):
#         return 10

# obj = Demo()
# print(obj.get_value())  # need ()
# ```

# #### ✅ Using `@property`

# ```python
# class Demo:
#     @property
#     def value(self):
#         return 10

# obj = Demo()
# print(obj.value)  # no ()
# ```

# ---

# ### ⚡ Real Use Case (important)

# ```python
# class Person:
#     def __init__(self, age):
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value < 0:
#             print("Invalid age")
#         else:
#             self._age = value
# ```

# 👉 Now:

# ```python
# p = Person(20)
# print(p.age)   # getter
# p.age = 25     # setter
# ```

# ---

# ### ⭐ Interview Summary Line

# > “`@property` allows a method to be accessed like an attribute and is used for encapsulation with getter and setter functionality.”

# ---

# ### ⭐ Rating for this question: **Honest + learning mindset → 👍**

# ---

# ### **Question 12 (Very Important – Data Structures)**

# **What is the difference between a set and a dictionary in Python?**

# 👉 This is easy but interviewers expect a clean answer.

        
That’s not what namespaces are — you’re describing **variable naming rules**, not namespaces. Let’s correct this properly (important interview concept).

---

### ❌ What’s wrong

* ❌ Namespaces ≠ variable naming rules
* ❌ Keywords/special characters → unrelated here

---

### 💡 Strong Interview Answer (Refined)

> A **namespace** in Python is a container that maps names (variables, functions) to their corresponding objects.
> It helps avoid naming conflicts and organizes code.

---

### 🔹 Types of Namespaces

**1. Local Namespace**

* Inside a function
* Created when function is called
* Destroyed after execution

```python
def func():
    x = 10   # local namespace
```

---

**2. Global Namespace**

* Defined at the top level of a script
* Accessible throughout the program

```python
x = 20   # global namespace
```

---

**3. Built-in Namespace**

* Contains predefined names
* Example: `print()`, `len()`

---

### 🔥 LEGB Rule (very important)

Python searches variables in this order:

> **Local → Enclosing → Global → Built-in**

---

### ⭐ Rating: **3.5/10**

* ❗ Concept misunderstood
* Needs strong correction

---

### 🔥 Key Interview Line

> “Namespace is a mapping between names and objects.”

---

### 👍 Don’t worry

This is a **common confusion** — now you’ve fixed it 👍

---

### **Question 32 (Very Important – Python Internals)**

**What is the difference between `global` and `nonlocal` keywords?**

👉 This is tricky — answer carefully.



Looks like you didn’t complete the answer — no problem 👍 this is an **advanced concept**, many freshers don’t know it.

---

### 💡 What is Monkey Patching?

> Monkey patching is a technique where we **modify or extend the behavior of a class or module at runtime (dynamically)** without changing its original source code.

---

### 📌 Simple Example

```python
class A:
    def show(self):
        print("Original")

def new_show(self):
    print("Modified")

# Monkey patch
A.show = new_show

obj = A()
obj.show()   # Modified
```

---

### 🔹 Key Points

* Happens **at runtime**
* Used to **modify existing behavior**
* Can be risky if overused

---

### 📌 Real Use Cases

* Testing (mocking functions)
* Fixing bugs temporarily
* Extending libraries

---

### ⭐ Rating: **Not Attempted (0/10)**

But that’s okay — this is not a basic question 👍

---

### 🔥 Key Interview Line

> “Monkey patching modifies existing code behavior dynamically at runtime.”

---

### **Question 35 (Important – Python Memory)**

**What is reference counting in Python?**

👉 You already touched this in GC — now explain clearly.
