from typing import List
class New:
#1 #Cumulative Sum - https://workat.tech/problem-solving/practice/cumulative-sum
    def getCumulativeSum(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            arr[i] = arr[i] + arr[i-1]
        print(arr)
        return arr
    
#2 #Positive Cumulative Sum - https://workat.tech/problem-solving/practice/positive-cumulative-sum   
    def getPositiveCumulativeSum(self, arr):
        result = []
        cumulative_sum = 0
        
        for num in arr:
            cumulative_sum += num
            result.append(cumulative_sum)
        
        return result
#3  #Identical Twins - https://workat.tech/problem-solving/practice/identical-twins
    def getIdenticalTwinsCounUsingMap(self, nums) -> int:
		# add your logic here
        count_map = {}
        twin_count = 0
        
        for num in nums:
            if num in count_map:
                twin_count += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1
        print(twin_count[key])
        return twin_count

    def getIdenticalTwinsCount(self, arr: List[int]) -> int:
        count = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    count +=1
        return count
#4 #Even Number of Digits - https://workat.tech/problem-solving/practice/even-number-of-digits
    def hasEvenNumberOfDigits(self, number: int) -> bool:
        digit_count = 0
        while number != 0:
            number //= 10
            digit_count += 1
        return digit_count % 2 == 0

    def getEvenNumberOfDigits(self, arr: List[int]):
        result = []
        val1 =[]
        count = 0 
        for val in arr:
            count = 0 
            val1 = val
             # Reset count for each number
            while val != 0:
                val //= 10
                count += 1
            if count % 2 == 0:
                result.append(val1)  # Append the original value, not the modified one
        return result


obj = New()
obj.getEvenNumberOfDigits([42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442])
obj.getIdenticalTwinsCount([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
obj.getCumulativeSum([1, 2, 3, 4, 5])
obj.getPositiveCumulativeSum([1, -2, 3, 4, -6])
