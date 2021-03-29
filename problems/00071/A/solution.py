N = int(input())

for i in range(N):
    word = input()
    length = len(word)
    if length>10:
        print(word[0]+str(length-2)+word[-1])
    else:
        print(word)