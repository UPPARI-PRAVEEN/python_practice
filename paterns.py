
# *
# * *
# * * *
# * * * *

# n = 4;

# for i in range(n+1):
#     for j in range(i):
#         print("*",end = " ");
#     print("")


# * * * *
# * * *
# * *
# *

# n = 4

# for i in range(n+1,0,-1):
#     for j in range(i):
#         print("*",end = " ")
#     print("")

#   *
#   * *
#  * * *
# * * * *


# n = 4

# for i in range(n+1):
#     for j in range(n - i):
#         print(" ",end = "")
#     for j in range(i):
#         print("*",end = " ")
#     print("")

#   *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#   *


# n = 4

# for i in range(1,n+1):
#     for j in range(n - i):
#         print(" ",end = "")
#     for j in range(i):
#         print("*",end = " ")
#     print("")

# for i in range(n-1,0,-1):
#     for j in range(n - i):
#         print(" ",end = "")
#     for j in range(i):
#         print("*",end = " ")
#     print("")


# A
# A B
# A B C
# A B C D

# n = 4

# for i in range(1,n+1):
    
#     for j in range(i):
#         print(chr(65+j),end = " ")
#     print("")


# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n = 4
# num = 1;
# for i in range(1,n+1):
    
#     for j in range(i):
#         print(num,end = " ")
#         num +=1;
#     print("")

# A 
# 1 2 
# B C D 
# 3 4 5 6 
# n = 4;
# num = 1;
# alph = 1;
# for i in range(1,n+1):
#     for j in range(i):
#         if i % 2 == 0:
#             print(num,end = " ");
#             num +=1
#         else:
#             print(chr(65+alph-1),end = " ")
#             alph +=1;
       
        
#     print("")


# e d c b a 
#   e d c b 
#     e d c 
#       e d 
#         e 

# n = 5;
# space = 0;
# starts = n;
# for i in range(1,n+1):
#     rev = 4
#     for j in range(space):
#         print(" ",end = " ")
#     for j in range(starts):
#         print(chr(97+rev),end = " ")
#         rev -=1
#     space += 1;
#     starts -= 1;
#     print("")


# e 
# e d 
# e d c 
# e d c b 
# e d c b a 

# n = 5;
# num = 1;
# for i in range(1,n+1):
#     alph = 4;

#     for j in range(i):
#         print(chr(alph+97),end = " ")
#         alph -=1;
        
#     print("")


# 1 
# 3 2 
# 6 5 4 
# 10 9 8 7 

# === Code Execution Successful ===
# n = 4;
# num = 1;
# for i in range(1,n+1):
#     ls = [];
#     for j in range(i):
#         ls.append(num)
#         num +=1;

#     for val in ls[::-1]:
#         print(val,end = " ")
        
        
#     print("")

# 1 2 3 4 5 4 3 
#   1 2 3 4 3 
#     1 2 3 
#       1 
        
          
            

# === Code Execution Successful ===
# n = 7;
# itr = 7
# spaces = 0
# for i in range(n):
#     num = 1;
#     for j in range(spaces):
#         print(" ",end = " ");
#     for j in range(itr):
#         if j <= itr // 2:
#             print(num,end = " ")
#             num +=1
#         else:
#             print(num,end = " ")
#             num -=1;
        
#     spaces +=1;
#     itr -=2;
#     print("")