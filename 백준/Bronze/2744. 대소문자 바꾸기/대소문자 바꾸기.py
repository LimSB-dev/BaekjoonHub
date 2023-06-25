import sys
input = sys.stdin.readline

string = input()
new_string = ''

for alpha in string:
    if alpha.isupper():
        new_string += alpha.lower()
    else:
        new_string += alpha.upper()

print(new_string)