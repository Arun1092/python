word=str(input("enter the word:"))
print("the original string is :"+word)
print("the vowel are:",end="")
for i in word:
    if i in "aeiouAEIOU":
        print([i],end="")