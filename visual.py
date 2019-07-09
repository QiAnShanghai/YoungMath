
def print_tex(a,l):
    f = open("visual.tex","w")
    
    def ltx(s):
        f.write(s+"\n")
    x0 = 0
    y0 = 0
    def node(x,y,a):
        x = x*l
        y = -y*l
        ltx("\\draw [ultra thick] ("+str(x0+x-l/2)+","+str(y0+y-l/2)+") rectangle ("+str(x0+x+l/2)+","+str(y0+y+l/2)+");")
        ltx("\\node at ($("+str(x0+x)+","+str(y0+y)+")$) {$"+str(a)+"$};")

    ltx("\\documentclass{article}")
    ltx("\\usepackage{tikz}")
    ltx("\\usetikzlibrary{calc}")

    ltx("\\begin{document}\\begin{figure}")
    ltx("\t\\tikzset{")
    ltx("\t\ttick/.style = {black, very thick}")
    ltx("\t}")

    ltx("\\begin{tikzpicture} % boxlength=1")

    for i in range(len(a)):
        for j in range(len(a[i])):
            node(j,i,a[i][j])

    ltx("\\end{tikzpicture}")
    ltx("\\end{figure}")
    ltx("\\end{document}")

    f.close()

