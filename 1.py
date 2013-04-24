## takes and integer as inputs
## converts the integer to its binary represenation
## converts the binary number to it's complement (e.g. 010 -> 101)
## converts the binary complement back to an integer
## and returns the integer value

def getIntegerComplement(n):
    ## dictionary to invert binary string
    bin_invert = {"1":"0","0":"1"} 
    
    ## convert the integer to a binary
    n_bin = bin(n)[2:]

    print bin(n)[2:]
    print n_bin

    ## reverse each binary and concatenate
    output = "".join(map(lambda x: bin_invert[x] , list(n_bin))) 

    print output

    return int(output,2)
    

def test():
    print getIntegerComplement(50)
    print getIntegerComplement(100)
    
        
        
