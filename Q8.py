#Remove vowels from words

def removeVowels(w):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if not w: #if not string
        return w
    elif w[0] in vowels: #checks first letter of word
        return removeVowels(w[1:]) #checks remaining letter in word
    else:
        return w[0] + removeVowels(w[1:]) #checks whole word 

w = str(input('Enter word: '))
print(removeVowels(w))
