ls = [1, 2, 3, 4, 5, 6];#[1, 3, 5, 2, 4, 6]
#mmove even to end

ls = [1, 2, 3, 4, 5, 6]

left = 0
right = len(ls) - 1

while left < right:
    if ls[left] % 2 != 0:
        left += 1
    else:
        ls[left], ls[right] = ls[right], ls[left]
        right -= 1

print(ls)

for i in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j] % 2 == 0:
            temp = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = temp
print(ls)

reverse list
ls = [1, 2, 3, 4, 5, 6]

start = 0
end = len(ls)-1
while start < end:
    temp = ls[start]
    ls[start] = ls[end]
    ls[end] = temp
    start +=1
    end -=1
print(ls)

ls =[1,2,3,5]
#find missing number in list
for i in range(len(ls)-1):
    if ls[i]+1 != ls[i+1]:
        print(ls[i]+1)
to find missing number in list with 0 to n
ls = [0,1,2,4,5]
total_sum = len(ls) * (len(ls) + 1) // 2
actual_sum = sum(ls)
if total_sum - actual_sum != 0:
    print(total_sum - actual_sum)
else:    
    print("no missing number")

ls = [1, 6]

for i in range(len(ls)-1):
    if ls[i]+1 != ls[i+1]:
        for j in range(ls[i]+1,ls[i+1]):
             print(j)

#*** find first non repeating character in string
st = "programming"
#firt occurence of non repeating character
res = ""
for i in range(len(st)-1):
    if st[i] not in st[i+1:] and st[i] not in res:
        print(st[i])
        break;
    else:
        res += st[i]
# or we can use dictionary to count frequency of each character and then find first character with frequency 1
dic = {}
for ch in st:
    dic[ch] = dic.get(ch,0) + 1
for ch in st:
    if dic[ch] == 1:
        print(ch)
        break;

exception handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Program executed successfully.")
        
transactions = [
    {"user": "A", "amount": 100},
    {"user": "B", "amount": 200},
    {"user": "A", "amount": 300},
    {"user": "C", "amount": 400},
    {"user": "B", "amount": 100}
]#{'A': 400, 'B': 300, 'C': 400}
dic = {}
for i in range(len(transactions)):
   
    if transactions[i]["user"] in dic:
        print("hi")
        dic[transactions[i]["user"] ] += transactions[i]["amount"]
    else: 
        print("first")
        dic[transactions[i]["user"] ] = transactions[i]["amount"]
       
print(dic)
    
ls = [1,2,3,4,5,6];
k = 3;
#[4, 5, 6, 1, 2, 3]

def reverse(ls,st,ed):
    
    while st < ed:
        temp = ls[st]
        ls[st] = ls[ed]
        ls[ed] = temp
        st += 1;
        ed -= 1;
    return ls

reverse(ls,0,len(ls)-1)
reverse(ls,0,k-1)
reverse(ls,k,len(ls)-1)


print(ls)


#**** max sum of subarray
ls =  [-2,1,-3,4,-1,2,1,-5,4]

max_sum = float('-inf')
curr_sum = 0;
tempStart = 0
start = 0
end = 0;

