input1 = input("Type a sentance  ").lower()
length = len(input1)
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
for i in range(length):
    if input1[i] == "a":
        c1 += 1
    elif input1[i] == "e":
        c2 += 1
    elif input1[i] == "i":
        c3 += 1
    elif input1[i] == "o":
        c4 += 1
    elif input1[i] == "u":
        c5 += 1 

print("A = ",c1)
print("E = ",c2)
print("I = ",c3)      
print("O = ",c4)        
print("U = ",c5)
