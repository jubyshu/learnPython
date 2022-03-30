# s = r'xcopy /s c:\\ d:\\e'
s = r'l "b:\" /kzv /yar'

l = []
if '"' not in s:
    l = s.split(" ")
    print(len(l))
    for i in l:
        print(i)
else:
    l = s.split('"')
    left = l[0].split()
    right = l[-1].split()
    nl = left + l[1:-1] + right
    print(len(nl) - nl.count(' ') - nl.count(''))
    for i in nl:
        if i != '' and i != ' ':
            print(i)
