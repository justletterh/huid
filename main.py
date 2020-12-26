from utils import *
import consts

def to_fancy(l):
    return "{"+"-".join(list_str(l))+"}"

def to_bin(n=consts.default,*,pad=True):
    if n>consts.binmax:
        n=n%consts.binmax
    n=str(bin(n)).replace("0b","")
    if pad:
        n=f"{'0'*(consts.bl-len(n))}{n}"
    return n

def to_oct(n=consts.default,*,pad=True):
    if n>consts.octmax:
        n=n%consts.octmax
    n=str(oct(n)).replace("0o","")
    if pad:
        n=f"{'0'*(consts.bl-len(n))}{n}"
    return n

def to_dec(n=consts.default,*,pad=True):
    if n>consts.decmax:
        n=n%consts.decmax
    n=str(n)
    if pad:
        n=f"{'0'*(consts.bl-len(n))}{n}"
    return n

def to_hex(n=consts.default,*,pad=True):
    if n>consts.hexmax:
        n=n%consts.hexmax
    n=str(hex(n)).replace("0x","")
    if pad:
        n=f"{'0'*(consts.bl-len(n))}{n}"
    return n.upper()

def to_b26(n=consts.default,*,pad=True):
    if n>consts.b26max:
        n=n%consts.b26max
    n=to_digits(n,26)
    o=""
    for i in n:
        o+=consts.b26alpha[i]
    if pad:
        n=f"{consts.b26alpha[0]*(consts.bl-len(o))}{o}"
    return n.upper()

def to_b32(n=consts.default,*,pad=True):
    if n>consts.b32max:
        n=n%consts.b32max
    n=to_digits(n,32)
    o=""
    for i in n:
        o+=consts.b32alpha[i]
    if pad:
        n=f"{consts.b32alpha[0]*(consts.bl-len(o))}{o}"
    return n.upper()

def to_b64(n=consts.default,*,pad=True):
    if n>consts.b64max:
        n=n%consts.b64max
    n=to_digits(n,64)
    o=""
    for i in n:
        o+=consts.b64alpha[i]
    if pad:
        n=f"{consts.b64alpha[0]*(consts.bl-len(o))}{o}"
    return n

def to_b84(n=consts.default,*,pad=True):
    if n>consts.b84max:
        n=n%consts.b84max
    n=to_digits(n,84)
    o=""
    for i in n:
        o+=consts.b84alpha[i]
    if pad:
        n=f"{consts.b84alpha[0]*(consts.bl-len(o))}{o}"
    return n

def from_b26(s):
    o=[]
    for c in s:
        o.append(consts.b26alpha.find(c))
    return from_digits(o,26)

def from_b32(s):
    o=[]
    for c in s:
        o.append(consts.b32alpha.find(c))
    return from_digits(o,32)

def from_b64(s):
    o=[]
    for c in s:
        o.append(consts.b64alpha.find(c))
    return from_digits(o,64)

def from_b84(s):
    o=[]
    for c in s:
        o.append(consts.b84alpha.find(c))
    return from_digits(o,84)

def to_huid(x=[consts.binmax,consts.octmax,consts.decmax,consts.hexmax,consts.b26max,consts.b32max,consts.b64max,consts.b84max],*,fancy=True,rng=False):
    o=[]
    if x==None:
        x=dupe(None,8)
    try:
        if x[0]==None:
            x[0]=consts.binmax
        if x[1]==None:
            x[1]=consts.octmax
        if x[2]==None:
            x[2]=consts.decmax
        if x[3]==None:
            x[3]=consts.hexmax
        if x[4]==None:
            x[4]=consts.b26max
        if x[5]==None:
            x[5]=consts.b32max
        if x[6]==None:
            x[6]=consts.b64max
        if x[7]==None:
            x[7]=consts.b84max
    except IndexError:
        pass
    if rng:
        x=[randint(0,consts.binmax),randint(0,consts.octmax),randint(0,consts.decmax),randint(0,consts.hexmax),randint(0,consts.b26max),randint(0,consts.b32max),randint(0,consts.b64max),randint(0,consts.b84max)]
    try:
        o.append(to_bin(x[0]))
    except IndexError:
        o.append(to_bin())
    try:
        o.append(to_oct(x[1]))
    except IndexError:
        o.append(to_oct())
    try:
        o.append(x[2])
    except IndexError:
        o.append(consts.default)
    try:
        o.append(to_hex(x[3]))
    except IndexError:
        o.append(to_hex())
    try:
        o.append(to_b26(x[4]))
    except IndexError:
        o.append(to_b26())
    try:
        o.append(to_b32(x[5]))
    except IndexError:
        o.append(to_b32())
    try:
        o.append(to_b64(x[6]))
    except IndexError:
        o.append(to_b64())
    try:
        o.append(to_b84(x[7]))
    except IndexError:
        o.append(to_b84())
    if fancy:
        o=to_fancy(o)
    return o

def from_huid(s,*,fancy=True):
    if type(s)==str:
        s=s.replace("{","").replace("}","").split("-")
    s[0]=eval(f"0b{s[0]}")
    s[1]=eval(f"0o{s[1]}")
    s[2]=eval(s[2])
    s[3]=eval(f"0x{s[3]}")
    s[4]=from_b26(s[4])
    s[5]=from_b32(s[5])
    s[6]=from_b64(s[6])
    s[7]=from_b84(s[7])
    if fancy:
        s=to_fancy(s)
    return s

def main():
    res=to_huid(None,rng=True)
    print(f"{res}\n")
    print(from_huid(res))

if __name__=="__main__":
    main()