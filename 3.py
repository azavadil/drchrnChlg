## the objective is to find the length of the longest substring where the sum of the
## of the digits on the right half of the substring equals the sum of the digits on the left half. 
## for test case 1 the answer is a length of 6  
## 123 (sum of 6, length of 3) 
## 231 (sum of 6, length of 3)
## "(123)(231)"
## for test case 2, the answer is length of 36 
## 656151741692121755 (sum of 74, length 18)
## 139511285921925731 (sum of 74, length 18)
## "98(656151741692121755)(139511285921925731)2"

def f(s):
    def aux(low,mid,high,max_string):
        if(low < 0 or high > len(s)):
           return max_string
        else:
           sum_head = sum([int(x) for x in s[low:mid]])
           sum_tail = sum([int(x) for x in s[mid:high]])
           
           if (sum_head == sum_tail and len(s[low:mid]) > len(max_string)):
               max_string = s[low:mid]
           return aux(low-1,mid,high+1, max_string)

    return 2*max([len(aux(x,x+1,x+2,'')) for x in xrange(len(s))])


def test():
    print f("123231")
  
    print f("986561517416921217551395112859219257312")

           
                         
