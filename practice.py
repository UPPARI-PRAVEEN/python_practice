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

# ls =  [-2,1,-3,4,-1,2,1,-5,4]
# currSum = ls[0] #1 -2 4 3 5
# maxSum =ls[0]
# stIndex = 0
# endIndex = 0
# tempIndex = 0;
# #Max subarray sum 
# #OUTUT: 6 [4,-1,2,1]
# for i in range(1,len(ls)):
#     if ls[i] > currSum+ls[i]:
#         currSum = ls[i]
#         tempIndex = i//1
#     else:
#         currSum += ls[i]
#     if currSum > maxSum:# 1 > -2
#         maxSum = currSum #1
#         stIndex = tempIndex #1 4
#         endIndex = i;#1 5 6
# print(stIndex,endIndex)
# print(ls[stIndex:endIndex+1])

# st = "I love python"
# # Output: "python love I"
# res = "";
# word = ""
# for ch in st:
    
#     if ch != ' ':
#         word += ch;
#     else: 
#         res = word + " " + res;
#         word = ""
# res = word + " " + res

# print(res)


# ls = [1,3,2,4]
# targetSum = 6
# res = []

# for i in range(len(ls)):
#     nested = []
#     sumEle = 0
    
#     for j in range(i, len(ls)):
#         nested.append(ls[j])
#         sumEle += ls[j]
        
#         if sumEle == targetSum:
#             res.append(nested[:])   # copy
#             break

# print(res)



# st = "xyz" #azy
# res = ""
# for ch in st:
#     chars = ""
#     if ord(ch) == 122 or ord(ch) == 90:
#         chars = chr(ord(ch) - 25)
#     else:
#         chars = chr(ord(ch) + 1)
#     res = chars + res
#     chars = ""
# print(res)


# 

#cecking amstrong number or not
# num = 153;
# temp = num;
# def countNum(val):
#     para = val
#     count = 0;
#     print(para)
#     while para !=0:
#         count += 1;
#         para = para // 10;
#     return count;
# def isMul(num, count):
#     print(num ** count,"ismul")
#     return num ** count  
# def result(count,num):
    
#     sumNum = 0;
#     for i in range(0,count):
#         print(num,"number digit")
#         sumNum += isMul(num % 10,count)
#         num = num // 10;
#     return sumNum;
        
# count = countNum(num)
# res = result(count,num)
# print(res)
# if res == temp:
#     print("is amstromstorn number");
# else:
#     print("not amstrong number")


        
#    sypnum     
#     num = 1124;

# def sumOfdigit(num, isAdd):
#     result = 0 if isAdd else 1   # ✔ Python ternary

#     val = num
#     while val != 0:
#         digit = val % 10

#         if isAdd:
#             result += digit
#         else:
#             result *= digit

#         val = val // 10

#     return result
# sumNum = sumOfdigit(num,True)
# mulNum = sumOfdigit(num,False)
# print(sumNum,mulNum)


#factorial of number
# num = 5;

# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num - 1)
# res = fact(num)
# print(res)

# num = 4;
# res = 1;
# for i in range(1,num+1):
#     res = res * i;
# print(res)

# prime = 11
# isPrime = True

# for i in range(2,5):
#     if prime % i == 0:
#         isPrime =False
#         break
# if isPrime :
#     print("is a prime number")
# else:
#     print("not a primenumber")
