class sorting :
    #0(n2)
    def bubbleSort(self,my_array):
        n = len(my_array)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if my_array[j] > my_array[j+1]:
                    my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                    swapped = True
            if not swapped:
                break

        print("Sorted array:", my_array)
        return my_array
    
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
    
    def insertionSort(self,my_array):
        n = len(my_array)
        for i in range(1,n):
            insert_index = i
            current_value = my_array[i]
            for j in range(i-1, -1, -1):
                if my_array[j] > current_value:     
                    my_array[j+1] = my_array[j]
                    insert_index = j
                else:
                    break
            my_array[insert_index] = current_value

        print("Sorted array:", my_array)
    
    
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
        #return self.quickSort(items_lower + [pivot] + items_greater)
        
    #0(log(n)) complexity
    #merge sort 
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        l=self.merge_sort(left_arr)
        r=self.merge_sort(right_arr)
        
        return self.merge(l,r)

    def merge(self,left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

obj = sorting()

arr = [26,16,22,44,8,1]
#obj.insertionSort(arr)
#obj.bubbleSort(arr)
#obj.selectionSort(arr)
j=obj.merge_sort(arr)
val = obj.quickSort(arr)
a = val