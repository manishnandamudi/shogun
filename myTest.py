class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            return (nums1[n//2] + nums1[n//2 - 1]) / 2
        else:
            return nums1[n//2]
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range (n):
            for j in range (i+1,n):
                result=nums[i]+nums[j]
                if result == target:
                    return (i,j)
                else:
                    continue
    def isPalindrome(self, s):
        # Run loop from 0 to len/2
        for i in range(0, int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def factorial(self, i):
        fact = 1
        for number in range(1, i+1):
            fact = fact * number
        return fact

    def fact_recursive(self, i):
        if i == 1:
            return 1
        else:
            return i * self.fact_recursive(i-1)
        
    def swap(num1, num2):

        print(f"Before swapping: num1 = {num1}, num2 = {num2}")
        temp = num1
        num1 = num2
        num2 = temp
        print(f"After swapping: num1 = {num1}, num2 = {num2}")
        return num1, num2
    
    def primeNumber(self,n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    print(f"{n} is not a prime number")
                    break
            else:
                print(f"{n} is a prime number")
                
    def prime(self,n):
     count =0
     if n >1:
        for i in range(1,n+1):
             if (n%i)==0:
                count+=1
        if count==2:
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")
                
                    


solution = Solution()
#leetcode problem Median of Two Sorted Arrays
nums1 = [1, 2]
nums2 = [3,5]
result = solution.findMedianSortedArrays(nums1, nums2)



#leetcode problem Two Sum
nums = [2,7,11,15]
target = 26
result = solution.twoSum(nums, target)

#check prime number
result = solution.prime(5)

# test palindrome method
s = "malayalam"
ans = solution.isPalindrome(s)
if ans:
    print("Yes its a pallindrome")
else:
    print("No")

# test factorial method
num = 0
fact = solution.factorial(num)
print(f"The factorial of {num} is {fact}")

# test recursive factorial method
num = 88
fact = solution.fact_recursive(num)
print(f"The factorial of {num} is {fact}")

#take input from user

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

sol,sol1 = Solution.swap(num1, num2)