C = input('Robot yo\'nalishini kiriting (N W E S): ')
N = int(input('Komandani kiriting: '))
if C == 'N':
    if N == 1:
        C = 'W'
    elif N == -1:
        C = 'E'
elif C == 'E':
    if N == 1:
        C = 'N'
    elif N == -1:
        C = 'S'
elif C == 'S':
    if N == 1:
        C = 'E'
    elif N == -1:
        C = 'W'
elif C == 'W':
    if N == 1:
        C = 'S'
    elif N == -1:
        C = 'N'
print(f'Yangi yo\'nalish: {C}')