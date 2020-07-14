a, c = map(int, input().split()) #step, mode
abc = list("abcdefghijklmnoprstuvwxyz")
inp = input()
b = ""
if c == 0: #encryption
    for i in list(inp):
        b += (abc[abc.index(i) + a])
    print(b)
elif c == -1: #decryption
    for i in list(inp):
        b += (abc[abc.index(i) - a])
    print(b)