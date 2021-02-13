operation = input()
pseudo_random_number = int(input())
rotor =[input()for i in range(3)]
     
message = input()
m=[]
if operation=="ENCODE":
    m = list(message)
    for i,c in enumerate(m):
        r=(ord(c)+pseudo_random_number+i-65)%26+65
        m[i]=chr(r)
    for rot in rotor:
        m = [rot[ord(i)-65] for i in m]
else:
    m = list(message)
    for rot in reversed(rotor):
        m = [chr(rot.index(i)+65)for i in m]
    for i,c in enumerate(m):
        r=ord(c)-pseudo_random_number-i-65
        while r<0: r+=26
        m[i] = chr(r+65)
print("".join(m))
 
