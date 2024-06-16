sentence=input("Enter a sentence: ").lower()
reversed_sentance=[]
x=0
for i in sentence:
  x=x-1
  reversed_sentance.append(sentence[x])
  
palindrome=("").join(reversed_sentance)
if sentence==palindrome:
  print(f"{sentence} is a palindrome")
else:
  print(f"{sentence} is not a palindrome")
