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
#             res.append(nested[:])   # copy because nested will change in next iteration what happens if we append nested directly 
                                        # nested will be modified in next iteration and res will have reference to nested so it will change as well
#             break

# print(res)#[[1, 3, 2], [2, 4]]



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

#print prime numbers in range or 1 to n
# n = 20;   
# for i in range(2,n+1):
#     isPrime = True    
#     for j in range(2,i//2+1):
#         if i % j == 0:    
#             isPrime = False
#             break 
#     if isPrime:
#         print(i)  


# ls = [1,0,2,0,3,0,4]
# #move zero to end
# pos = 0
# for i in range(len(ls)):
#     if ls[i] != 0:
#         ls[pos], ls[i] = ls[i], ls[pos]
#         pos += 1

# print(ls)

# string = "aabbcde"
# # Output: c fist occurance not repeating character
# revString = ""
# for i in range(len(string)-1):
#     if string[i] not in string[i+1:] and string[i] not in revString:
#         print(string[i]);
#         break;
#     else:
#         revString += string[i]

# string = "aabbcde"

# freq = {}

# for ch in string:
#     freq[ch] = freq.get(ch, 0) + 1

# for ch in string:
#     if freq[ch] == 1:
#         print(ch)
#         break


# arr = [10, 5, 8, 20, 20]

# first = float('-inf')
# second = float('-inf')

# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif first > num > second:
#         second = num

# print(second)

# s = "abcabcbb"
# # Output: True

# def longesSub(string):
#     logGeststr = "";
#     for i in range(len(string)):
#         subStr = ""
#         for j in range(i,len(string)-1):
#             if string[j] in subStr:
#                 break;
#             else:
#                 subStr += string[j];
#         if len(subStr) > len(logGeststr):
#             logGeststr = subStr
            
#     return logGeststr;
# sorting1 = longesSub(s)
# print(sorting1)


# s = "aaabbcc"
# # Output: "a3b2c1"
# res = "";
# count = 0;


# for i in range(len(s)-1):
#     ch = s[i];
#     if ch == s[i+1]:
#         count += 1;
#         print(ch,count)
#     else:
#         res = res + ch + str(count+1)
        
#         count = 0
# res = res + s[-1] + str(count + 1)
# print(res)

# ls =  [16,17,4,3,5,2]
# # Output: [17,5,2]
# res =[];
# for i in range(len(ls)-1):
#     if ls[i] < ls[i+1]:
#         res.append(ls[i+1])
# res.append(ls[-1])       
# print(res)

# nums = [2,7,11,15]
# target = 9

# mp = {}

# for i in range(len(nums)):
#     diff = target - nums[i]
    
#     if diff in mp:
#         print([mp[diff], i])
#         break
    
#     mp[nums[i]] = i

# s = "madams"
# ls = list(s);
# start = 0;
# end = len(ls)-1
# while start < end:
   
    
#     ls[start],ls[end] = ls[end],ls[start]
        
#     start+=1;
#     end-=1;
# print("".join(ls))

# s = "madam"

# start = 0
# end = len(s) - 1

# isPalindrome = True

# while start < end:
#     if s[start] != s[end]:
#         isPalindrome = False
#         break
#     start += 1
#     end -= 1

# print(isPalindrome)


# ls = [1,-2,3,-4,5]
# # Output: [-2,-4,1,3,5]  (order not important)

# start =0
# end = len(ls)-2

# while start < end:
#     if ls[start] > 0:
#         ls[start],ls[end] = ls[end],ls[start]
#     start +=1
#     end -=1
    
# print(ls)

#++++++++++++++++++++++++++++++++++++++++++++ + sliding window ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#**************** find max sum of subarray of size k ****************
# arr = [2,1,5,1,3,2]
# k = 3

# # Output: 9   # (5+1+3)
# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k,len(arr)):
#     window_sum += arr[i]
#     window_sum -= arr[i-k]
#     max_sum = max(max_sum,window_sum)
# print(max_sum)

#********** Revemove duplicates from sorted array **********
arr = [1, 1, 2, 2, 3, 3]

i = 0  

for j in range(1,len(arr)):
    if arr[i] != arr[j]:
        i +=1;
        arr[i] = arr[j]
print(arr[:i+1])

#********** Remove duplicates from unsorted array **********
arr = [3, 1, 2, 1, 3, 2]

i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[i] == arr[j]:
            arr.pop(j)  # remove duplicate
        else:
            j += 1
    i += 1

print(arr)  # [3, 1, 2]

#********** Find the missing number in an array of size n containing numbers from 0 to n **********
arr = [3, 0, 1]

n = len(arr)
expected_sum = n * (n + 1) // 2

actual_sum = 0
for num in arr:
    actual_sum += num

print(expected_sum - actual_sum)

#************* max sum array ****************
arr = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

max_sum = float('-inf');
curr_sum = 0;
start_val = 0
start =0;
end = 0;

for i in range(len(arr)):
    if curr_sum == 0:
        start_val = i
    curr_sum += arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        start = start_val
        end = i
    if curr_sum < 0:
        curr_sum = 0
       
        
print(max_sum,start,end)


#************************ Logest increasing subsequence without db ******************
arr = [10,9,2,5,3,7,101,18]
# Output: 4

def f(index,prev_index,arr,n):
    if index == n:
        return 0
    not_take = 0 + f(index+1,prev_index,arr,n)
    take = 0;
    if prev_index == -1 or arr[index] > arr[prev_index]:
        take = 1 + f(index+1,index,arr,n)
    return max(take,not_take);
res = f(0,-1,arr,len(arr)-1)
print(res)

#***************** Logest increasing subsequence with db ******************
arr = [3, 1, 2]
# Output: 4
def f(index, prev_index, arr, n,dp):
        if index == n:
            return 0
        
        if dp[index][prev_index+1] != -1:
            return dp[index][prev_index+1]

        not_take = f(index + 1, prev_index, arr, n,dp)
        
        
        take = 0
        if prev_index == -1 or arr[index] > arr[prev_index]:
            take = 1 + f(index + 1, index, arr, n,dp)
        
        dp[index][prev_index+1] = max(take, not_take)
        print(dp)
        return dp[index][prev_index+1]



n = len(arr)
dp = [[-1] * (n + 1) for _ in range(len(arr))]
print(dp)
res = f(0, -1, arr, n,dp)
print(res)


#***************** Coin change 2 ******************
class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        return self.f(n - 1, amount, coins, dp)

    def f(self, index, target, arr, dp):
        if index == 0:
            if target % arr[0] == 0:
                return 1
            return 0

        if dp[index][target] != -1:
            return dp[index][target]

        not_take = self.f(index - 1, target, arr, dp)

        take = 0
        if target >= arr[index]:
            take = self.f(index, target - arr[index], arr, dp)

        dp[index][target] = take + not_take
        return dp[index][target]


#****** 0/1 knap scact with paint walls ******************
class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = {}

        def fn(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            # Option 1: take paid painter
            take = cost[i] + fn(i + time[i] + 1)
            
            # Option 2: skip
            skip = fn(i + 1)
            
            dp[i] = min(take, skip)
            return dp[i]

        return fn(0)

#************ DP paint walls ******************
class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = {}

        def fn(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            # Option 1: take paid painter
            take = cost[i] + fn(i + time[i] + 1)
            
            # Option 2: skip
            skip = fn(i + 1)
            
            dp[i] = min(take, skip)
            return dp[i]

        return fn(0)
