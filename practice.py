# ls = [1, 2, 3, 4, 5, 6];#[1, 3, 5, 2, 4, 6]
# #mmove even to end

# for i in range(len(ls)):
#     for j in range(len(ls)-1):
#         if ls[j] % 2 == 0:
#             temp = ls[j]
#             ls[j] = ls[j+1]
#             ls[j+1] = temp
# print(ls)

#reverse list
# ls = [1, 2, 3, 4, 5, 6]

# start = 0
# end = len(ls)-1
# while start < end:
#     temp = ls[start]
#     ls[start] = ls[end]
#     ls[end] = temp
#     start +=1
#     end -=1
# print(ls)

# ls =[1,2,3,5]
# #find missing number in list
# for i in range(len(ls)-1):
#     if ls[i]+1 != ls[i+1]:
#         print(ls[i]+1)

# st = "programming"
# #firt occurence of non repeating character
# for i in range(len(st)):
#     if st[i] not in st[i+1:]:
#         print(st[i])
#         break

#exception handling
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)

# except ValueError:
#     print("Invalid input! Please enter a valid integer.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except Exception as e:
#     print("Something went wrong:", e)

# finally:
#     print("Program executed successfully.")
        
# transactions = [
#     {"user": "A", "amount": 100},
#     {"user": "B", "amount": 200},
#     {"user": "A", "amount": 300},
#     {"user": "C", "amount": 400},
#     {"user": "B", "amount": 100}
# ]#{'A': 400, 'B': 300, 'C': 400}
# dic = {}
# for i in range(len(transactions)):
   
#     if transactions[i]["user"] in dic:
#         print("hi")
#         dic[transactions[i]["user"] ] += transactions[i]["amount"]
#     else: 
#         print("first")
#         dic[transactions[i]["user"] ] = transactions[i]["amount"]
       
# print(dic)
    
# ls = [1,2,3,4,5,6];
# k = 3;
# #[4, 5, 6, 1, 2, 3]

# def reverse(ls,st,ed):
    
#     while st < ed:
#         temp = ls[st]
#         ls[st] = ls[ed]
#         ls[ed] = temp
#         st += 1;
#         ed -= 1;
#     return ls

# reverse(ls,0,len(ls)-1)
# reverse(ls,0,k-1)
# reverse(ls,k,len(ls)-1)


# print(ls)