class sorting :
    #0(n)
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
    
    #0(n)
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
    
    
    #0(log(n)) complexity
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
    
    #0(log(n)) complexity
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

obj = sorting()

arr = [26,16,22,44,8,9]
#obj.bubbleSort(arr)
#obj.selectionSort(arr)

val = obj.quickSort(arr)
a = val