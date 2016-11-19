#Reverse words in a sentence

def reverseSentence(s):
  x = s.split() #splits sentence
  result = [] #blank results list 
  for word in x: #loops through words
    result.insert(0,word) #inserts words at start of results list
  return " ".join(result) #joins words back together

s = str(input('Enter sentence: '))
print(reverseSentence(s))
