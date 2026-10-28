word = input("Enter a word: ")
vowel = ['a', 'e', 'i', 'o', 'u']
list = []
for x in word:
    if x in vowel and x not in list:
        list.append(x)
print("vowel present in given word is",list)