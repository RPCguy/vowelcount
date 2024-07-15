sentance = input("Enter a senrtence: ").lower()
vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}
for letter in sentance:
    if letter in vowels:
        vowels[letter] += 1

print(vowels)