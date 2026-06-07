text=input("Enter your string:")
words=text.split()

print(words)

counts={}

for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)

for word,counts in counts.items():
    print(f"{word} appears {counts} times")