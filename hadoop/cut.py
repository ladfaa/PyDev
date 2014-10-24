f = open('links-converted.txt')
fout = open('file01', 'w')
k = 0
for line in f:
    if k == 1000:break;
    k = k + 1
    fout.write(line)
f.close()
fout.close()