# Function to remove a specific word from a list
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Rohan", "Shubham", "an"]

print(rem(l, "an"))