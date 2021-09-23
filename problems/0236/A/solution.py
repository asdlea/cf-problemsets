word = input()

letters = {x for x in word}

if len(letters)%2 == 0:
    response = "CHAT WITH HER!"
else:
    response = "IGNORE HIM!"

print(response)