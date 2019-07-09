import words
import visual
class youngtableau(list):
    def __init__(self,word):
        A = words.parse_word(word)
        for a in A:
            self.append(a)

    def visual(self,l):
      visual.print_tex(self,l) 

    def row_insert(self,x):
        Y =youngtableau(self.word())
        def ins(i,x):
            if i>= len(Y):
                Y.append([x])
                return
            for j in range(len(Y[i])):
                if Y[i][j]>x:
                    y = Y[i][j]
                    Y[i][j] = x
                    ins(i+1,y)
                    return
            Y[i].append(x)

        ins(0,x)
        return Y

    def word(self):
        w = []
        for ii in range(len(self)):
            i = len(self) - 1 - ii
            for j in range(len(self[i])):
                    w.append(self[i][j])
        return w

def create_from(row,filename):
    return youngtableau(words.parse(row,filename))

def multiply(S,T):
    ans = youngtableau(S.word())
    W = T.word()
    for w in W:
        ans.row_insert(w)
    return ans

class word(list):
    def __init__(self,S):
        for s in S:
            self.append(s)

    def K1(self,i):
        ans = word(self)
        if i+2 >= len(self):
            raise ValueError("out of range")
        y = self[i]
        z = self[i+1]
        x = self[i+2]
        if x<y and y<=z:
            ans[i+1] = x
            ans[i+2] = z
        else:
            raise ValueError("K-operation impossible")
        return ans

    def K1_inv(self,i):
        ans = word(self)
        if i+2 >= len(self):
            raise ValueError("out of range")
        y = self[i]
        x = self[i+1]
        z = self[i+2]
        if x<y and y<=z:
            ans[i+1] = z
            ans[i+2] = x
        else:
            raise ValueError("K-operation impossible")
        return ans

    def K2(self,i):
        ans = word(self)
        if i+2 >= len(self):
            raise ValueError("out of range")
        x = self[i]
        z = self[i+1]
        y = self[i+2]
        if x<=y and y<z:
            ans[i] = z
            ans[i+1] = x
        else:
            raise ValueError("K-operation impossible")
        return ans
    
    def K2_inv(self,i):
        ans = word(self)
        if i+2 >= len(self):
            raise ValueError("out of range")
        z = self[i]
        x = self[i+1]
        y = self[i+2]
        if x<=y and y<z:
            ans[i] = z
            ans[i+1] = x
        else:
            raise ValueError("K-operation impossible")
        return ans

def pi_inv(word):
    Y = youngtableau([])
    for w in word:
        Y.row_insert(w)
    return Y.word()

def mult_classes(a,b):
    ans = word(a)
    for c in b:
        ans.append(c)
    return pi_inv(ans)

def are_equiv(a,b):
    A = pi_inv(a)
    B = pi_inv(b)
    return A == B


