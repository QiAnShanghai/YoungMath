def s_to_v(S):
    
    v = []

    T = ['0','1','2','3','4','5','6','7','8','9',' ']

    for s in S:
        if not (s in T):
            raise ValueError("no young tableau")

    i = 0
    while 1:
        while i<len(S):
            if S[i]!=' ':
                break
            i+=1
        j = i
        while j<len(S):
            if S[j]==' ':
                break
            j+=1
        if i == j:
            break
        v.append(int(S[i:j]))
        i = j
    
    return v

def parse_word(v):
    if len(v)==0:
        return []
    if len(v)==1:
        return [[v]]

    a = [[]]
    a[0].append(v[0])
    i = 1
    k = 0
    while i < len(v):
        if v[i]>=v[i-1]:
            a[k].append(v[i])
        else:
            a.append([v[i]])
            k+=1
        i+=1
    b = []
    for i in range(len(a)):
        b.append(a[len(a)-i-1])
    for i in range(1,len(b)):
        if len(b[i]) > len(b[i-1]):
            raise ValueError("no young tableau")
        for j in range(len(b[i])):
            if b[i][j] <= b[i-1][j]:
                raise ValueError("no young tableau")
    return b

def parse(row,fl):
    f = open(fl,"r")
    for i in range(row):
        f.readline()
    s = f.readline()
    s = s[0:len(s)-1]
    return s_to_v(s)

