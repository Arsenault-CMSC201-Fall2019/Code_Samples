#coding for Tuesday, November 12
#list.extend()
first_list = [1,2,3,4]
second_list = [5,6,7,8]
first_list.extend(second_list)
print(first_list)

def factorial(number):
    if number == 1:
        return (1)
    else:
        return(number * factorial(number - 1))

if __name__ == "__main__":
    print(factorial(6))

def iterative_factorial(number):
    result = 1
    for i in range(1,number+1):
        result = result * i
    return (result)

if __name__ == "__main__":
    print(iterative_factorial(6))

def iterative_fibonacci (number):
    result = [1,1]
    for i in range(2,number+1):
        next_fib = result[i - 2] + result[i-1]
        result.append(next_fib)
    return(result[number])

def recursive_fibonacci(number):
    if number <= 1:
        return(1)
    else:
        return (recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2))


if __name__ == "__main__":
    print(iterative_fibonacci(8))
    print(recursive_fibonacci(8))

def iterative_palindrome(saying):
    palindrome = True
    i = 0
    while (palindrome) and i <= (len(saying)/2):
        if saying[i] != saying[-(i+1)]:
            palindrome = False
        i += 1
    return(palindrome)


def recursive_palindrome (saying):
    if len(saying) < 2:
        return(True)
    if saying[0] != saying[-1]:
        return(False)
    return(recursive_palindrome(saying[1:-1]))



if __name__ == "__main__":
    saying = "amanaplanacanalpanama"
    print(iterative_palindrome(saying))
    print(recursive_palindrome(saying))