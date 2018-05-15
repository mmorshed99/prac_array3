#Given a list of non negative integers, arrange them such that they form the largest number.
#
#For example:
#
#Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
#Note: The result may be very large, so you need to return a string instead of an integer.
def large_seq(a0,a1):
     b0 = str(a0)
     b1 = str(a1)
     b01 = b0 + b1
     b10 = b1 + b0
     c01 = int(b01)
     c10 = int(b10)
     if c10 > c01:
       return a1
     else:
       return a0

def merge_sort(A):
   new_A = []
   if len(A) == 1:
     return A
   elif len(A) == 2:
     temp_val = large_seq(A[0],A[1]) 
     if temp_val == A[1]:
       new_A.append(A[1])
       new_A.append(A[0])
     else:
       new_A = A
     return new_A
   else:     
     A_left = merge_sort(A[0:(len(A)//2)])
     A_right = merge_sort(A[len(A)//2:len(A)])
     curr_index_left = 0
     curr_index_right = 0
     while(True):
           temp_val = large_seq(A_left[curr_index_left],A_right[curr_index_right])
           if temp_val == A_left[curr_index_left] :
             new_A.append(A_left[curr_index_left])
             curr_index_left += 1
           else:
             new_A.append(A_right[curr_index_right])
             curr_index_right += 1
           if curr_index_left == len(A_left) and curr_index_right == len(A_right):
             break
           if curr_index_left == len(A_left):
             for i in range(curr_index_right,len(A_right)):
               new_A.append(A_right[i])
             break
           if curr_index_right == len(A_right):
             for i in range(curr_index_left,len(A_left)):
               new_A.append(A_left[i])
             break
     return new_A 
#A = [5,1,6,9,10,4,2,1,4]
#A = [3, 30, 34, 5, 9]
A = [13, 33, 6, 39, 5, 2, 1]
#A = [0]
print(A)
list1=(merge_sort(A))
test_zero = 1
for i in range(0, len(list1)):
     if list1[i] != 0:
        test_zero = 0
if test_zero:
        print(0)
else:
  str1 = ''.join(str(e) for e in list1)             
  print(str1)
### bit more compact ###
def largestNumber(self, A):
        def mysort(A):
            if len(A) == 1:
                return [A[0]]
            if len(A) == 2:
                temp1 = str(A[0]) + str(A[1])
                temp2 = str(A[1]) + str(A[0])
                if int(temp1) > int(temp2):
                    return [A[0],A[1]]
                else:
                    return [A[1],A[0]]
            A_left = mysort(A[:len(A)//2])
            A_rgt  = mysort(A[len(A)//2:])
            i = 0
            j = 0
            temp = []
            while(i < len(A_left) and j < len(A_rgt)):
                if int(str(A_left[i])+str(A_rgt[j]))>int(str(A_rgt[j]) + str(A_left[i])):
                    temp.append(A_left[i])
                    i += 1
                else:
                    temp.append(A_rgt[j])
                    j += 1
                if i == len(A_left):
                    temp.extend(A_rgt[j:])
                    break
                if j == len(A_rgt):
                    temp.extend(A_left[i:])
                    break
            return temp
        #myA = []
        #for i in A:
        #    myA.append(i)
        mytemp = mysort(A)
        i = 0
        while(i < len(mytemp)-1 and mytemp[i] == 0):
            i += 1
        mytemp = mytemp[i:]
        return ''.join(str(x) for x in mytemp)
