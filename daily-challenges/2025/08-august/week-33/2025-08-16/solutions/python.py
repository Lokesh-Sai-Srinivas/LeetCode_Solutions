class Solution(object):
    def maximum69Number (self, num):
        

        temp = str(num)
        temp = temp.replace('6','9',1)
        
        return int(temp)