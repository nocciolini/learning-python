name = str(input("Input your name: "))

frequencyTypedChars={}

for i in name.strip():
    if i in frequencyTypedChars.keys():
       frequencyTypedChars[i] += 1
    else:
       frequencyTypedChars[i] = 1
        
print(frequencyTypedChars)