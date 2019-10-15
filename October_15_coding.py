# Coding samples for October 15
#
#
#  First the function definition
def reverse_word (word):

    i = 0;
    reversed_word = ''
    while i < len(word):
        reversed_word = word[i] + reversed_word
        i += 1
    print("The word ", word, "reversed is ", reversed_word)
# now the code. DON’T FORGET TO INDENT!!



animals = ["dog", "cat", "platypus", "ocelot"]
for critter in animals:
	reverse_word(critter)


#
# Next example
#
# A function to calculate a student discount price
# You get a discount off the list price of a book. But you have to
# pay sales tax on the full list price
def discount_price (list_price, discount_rate, tax_rate):
    amount_off = discount_rate * list_price
    price_paid = list_price * (1 + tax_rate) - amount_off
    print("Your final price is ", price_paid)

#now we’ll try calling with different parameter orders
list_price = 100.00
discount_rate = 0.2 # 20 percent off
tax_rate = 0.06       # 6 percent sales tax
discount_price(list_price, discount_rate, tax_rate)
discount_price (discount_rate, tax_rate, list_price)
discount_price (tax_rate, discount_rate, list_price)

# Now we'll write a function to calculate the
# fourth root of a number, use a
# return statement, rather than having the function
# simply print out the result
# the fourth root of a number is equal to the number
# raised to the 1/4 power
def fourth_root(num):
	ans = num**(1/4)
	return (ans)

#set the variable’s value, then call the function
original_number = 81
final_number = fourth_root(original_number)
print(final_number)



#  Now we'll rewrite the "reverse_word"
# function using a return statement
#
def reverse_word (word):

    i = 0;
    reversed_word = ''
    while i < len(word):
        reversed_word = word[i] + reversed_word
        i += 1
    return(reversed_word)
# now the code. DON’T FORGET TO INDENT!!


# Now the call is
animals = ["cat", "Australian cattle dog", "duckbilled platypus", "ocelot", "zebra"]
for critter in animals:
    r_word = reverse_word(critter)
    print("The word ", critter, "reversed is ", r_word)
# now do whatever you want to with the
# reversed word in the main program

#program control example

# raised to the 1/4 power
def fourth_root(num):
    ans = num**(1/4)
    return (ans)
    print("This line will not be executed")

#set the variable’s value, then call the function
original_number = 81
final_number = fourth_root(original_number)
print(final_number)

# Now some examples of using the
# special value None and type NoneType
# Function definition

def fourth_root(num):
    if num >= 0:
        ans = num**(1/4)
        return (ans)
    else:
        return None
# we could have also said
#		return
# or just omitted the entire else: clause and
# have no return statement at all. The code
# works the same

# get the original value from the user
# then call the function
original_number = float(input("enter a number"))
done = False
while not(done):
    final_number = fourth_root(original_number)
    if final_number != None:
        print("The fourth root of", original_number, end = '')
        print(" is ", final_number)
        done = True
    else:
        original_number = float(input("we were serious about needing a non-negative number"))
