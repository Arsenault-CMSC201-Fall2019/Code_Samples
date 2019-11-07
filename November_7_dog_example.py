with open("Doug.txt", "r") as f:
    data = f.read()
    print(data)

    #now, split the file on whitespace so that
    #we can identify words
    words = data.split()
    print(words)

    #Next we go through the list of words
    #looking for the word "dog". If we find
    #it we replace it with "cat". If the word is
    #not dog, we do nothing
    for i in range(len(words)):
        if words[i] == 'dog':
            words[i] = 'cat'

    #let's see what we've done
    print(words)

# we're done with the file, so we need to close it
# Using the with statement, that happens automatically
# when we unindent


# Next, let's write the result to a file
# instead of to the screen

s = ' '
data = s.join(words)
with open("results.txt", "w") as outfile:
    outfile.write(data)
