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

        
        
        