for i in range(len(ls)):
    if curr_sum == 0:
        tempStart = i
    curr_sum += ls[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        start = tempStart
        end = i
    if curr_sum < 0:
        curr_sum = 0
print(ls[start:end+1])

st = "I love python"
# Output: "python love I"
res = "";
word = ""
for ch in st:
    
    if ch != ' ':
        word += ch;
    else: 
        res = word + " " + res;
        word = ""
res = word + " " + res

print(res)

#**** find all subarray with given sum

ls = [1,3,2,4]
targetSum = 6
res = []

for i in range(len(ls)):
    nested = []
    sumEle = 0
    
    for j in range(i, len(ls)):
        nested.append(ls[j])
        sumEle += ls[j]
        
        if sumEle == targetSum:
            res.append(nested[:])   # copy because nested will change in next iteration what happens if we append nested directly 
                                        nested will be modified in next iteration and res will have reference to nested so it will change as well
            break

print(res)#[[1, 3, 2], [2, 4]]
#optimized approach using hashmap prefix sum
hp = {}
curr_sum = 0
for i in range(len(ls)):    
    curr_sum += ls[i]
    
    if curr_sum == targetSum:
        res.append(ls[:i+1])
    
    if (curr_sum - targetSum) in hp:
        res.append(ls[hp[curr_sum - targetSum] + 1 : i + 1])
    
    hp[curr_sum] = i
print(res)#[[1, 3, 2], [2, 4]]



st = "xyz" #azy
res = ""
for ch in st:
    chars = ""
    if ord(ch) == 122 or ord(ch) == 90:
        chars = chr(ord(ch) - 25)
    else:
        chars = chr(ord(ch) + 1)
    res = chars + res
    chars = ""
print(res)




# cecking amstrong number or not
num = 153;
temp = num;
def countNum(val):
    para = val
    count = 0;
    print(para)
    while para !=0:
        count += 1;
        para = para // 10;
    return count;
def isMul(num, count):
    return num ** count  
def result(count,num):
    
    sumNum = 0;
    for i in range(0,count):
        print(num,"number digit")
        sumNum += isMul(num % 10,count)
        num = num // 10;
    return sumNum;
        
count = countNum(num)
res = result(count,num)
print(res)
if res == temp:
    print("is amstromstorn number");
else:
    print("not amstrong number")


# ********* sypnum     
    num = 1124

def sumOfdigit(num, isAdd):
    result = 0 if isAdd else 1   # ✔ Python ternary

    val = num
    while val != 0:
        digit = val % 10

        if isAdd:
            result += digit
        else:
            result *= digit

        val = val // 10

    return result
sumNum = sumOfdigit(num,True)
mulNum = sumOfdigit(num,False)
print(sumNum,mulNum)


#  factorial of number
num = 5

def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)
res = fact(num)
print(res)
 # or we can do it iteratively
num = 4;
res = 1;
for i in range(1,num+1):
    res = res * i;
print(res)

prime = 11
isPrime = True

for i in range(2,5):
    if prime % i == 0:
        isPrime =False
        break
if isPrime :
    print("is a prime number")
else:
    print("not a primenumber")

print prime numbers in range or 1 to n
n = 20;   
for i in range(2,n+1):
    isPrime = True    
    for j in range(2,i//2+1):
        if i % j == 0:    
            isPrime = False
            break 
    if isPrime:
        print(i)  


ls = [1,0,2,0,3,0,4]
#move zero to end
pos = 0
for i in range(len(ls)):
    if ls[i] != 0:
        ls[pos], ls[i] = ls[i], ls[pos]
        pos += 1

print(ls)

string = "aabbcde"
# Output: c fist occurance not repeating character
revString = ""
for i in range(len(string)-1):
    if string[i] not in string[i+1:] and string[i] not in revString:
        print(string[i]);
        break;
    else:
        revString += string[i]

string = "aabbcde"

freq = {}

for ch in string:
    freq[ch] = freq.get(ch, 0) + 1

for ch in string:
    if freq[ch] == 1:
        print(ch)
        break


arr = [10, 5, 8, 20, 20]

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second)
#***** longest substring without repeating characters
s = "abcabcbb"
# Output: "abc"

def longesSub(string):
    logGeststr = "";
    for i in range(len(string)):
        subStr = ""
        for j in range(i,len(string)-1):
            if string[j] in subStr:
                break;
            else:
                subStr += string[j];
        if len(subStr) > len(logGeststr):
            logGeststr = subStr
            
    return logGeststr;
sorting1 = longesSub(s)
print(sorting1)


#**** count of each character in string 
s = "aaabbcc"
# Output: "a3b2c1"
res = "";
count = 0;


for i in range(len(s)-1):
    ch = s[i];
    if ch == s[i+1]:
        count += 1;
        print(ch,count)
    else:
        res = res + ch + str(count+1)
        
        count = 0
