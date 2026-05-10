

# 1593. Split a String Into the Max Number of Unique Substrings
#INPUT: nums = [1,2,1,2,1], k = 2
#OUTPUT: 8
#EXPLANATION: One optimal way to split nums into unique substrings is: [1], [2,1], [2,1]. 
#The cost of this split is 3 (for the first substring) + 4 (for the second substring) + 4 (for the third substring) + 2 (for k) = 8. 
#It can be shown that 8 is the minimum cost possible.
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
        