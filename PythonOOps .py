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
        
        
        