# Coding for Tuesday, October 22
#
#
# First an illustration of more "strangeness"
# in how Python handles variable copying
#
a = 1
b = a
b += a
print(a)

# that worked roughly the way we expected it to
# now how about this
c = [1,2,3,4]
d = c
d.append(5)
print(c)

## Now an illustration of mutable variables
# passed as parameters to a function
def strange_stuff (a_list):
    a_list.append(5)
    return

# This function doesn't return any value
# that's usable by the main program. So what
# will happen?
# a calling program
if __name__ == "__main__":
    main_list = [1,2,3,4]
    strange_stuff(main_list)
    print(main_list)

# a "safe" way to not mess up the parameter
def safe_strange_stuff (a_list):
    safe_list = list(a_list)
    safe_list.append(5)
    return

if __name__ == "__main__":
    main_list = [1,2,3,4]
    safe_strange_stuff(main_list)
    print(main_list)

## Creating a two-dimensional list to recreate
# a medal table
medal_table = [
    [1, 14, 11,4,29],
    [2,5,2,4,11],
    [3,3,5,4,12],
    [4,3,3,3,9],
    [5,2,5,1,8],
    [6,2,3,0,5],
    [7,2,0,4,6],
]
print (medal_table[0])

# define constants to help us keep track of which
# column means what
RANK = 0
GOLDS = 1
SILVERS = 2
BRONZES = 3
TOTAL = 4
golds_won = 0
for i in range(len(medal_table)):
    golds_won += medal_table[i][GOLDS]
print(golds_won)

#write a routine that fills a 2D table with the
#successive squares - 1, 4, 9, 16, 25,...
ROWS = 5
COLUMNS = 10
square_table = []  #create the initial blank table
num_to_be_squared = 1
for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        row.append(num_to_be_squared**2)
        num_to_be_squared += 1
    square_table.append(row)
print(square_table)

# How do I make that output look prettier?
# print out each row on a separate line
for k in range(ROWS):
    print(square_table[k])

# adding a column to our medal_table
# to put the "country" in
countries =["United States", "Kenya", "Jamaica", "China", "Ethiopia", "Great Britain", "Germany"]
for i in range(len(medal_table)):
    medal_table[i].insert(1, countries[i])

for k in range(len(medal_table)):
    print(medal_table[k])

# Now we need to update the constant definitions
# so that our previous code will still work
RANK = 0
COUNTRY = 1
GOLDS = 2
SILVERS = 3
BRONZES = 4
TOTALS = 5

golds_won = 0
for i in range(len(medal_table)):
    golds_won += medal_table[i][GOLDS]
print(golds_won)

# How many silver medals did China win?
#
for i in range(len(medal_table)):
    if medal_table[i][COUNTRY] =="China":
        print ("China won ", medal_table[i][SILVERS], "Silver medals")