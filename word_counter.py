fname = input('Enter a file name ')
oname = open(fname)
cnt = 0
for line in oname :
    line = line.rstrip()
    line = line.split()
    cnt = len(line) + cnt
print('The numbers of words you have in your file is: ',cnt)