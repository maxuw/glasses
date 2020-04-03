import sys

def dupa():
    print("dupa")

lines = []
line2 = None



for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line)
    print(f'Processing Message from sys.stdin *****{line}*****')
    # dupa()

    if len(lines) > 1:
        dupa()
