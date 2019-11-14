#print all permutations of a string without repeats
def permute(prev_str, str):
    if len(str)==0:
        print(prev_str)
    else:
        for i in range(len(str)):
            permute(prev_str + str[i],str[:i] + str[i+1:])

permute ("", "abcdefg")


#Euclid's algorithm for finding the Greatest Common
#Divisor between two integers

def GCD (a,b):
    print ("a = ", a, "b = ", b)
    if b == 0:
        return a
    else:
        return GCD (b, a%b)

print (GCD(100,99))