res = res + s[-1] + str(count + 1)
print(res)


#**** find all elements which are greater than next element in list
ls = [16, 17, 4, 3, 5, 2]
res = []

# The rightmost element is always a leader
current_max = ls[-1]
res.append(current_max)

# Start from the second to last element and move backwards
for i in range(len(ls) - 2, -1, -1):
    if ls[i] > current_max:
        current_max = ls[i]
        res.append(current_max)

# Since we collected them backwards, reverse to match original order
res.reverse()
print(res)  # Output: [17, 5, 2]

nums = [2,7,11,15]
target = 9

mp = {}

for i in range(len(nums)):
    diff = target - nums[i]
    
    if diff in mp:
        print([mp[diff], i])
        break
    
    mp[nums[i]] = i

s = "madams"
ls = list(s);
start = 0;
end = len(ls)-1
while start < end:
   
    
    ls[start],ls[end] = ls[end],ls[start]
        
    start+=1;
    end-=1;
print("".join(ls))

s = "madam"

start = 0
end = len(s) - 1

isPalindrome = True

while start < end:
    if s[start] != s[end]:
        isPalindrome = False
        break
    start += 1
    end -= 1

print(isPalindrome)


ls = [1,-2,3,-4,5]
# Output: [-2,-4,1,3,5]  (order not important)

start =0
end = len(ls)-2

while start < end:
    if ls[start] > 0:
        ls[start],ls[end] = ls[end],ls[start]
    start +=1
    end -=1
    
print(ls)

++++++++++++++++++++++++++++++++++++++++++++ + sliding window ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
**************** find max sum of subarray of size k  ****************
arr = [2,1,5,1,3,2]
k = 3

# Output: 9   # (5+1+3)
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i-k]
    max_sum = max(max_sum,window_sum)
print(max_sum)

#********** Revemove duplicates from sorted array **********
arr = [1, 1, 2, 2, 3, 3]
# ourput: [1, 2, 3] (the first three elements of the array are now 1, 2, and 3, and the rest of the elements can be ignored)
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
# Output: 4 because the longest increasing subsequence is [2,3,7,101] and its length is 4.

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

#***************** Merge sort leetcode 912******************
#input: nums = [5,2,3,1]
#output: [1,2,3,5] (the array is sorted in ascending order using the merge sort algorithm)
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j +=1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        return mergeSort(nums)


#***************** Best time to buy and sell stock 121 ******************
#input: prices = [7,1,5,3,6,4]
#output: 5 (buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif sell_profit < prices[i] - buy:
                sell_profit = prices[i] - buy
        return sell_profit


        

            





        


#***************** Coin change 2 ******************
#input: amount = 4, coins = [1, 2, 3]
#output: 4 (there are four ways to make up the amount: 1) 1+1+1+1, 2) 1+1+2, 3) 1+3, 4) 2+2)
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
        #input: amount = 4, coins = [1, 2, 3]
        #output: 4 (there are four ways to make up the amount: 1) 1+1+1+1, 2) 1+1+2, 3) 1+3, 4) 2+2)


#****** 0/1 knap scact with paint walls ******************
class Solution(object):
    #input: cost = [1, 2, 3], time = [1, 2, 3]
    #output: 2 (paint wall 0 with cost 1, then skip wall 1 because painter is busy, and paint wall 2 with cost 3. Total cost = 1 + 3 = 4)
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

#************ longest common subsequence leetcode 1143 ******************
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #input: text1 = "abcde", text2 = "ace"
        #output: 3 (longest common subsequence is "ace" and its length is 3.)
        #because "ace" is a subsequence of "abcde" and "ace", and its length is 3.
        #invalid input: text1 = "abc", text2 = "def"
        #output: 0 (there is no common subsequence between "abc" and "def", so the length of the longest common subsequence is 0.)
        len1 = len(text1)
        len2 = len(text2)
        dp = [[-1 for _ in range(len2)] for _ in range(len1)]

        res = self.fn(len1-1,len2-1,text1,text2,dp)
        return res
    
    def fn(self,i,j,s1,s2,dp):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.fn(i-1,j-1,s1,s2,dp)
        else:
            dp[i][j] =0 + max(self.fn(i-1,j,s1,s2,dp),self.fn(i,j-1,s1,s2,dp)) 
        return dp[i][j]


