# coding: 3 character ke tenathi vadhre hoy to first character ne last ma movu karvu ane 3 random character first and last ma append karva ane jo string 3 character thi nani hoy to string ne reverse karvi

str = input("Enter your message: ")
words = str.split()
coding = True

if coding :
    nwords =[]
    for wrd in words:
        if len(wrd) >=3:
            r1 = "dfg"
            r2 = "swa"
            strnew = r1 + wrd[1:] + wrd[0] + r2
            nwords.append(strnew)
        else:
            nwords.append(wrd[::-1])
    print(" ".join(nwords))

else:
    nwords =[]
    for wrd in words:
        if len(wrd) >=3 :
            strnew = wrd[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(wrd[::-1])
    print(" ".join(nwords))