import datetime as val
from collections import Counter,deque

class Solution:
    def __init__(self,val1,val2,val3):
        self.val1 =val1
        self.val2 =val2
        self.val3 =val3
        
        
    def removeElement(self, nums, val):
        # num = len(nums)
        # for i in range(num-1):
        #     if nums[i] == val:
        #         nums.pop(i)
        # print(nums)
        # return len(nums)
        nums = [1,1,2]
        val  =1 
        i =0 
        for x in nums:
            if x != val:
                nums[i] =x
                i +=1
        return i
    
    def removeDuplicates(self,nums):
        rel = []
        nums = [1,1,2]
        if len(nums) == 0:
            return 0
        index = 0
        temp = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        print(index)
        
        index1=1
        for i in range(1,len(nums)-1):
            for j in range(i+1,len(nums)-1):
                if nums[j] != nums[i]:
                    nums[index1] = nums[i]
                    index1 +=1
                    
        
        nums = [1,1,2]
        num_dict = {}
        result = []
        count = 0
        for num in nums:
            if num not in num_dict:
                result.append(num)
                num_dict[num] = True
                count +=1
        return result
            
        
                


        
        
        
    #leetcode88 
    #merge two List
    def mergeTwoLists1(self, a, b):
        merged = []
        i = j = 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        
        # Add remaining elements from list a, if any
        while i < len(a):
            merged.append(a[i])
            i += 1
        
        # Add remaining elements from list b, if any
        while j < len(b):
            merged.append(b[j])
            j += 1
        
        return merged
    
    #leetcode88 
    #merge two ListNode linkList
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
    
    
    #leetcode 88
    def mergeArray(self,nums1,m,nums2,n):
        i = m - 1
        j = n - 1
        # Start from the end of nums1 and nums2
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
        return nums1
        
        
        
        # newNum1 = nums1[:m]
        # newNum2 = nums2[:n]
        
        # new1 = newNum1 + newNum2
        # new1.sort()
        
        # return new1
        
    #leetcode 643
    def findMaxAverage(self,arr,k):
        sum = 0
        if len(arr)>1:
            for i in range(k):
                sum += arr[i]
            
            maxSum =sum
            
            firstIndex = 0
            endIndex = k
            while (endIndex < len(arr)):
                sum -=arr[firstIndex]
                firstIndex+=1
                
                sum+=arr[endIndex]
                endIndex+=1
                maxSum = max(maxSum,sum)
            result = maxSum/4     
            return maxSum/float(k)
        else:
            return arr[0]
            
            
            
    def checkSubstring(self,string1,string2):
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        freq_s1 = Counter(s1)
        freq_window = Counter(s2[:len_s1])

        if freq_s1 == freq_window:
            return True

        for i in range(len_s1, len_s2):
            char_out = s2[i - len_s1]
            if freq_window[char_out] == 1:
                del freq_window[char_out]
            else:
                freq_window[char_out] -= 1

            char_in = s2[i]
            freq_window[char_in] += 1

            if freq_s1 == freq_window:
                return True

        return False
        
    def reversecallusingPointer(self,input):
        char_array = list(input)
        start_index =0
        end_index = len(input)-1
        while(start_index<end_index):
            self.reverse_word(char_array,start_index,end_index)
            start_index =start_index+1
            end_index =end_index-1
        return "".join(char_array)

    def reverse_word(self,s, start, end):
            s[start], s[end] = s[end], s[start]
        
    def reverseUsingStack(self,stringInput):
        stack = []
        reserseStack = []
        for each in stringInput:
            stack.append(each)
        while len(stack) > 0:
            reserseStack.append(stack.pop())
        return "".join(reserseStack)
        
        
    def fibonacci(self, n):
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b   
        #recersive
        # if n <= 1:
        #     return n
        # result = self.fibonacci(n-1) + self.fibonacci(n-2)
        # return result
        
    def morethanNbyK(self,arr, n, k):
        x = n // k
    
        # unordered_map initialization
        freq = {}
    
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
    
        # Traversing the map
        for i in freq:
    
            # Checking if value of a key-value pair
            # is greater than x (where x=n/k)
            if (freq[i] > x):
    
                # Print the key of whose value
                # is greater than x
                print(i)    
        
        
    def bubbleSort(self,arr):
        index_len=len(arr)-1 #because we need to check the
        #next element in bubble sort so last element will never exist hence -1
        sorted=False
        
        while not sorted:
            sorted = True
            for i in range (0,index_len):
                if arr[i] > arr[i+1]:
                    sorted =False
                    arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
    #olog(n)
    def selectionSort(self,arr):
        for i in range(0,len(arr)):
            min =i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min]:
                   min = j
            temp =arr[i]
            arr[i] = arr[min]
            arr[min]=temp
        return arr
    
    
    #o(log(n)) complexity
    def quickSort(self,arr):
        length = len(arr)
        if length<=0:
            return arr
        else:
            pivot =arr.pop()

        items_lower =[]
        items_greater = []
        for val in arr:
            if (val >pivot):
                items_greater.append(val)
            else:
                items_lower.append(val)
        
        return self.quickSort(items_lower) + [pivot] + self.quickSort(items_greater)
    
    
    #merge sort
        
    def merge_sort(self,arr):
        if len(arr) > 1:
            # Divide the array into two halves
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            
            # Recursively sort the two halves
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            
            # Merge the sorted halves
            self.merge(arr, left_arr, right_arr)

    def merge(self,arr, left_arr, right_arr):
        i = j = k = 0
        
        # Merge the two sorted arrays
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Check if any elements were left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

            
            
            
                
    def binarySearch(self,num,target):
        l=0
        r=len(num)-1
        while(l<=r):
            mid = (l+r)//2
            if (num[mid]<target):
                l = mid +1
            elif(num[mid]>target):
                r = mid -1
            else:
                return mid
        return -1

                
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            val = (nums1[n//2] + nums1[n//2 - 1]) / 2
            return (nums1[n//2] + nums1[n//2 - 1]) / 2
        else:
            val1 = nums1[n//2]
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

    def pallindrome(self,num):
        temp=num
        reverse =0
        while (temp > 0):
            temp1 = temp % 10
            reverse = reverse * 10 +temp1
            temp = temp//10
        if reverse == num:
            return "isPallindrome"
        else:
            return "not a pallindrome"
        
    def palling_string(self,str1):
        # Check if the input is a string
        if not isinstance(str1,str):
            str1 = str(str1)
        
        rev = str1[::-1]
        if rev == str1:
            print(f"{rev} is pallindrome" )
        else:
            print(f"{rev} is not apallindrome")
            
    def pn(self,val):
        count =0
        if (val > 1):
            for i in range(1,val+1):
                if (val%i==0):
                    count+=1
            if count==2:
                print("prime value")
            else:
                print("not prime")
                
    def primeNumber(self,n):
        x = val.datetime.now()
        print(x)
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    print(f"{n} is not a prime number")
                    break
            else:
                print(f"{n} is a prime number")
                
                    
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
                
                    


solution = Solution(171,"malyalam",293)


solution.removeDuplicates([1,2,2,3,0,4,2])
solution.removeElement([1,2,2,3,0,4,2],2)

# bin =[3,9,20,"","",15,7]
# solution.binaryMaxDepth(bin)

# e=[1,2,4]
# f =[1,3,4]

# solution.mergeTwoLists(e,f)


a1 =[1,2,3,0,0,0]
a2 = [2,5,6]

res_mergeArray = solution.mergeArray(a1,3,a2,3)

# arr1 = [1]
# max_res = solution.findMaxAverage(arr1,4)


s1 = "ab"
s2 = "eidbaooo"
result = solution.checkSubstring(s1, s2)

# sRev = solution.reverseUsingStack("like this")

rev=solution.reversecallusingPointer("like this")

# val = solution.fibonacci(9)


# arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
# n = len(arr)
# k = 4
# solution.morethanNbyK(arr,n,k)

# #bubbleSort
#arr_b=[60,45,25,20,16,14,12,9]
#result_bubble=solution.bubbleSort(arr_b)


# #selection Sort
#arr1 =[2,7,8,1,6,10]
#result_ss = solution.selectionSort(arr1)

# # #quickSort
# arr1 =[4,9,3,6,2]
# result_ss = solution.quickSort(arr1)


# #mergeSort
# # Example usage:
# arr = [2,6,5,1,7,4,3]
# print("Original array:", arr)

# resoo =solution.merge_sort(arr)
# print("Sorted array:", arr)

# # #leetcode problem 704
# num = [1,2,5,9,10,44]
# target = 44
# res_bin = solution.binarySearch(num,target)


# # #leetcode problem Median of Two Sorted Arrays
#nums1 = [1, 2]
#nums2 = [3,5]
#result = solution.findMedianSortedArrays(nums1, nums2)



# # #leetcode problem Two Sum
nums = [2,7,11,15]
target = 26
result = solution.twoSum(nums, target)

# # #check prime number
# #val1 =solution.pn(23)
# #val = solution.pallindrome(171)
# result = solution.primeNumber(5)

# test palindrome method
# s = 707
# ans = solution.pallindrome(s)
# if ans:
#     print("Yes its a pallindrome")
# else:
#     print("No")

# sPallin = solution.palling_string(123)
# # test factorial method
# num = 4
# fact = solution.factorial(num)
# print(f"The factorial of {num} is {fact}")

# # test recursive factorial method
# num = 88
# fact = solution.fact_recursive(num)
# print(f"The factorial of {num} is {fact}")

# #take input from user

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# sol,sol1 = Solution.swap(num1, num2)