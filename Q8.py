#Remove vowels from words

def removeVowels(w):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    newString = ""
    for i in w: 
        if i not in vowels: #remove the non-vowels from string
            newString = newString+i
    w = newString
    return w

w = str(input('Enter word: '))
print(removeVowels(w))
