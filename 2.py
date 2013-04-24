## The objective is to return the number of interations
## required to reduce the  digits of a number. 
## e.g.
## 99: 9*9 = 81
## 81: 8*1 = 8 (single digit in 2 iterations)
##
## 1137638137: 1*1*3*7*6*3*8*1*3*7 = 84672
## 84672: 8*4*6*7*2 = 2688
## 268: 2*6*8*8 = 768
## 336: 3*3*6 = 54
## 54: 5*4 = 20
## 20: 2*0 = 0 (single digit in 7 iterations)

def f(n):
    def aux(n, acc):
        ## if n is 1 digit, return the accumulator
        if (len(str(n)) == 1):
            return acc
        else:
            ## convert to list of integers
            temp = map(lambda x: int(x), list(str(n)))
            ## foldleft
            temp = reduce(lambda x,y: x*y, temp, 1)
            return aux(temp, acc + 1)

    return aux(n,0)
    
def test():
    print f(99)
    print f(1137638147)
        
