class search():
    #binary search   o(logn) 
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
    
obj = search()
obj.binarySearch([11,88,44,77,100],77)