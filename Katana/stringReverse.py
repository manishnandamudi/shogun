class stringReverse:   
     
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
    
obj = stringReverse()
obj.reversecallusingPointer("rahul ll")
obj.reversecallusingPointer("like this")