s = input("Enter a sentence: ").lower().split()
freq = {}
for word in s:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)
