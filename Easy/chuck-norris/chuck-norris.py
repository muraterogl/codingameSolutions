import re
numbers = re.findall('(0+|1+)', ''.join(format(ord(c), 'b').zfill(7) for c in input()))
for i in range(len(numbers)):
    print(("0 " if numbers[i][0]=="1" else "00 ") + "0"*len(numbers[i]), end=" " if i < len(numbers)-1 else "")
print("") 
