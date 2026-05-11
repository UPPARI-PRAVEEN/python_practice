

# dupliate penalty 2567******************
#input: nums = [1,2,2,3], k = 2
#output: 4
#explanation: We can split nums into the two subarrays [1,2] and [2,3]. 
# The cost of the first subarray is 1 (no duplicates) and the cost of the second subarray is 3 
# (one duplicate 2). The total cost is 1 + 3 = 4. It can be shown that we cannot split nums into 
# subarrays such that the total cost is less than 4.
class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        dp = [float('inf')] * (l + 1)
        dp[l] = 0

        for i in range(len(nums)-1,-1,-1):
            hp = {}
            duplicates = 0
            for j in range(i,len(nums)):
                ch = nums[j]
                if ch in hp:
                    hp[ch] += 1
                else:
                    hp[ch] = 1
                
                if hp[ch] == 2:
                    duplicates +=2
                elif hp[ch] > 2:
                    duplicates += 1
                total_cost = duplicates + k
                dp[i] =min(dp[i],total_cost + dp[j+1])
        return dp[0]
#1105. Filling Bookcase Shelves
#INPUT: books = [[1,1],[2,3],[2,3],[1,1]], shelfWidth = 4
#OUTPUT: 6
#EXPLANATION: The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.

class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        l = len(books)
        dp = [float('inf')] * (l+1)
        dp[l] = 0

        for i in range(l-1,-1,-1):
            width = 0
            height = 0
            for j in range(i,l):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height,books[j][1])
                dp[i] = min(dp[i],height+dp[j+1])
        return dp[0]


#Non overlaping palindrom 2472******************

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isPalin(start,end):
            
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True
        l = len(s)
        dp = [0 for _ in range(l+1)]
        palinCount = 0

        for i in range(l-1,-1,-1):
            
            #skipping the curret index
            dp[i] = dp[i+1]

            #checking for k len
            if i + k -1 < l and isPalin(i,i+k-1):
                dp[i] = max(dp[i],1+dp[i+k])
            
            #checking for k+1 length
            if i + k  < l and isPalin(i,i+k):
                dp[i] = max(dp[i],1+dp[i+k+1])
        return dp[0]

#********* Partition Palindrome 131 ******************
#input: s = "aab"
#output: [["a","a","b"],["aa","b"]] (the palindrome partitioning of "aab" is [["a","a","b"],["aa","b"]], 
#where "a", "a", and "b" are palindromic substrings, and "aa" is also a palindromic substring)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalin(st,start,end):
            if len(st) == 1:
                return True
            
            while start < end:
                if st[start] != st[end]:
                    return False
                start +=1
                end -=1
            return True

        res = []

        def fn(s,index,res,nested):
            if index == len(s):
                res.append(nested[:])
                return
            
            for i in range(index,len(s)):
                if isPalin(s,index,i):
                    path.append(s[index:i+1])
                    fn(s,i+1,res,path)
                    path.pop()
        res = []
        path = []
        fn(s,0,res,path)
        return res


#680. Valid Palindrome II
#INPUT: s = "abca"
#OUTPUT: true
#EXPLANATION: You could delete the character 'c' to get a palindrome "aba", which is true.
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalin(start,end):
            
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:

                return isPalin(left +1,right) or isPalin(left,right-1)
            left +=1
            right -=1
        return True


            

        



        

        