#************* Edit distance leetcode 72 ******************
class Solution(object):
    #EG word1 = "horse", word2 = "ros"
    #OUTPUT: 3 (horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e'))
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[-1  for _ in range(l2)] for _ in range(l1)]
        return self.fn(l1-1,l2-1,word1,word2,dp)
    def fn(self,i,j,s1,s2,dp):
        if i<0:
            return j + 1
        if j < 0:
            return i + 1
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s1[i] == s2[j]:
            dp[i][j] = 0 + self.fn(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        if s1[i] != s2[j]:
            dp[i][j] = 1 + min(self.fn(i-1,j,s1,s2,dp),self.fn(i,j-1,s1,s2,dp),self.fn(i-1,j-1,s1,s2,dp))
            return dp[i][j]


#***************** Edit distance deletion operation with only insert and delete 583 ******************
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        return self.fn(len(word1)-1,len(word2)-1,word1,word2,dp)
    def fn(self,i,j,s1,s2,dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = 0 + self.fn(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        if s1[i] != s2[j]:
            dp[i][j] = 1 + min(self.fn(i-1,j,s1,s2,dp),self.fn(i,j-1,s1,s2,dp))
            return dp[i][j]
#******************* Make the three string equal ******************
class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        res = self.fn(len(s1)-1, len(s2)-1, len(s3)-1, s1, s2, s3)
        return res if res != float('inf') else -1

    def fn(self, i, j, k, s1, s2, s3):
        # if s3 is done → delete remaining chars
        if k < 0:
            return (i + 1) + (j + 1)

        # if any string finished but s3 still left → impossible
        if i < 0 or j < 0:
            return float('inf')

        # if all match
        if s1[i] == s2[j] == s3[k]:
            return self.fn(i-1, j-1, k-1, s1, s2, s3)

        # otherwise delete from s1 or s2
        return 1 + min(
            self.fn(i-1, j, k, s1, s2, s3),
            self.fn(i, j-1, k, s1, s2, s3)
        )

#***************** Minimum path sum 64 ******************
#input: grid = [[1,3,1],[1,5,1],[4,2,1]]
#output: 7 (1 → 3 → 1 → 1 → 1)

class Solution(object):
    def minPathSum(self, grid):
        # Rows: len(grid), Cols: len(grid[0])
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.fn(0, 0, grid, dp)

    def fn(self, i, j, grid, dp):
        # Out of bounds check
        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')
        
        # Memoization check
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Base case: Reached the bottom-right cell
        # Fixed the j check here:
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        # Recursive steps
        move_nx_col = grid[i][j] + self.fn(i, j + 1, grid, dp)
        move_next_row = grid[i][j] + self.fn(i + 1, j, grid, dp)
        
        dp[i][j] = min(move_nx_col, move_next_row)
        return dp[i][j]

#***************** Word break 139 ******************
#input: s = "leetcode", wordDict = ["leet", "code"]
#output: true (because "leetcode" can be segmented as "leet code")


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)+1
        dp = [False] * n
        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

###***************** Partition equal subset sum 416 ******************
#input: nums = [1,5,11,5]
#output: true (the array can be partitioned as [1, 5, 5] and [11])

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)-1
        
        t_sum = sum(nums)
        if t_sum % 2 != 0:
            return False
        target = t_sum // 2
        
        # target + 1 because we need to include the index for 'target' itself
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
        return self.fn(l,target,nums,dp)


    
    def fn(self,i,target,arr,dp):

        if target == 0:
            return True
        if i == 0:
            return target == arr[i]
        if dp[i][target] != -1:
            return dp[i][target]
        not_take = self.fn(i-1,target,arr,dp)
        take = False
        if arr[i] < target:
            
            take = self.fn(i-1,target-arr[i],arr,dp)
        dp[i][target] = take or not_take
        return dp[i][target]

##***************** Number of islands 200 ******************
#problem: Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
#vertically. You may assume all four edges of the grid are all surrounded by water.

#input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
#output: 3 (there are three islands: one consisting of the first four '1's, one consisting of the single '1' in the middle, and one consisting of the last two '1's)
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = set()
        
        count = 0
        
        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == "1" and (row, col) not in visited:
                    count += 1
                    self.bfs(row, col, visited, grid, rowLen, colLen)
        
        return count

    def bfs(self, row, col, visited, grid, rowLen, colLen):
        queue = [(row, col)]
        visited.add((row, col))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c = queue.pop(0)
            
            for dr, dc in directions:
                nrow = r + dr
                ncol = c + dc
                
                if (0 <= nrow < rowLen and 0 <= ncol < colLen and
                    grid[nrow][ncol] == "1" and (nrow, ncol) not in visited):
                    
                    queue.append((nrow, ncol))
                    visited.add((nrow, ncol))
#*** Kahn's algorithm for topological sort ******************
#algarithm
first we calculate indegree of each node and build the adjacency list
then we add all nodes with indegree 0 to the queue
then we pop from queue and add to topo sort result and decrease indegree of its neighbors by 1 and if any neighbor's indegree becomes 0 we add it to queue
from collections import deque

def topoSort(n, edges):
    adj = {i: [] for i in range(n)}
    indegree = [0] * n
    
    # build graph
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # queue of 0 indegree nodes
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    topo = []
    
    while queue:
        node = queue.popleft()
        topo.append(node)
        
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    # cycle check
    if len(topo) != n:
        return []  # cycle exists
    
    return topo

#******** Flood fill 733 ******************
#input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#output: [[2,2,2],[2,2,0],[2,0,1]] (starting from the pixel at (sr, sc), which is 1, all connected pixels with the same color 1 are changed to color 2)

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rLen = len(image)
        cLen = len(image[0])
        visited =set()
        original_C = image[sr][sc]
        if original_C == color:
            return image
        return self.dfs(sr,sc,image,visited,rLen,cLen,color,original_C )

    def dfs(self,sr,sc,image,visited,rLen,cLen,color,original_C ):
        visited.add((sr,sc))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        que = [(sr,sc)]
        image[sr][sc] = color

        while que:
            r,c = que.pop(0)
            for row,col in directions:
                dR = row + r
                dc = c + col
                if 0 <= dR < rLen and 0 <= dc < cLen and image[dR][dc] == original_C:
                    image[dR][dc] = color 
                    que.append([dR,dc])
        return image


#************* rotten oranges 994 ******************
#input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#output: 4 (Minute 0: [[2,1,1],[1,1,0],[0,1,1]] (initial state)
#Minute 1: [[2,2,1],[2,1,0],[0,1,1]] (the rotten orange at (0, 0) rots the adjacent fresh orange at (0, 1))
#Minute 2: [[2,2,2],[2,2,0],[0,1,1]] (the rotten oranges at (0, 0) and (0, 1) rot the adjacent fresh orange at (0, 2) and (1, 0))
#Minute 3: [[2,2,2],[2,2,0],[0,2,1]] (the rotten oranges at (0, 0), (0, 1), and (0, 2) rot the adjacent fresh orange at (1, 1))
#Minute 4: [[2,2,2],[2,2,0],[0,2,2]] (the rotten orange at (1, 1) rots the adjacent fresh orange at (2, 1))


from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rLen = len(grid)
        cLen = len(grid[0])
        que = deque()
        fresh = 0
        
       

        for row in range(rLen):
            for col in range(cLen):
                if grid[row][col] == 2:
                    que.append((row,col))
                elif grid[row][col] == 1:
                    fresh +=1
                

        if fresh == 0:
            return 0
        
        minutes = 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while que:
            size = len(que)
            for _ in range(size):
                r,c = que.popleft()
            
                for rcol,ccol in directions:
                    rd = rcol + r
                    cd = c + ccol
                    if 0 <= rd < rLen and 0 <= cd < cLen and grid[rd][cd] == 1:
                        grid[rd][cd] = 2
                        que.append((rd,cd))
                        fresh -=1
            minutes +=1
        
        return minutes - 1 if fresh == 0 else -1
#**** Surrounded regions 130 ******************
#input: grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#output: [["X","X","X","X"],["X","X","X","  X"],["X","X","X","X"],["X","O","X","X"]] (the 'O's in the middle are surrounded by 'X's and are flipped to 'X', while the 'O' at the bottom is not surrounded and remains unchanged)

class Solution(object):
    def solve(self, grid):
        if not grid:
            return 0
        
        rowLen = len(grid)
        colLen = len(grid[0])
        
        
        
        
        for i in range(rowLen):
            if grid[i][0] == "O":
                self.bfs(i,0,grid,rowLen, colLen)
            if grid[i][colLen-1] == "O":
                self.bfs(i,colLen-1,grid,rowLen, colLen)
        for j in range(colLen):
            if grid[0][j] == "O":
                self.bfs(0,j,grid,rowLen, colLen)
            if grid[rowLen-1][j] == "O":
                self.bfs(rowLen-1,j,grid,rowLen, colLen)
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 'S':
                    grid[i][j] = 'O'
                elif grid[i][j] == 'O':
                    grid[i][j] = 'X'


        
        return grid

    def bfs(self, row, col, grid,rowLen, colLen):
        queue = [(row, col)]
        grid[row][col] = "S"
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c = queue.pop(0)
            
            for dr, dc in directions:
                nrow = r + dr
                ncol = c + dc
                
                if 0 <= nrow < rowLen and 0 <= ncol < colLen and grid[nrow][ncol] == "O":
                    
                    grid[nrow][ncol] = "S"
                    queue.append((nrow, ncol))
#***************** Rotten oranges 994 ******************
#input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#output: 4 (Minute 0: [[2,1,1],[1,1,0],[0,1,1]] (initial state)
#Minute 1: [[2,2,1],[2,1,0],[0,1,1]] (the rotten orange at (0, 0) rots the adjacent fresh orange at (0, 1))
#Minute 2: [[2,2,2],[2,2,0],[0  ,1,1]] (the rotten oranges at (0, 0) and (0, 1) rot the adjacent fresh orange at (0, 2) and (1, 0))
#Minute 3: [[2,2,2],[2,2,0],[0  ,2,1]] (the rotten oranges at (0, 0), (0, 1), and (0, 2) rot the adjacent fresh orange at (1, 1))
#Minute 4: [[2,2,2],[2,2,0],[0  ,2,2]] (the rotten orange at (1, 1) rots the adjacent fresh orange at (2, 1))
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rLen = len(grid)
        cLen = len(grid[0])
        que = deque()
        fresh = 0
        
       

        for row in range(rLen):
            for col in range(cLen):
                if grid[row][col] == 2:
                    que.append((row,col))
                elif grid[row][col] == 1:
                    fresh +=1
                

        if fresh == 0:
            return 0
        
        minutes = 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while que:
            size = len(que)
            for _ in range(size):
                r,c = que.popleft()
            
                for rcol,ccol in directions:
                    rd = rcol + r
                    cd = c + ccol
                    if 0 <= rd < rLen and 0 <= cd < cLen and grid[rd][cd] == 1:
                        grid[rd][cd] = 2
                        que.append((rd,cd))
                        fresh -=1
            minutes +=1
        
        return minutes - 1 if fresh == 0 else -1

        
#** sliding window sub array sum equal to k 560 ******************
#input: nums = [1,1,1], k = 2
#output: 2 (the subarrays [1,1] at indices (0,1) and (1,2) sum to 2)
arr = [5, 2, 3, 4]
target = 7

def find_subarrays(nums, k):
    curr_sum = 0
    start = 0
    results = []
    
    for end in range(len(nums)):
        curr_sum += nums[end]
        
        # Shrink the window if the sum is too large
        while curr_sum > k and start <= end:
            curr_sum -= nums[start]
            start += 1
            
        # Check if we hit the target
        if curr_sum == k:
            results.append(nums[start:end+1])
            
    return results

print(find_subarrays(arr, target))

#********* Remove adjacent duplicates 1047 ******************
#input: s = "abbaca"
#output: "ca" (the first 'b' and the second 'b' are adjacent and can be removed, leaving "aaca". 
#Then, the first 'a' and the second 'a' are adjacent and can be removed, leaving "ca")
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
                

            
           
        return "".join(stack)

#********* Contiguous Array 525 ******************
#input: nums = [0,1,0]
#output: 2 (the longest contiguous subarray with equal number of 0 and 1 is [0,1] or [1,0], both of which have length 2)
#input 2: nums = [0,1,0,1,1,1]
#output 2: 4 (the longest contiguous subarray with equal number of 0 and 1 is [0,1,0,1], which has length 4)
#because we can treat 0 as -1, then the problem reduces to finding the longest subarray with sum 0. We can use a hash map to store 
#the cumulative sum and its earliest index. Whenever we encounter the same cumulative sum again, it means the subarray between 
#those two indices has a sum of 0, and we can update our maximum length accordingly.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        hp = {0: -1}
        sum_ele = 0
        max_len =float('-inf')
        for i in range(len(nums)):
            sum_ele += nums[i]
            if sum_ele in hp:
                max_len = max(max_len,i-hp[sum_ele])
            
            else:
                hp[sum_ele] = i
        return max_len


#**** Product of Array Except Self 238 ******************
#input: nums = [1,2,3,4]
#output: [24,12,8,6] (the product of all the elements except the current one for each index is [2*3*4, 1*3*4, 1*2*4, 1*2*3])

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [] #[1, 1*2, 1*2*3, 1*2*3*4]
        sufix = []#[2*3*4, 3*4, 4, 1]
        
        curr_p = 1
        suf_p =1
        for i in range(len(nums)):
            prefix.append(curr_p)
            curr_p *= nums[i]
            
        for j in range(len(nums)-1,-1,-1):
            sufix.insert(0,suf_p)
            suf_p *= nums[j]
        for i in range(len(nums)):
            nums[i] = prefix[i] * sufix[i]
            
            
        return nums
#********* Maximum Product Subarray 152 ******************
#input: nums = [2,3,-2,4]
#output: 6 (the contiguous subarray [2,3] has the largest product 6)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        
        max_product = float('-inf')
        pre =1
        sufix = 1

        for right in range(len(nums)):
            pre *= nums[right]
            sufix =sufix * nums[len(nums)-right-1] 
            max_product = max(max_product,pre,sufix)
            if pre ==0:
                pre =1
            if sufix == 0:
                sufix = 1
            
            
            
        return max_product 
#**** Sort Characters By Frequency 451 ******************
#input: s = "tree"
#output: "eert" (the characters 'e' appear twice and are sorted before 'r' and 't', which appear once each)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hp = {}
        res = ""
        for i,val in enumerate(s):
            if val in hp:
                hp[val] += 1
            else:
                hp[val] = 1
        hp = sorted(hp.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(len(hp)):
            char = hp[i][0]
            freq = int(hp[i][1])
            for j in range(freq):
                res += char
        return res
#********* Validate Stack Sequences 946 ******************
#input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
#output: true (we can simulate the push and pop operations as follows:+

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j =0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        if stack == []:
            return True
        else:
            return False

#Two Sum 1  problem******************
#input: nums = [2,7,11,15], target = 9  
#output: [0,1] (because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1])
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    

        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]
    
            if diff in mp:
                return ([mp[diff], i])
                break
    
            mp[nums[i]] = i
        
        

        

        
            
        
        

        
    
        
        

        
                    
        

        


        



        


        
    
        


        
