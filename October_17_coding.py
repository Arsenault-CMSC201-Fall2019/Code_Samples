# Coding for Thursday, October 17
#
# Write the Error checking code
# Take in a number and make sure that it is a positive
# integer. If it isn't, print an appropriate error message
#
def err_check(number):
    if not(int(number) == number):
        print("sorry that is not an integer")
        return
    elif number <= 0:
        print("sorry that is not a positive integer")
        return
    else:
        return ("success")

# Now a function that calls err_check before
# calculating a factorial
def factorial(number):
    status = err_check(number)
    if status == None:
        return
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return (fact)

# main program
if __name__ == '__main__':
    product = factorial(5)
    print(product)

# Now a version with error checking inside the
# factorial function
def nested_factorial(number):
    def err_check(number):
        if not(int(number) == number):
            print("sorry that is not an integer")
            return
        elif number <= 0:
            print("sorry that is not a positive integer")
            return
        else:
            return ("success")

# Now the code for the rest of the nested_factorial
# function
    status = err_check(number)
    if status == None:
        return
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return (fact)

#def foo():
#    y = err_check(-3)
#    print(y)

# Now a main program for this part
if __name__ == '__main__':
#   foo()
    product = nested_factorial(5)
    print(product)
    x = err_check(5)
    if not(x== None):
        print(x)
    else:
        print ("None")


def recursive_fact(number):
    if number == 0:
        return 1
    else:
        return( number *recursive_fact(number-1))

print(recursive_fact(5))

# Illustrating variable scope and visibility
# if you have a variable in the main program
# you can see it in a function even if it wasn't
# passed in.
def square_a_num(number):
    print("x is", x)
    return (number * number)

if __name__ == "__main__":
    x = 92
    z = square_a_num(9)
    print ("9 squared is", z)

# but you can't do anything with that variable
# in the function or python will complain
# if you have a variable in the main program
# you can see it in a function even if it wasn't
# passed in.
def square_a_num(number):
    x = x*x
    return (number * number)

if __name__ == "__main__":
    x = 92
    z = square_a_num(9)
    print ("9 squared is", z)
