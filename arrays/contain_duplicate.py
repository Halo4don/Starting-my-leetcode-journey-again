# LeetCode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
#
# Approach: Use a set to track numbers seen so far. If a number is already
# in the set, we've found a duplicate. A set is used instead of a dict since
# we only need membership checking, not key-value pairs.


My intial soluton was 

def containsDuplicate(self, nums):
       seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = 0
          
        return False

However, using a dict was a low level way of doing it as I don't need to keep track of the placeholder value 0. So instead I should have used a set.

So the better solution would have been

def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)

        return False

Using Set is cleaner since I just needed to know if I have seen this num before.
