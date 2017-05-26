import sys, os

cd = os.path.abspath(os.path.dirname(__file__))
pd = os.path.abspath(os.path.join(cd, os.pardir))
ppd = os.path.abspath(os.path.join(pd,os.pardir))

sys.path.append(ppd)
from N_test.oreilly.ch02.and_gate import AND

print(str(AND(1,0)))
