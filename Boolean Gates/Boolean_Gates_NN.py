import math

#binary threshold logic signal function, to act as a TLN
def binary(x):
  if(x<=0):
    return 0
  else:
    return 1

#AND GATE FUNCTION
def find_and(x1,x2):
    #INITIALIZING MANUAL WEIGHTS
    w0= -1.5
    w1= 1
    w2= 1
    #BIAS FOR THE NEURON
    bias= 1* w0
    x1 = [i * w1 for i in x1]
    x2= [i * w2 for i in x2]
    q=[x1[i]+x2[i] for i in range(len(x1))]
    q = [i + bias for i in q]
    s = [binary(i) for i in q]
    return q,s

#OR GATE FUNCTION
def find_or(x1,x2):
    #INITIALIZING MANUAL WEIGHTS
    w0= -0.5
    w1= 1
    w2= 1
    #BIAS FOR THE NEURON
    bias= 1* w0
    x1 = [i * w1 for i in x1]
    x2= [i * w2 for i in x2]
    q=[x1[i]+x2[i] for i in range(len(x1))]
    q = [i + bias for i in q]
    s = [binary(i) for i in q]
    return q,s

#NAND GATE FUNCTION
def find_nand(x1,x2):
    #INITIALIZING MANUAL WEIGHTS
    w0= 1.5
    w1= -1
    w2= -1
    #BIAS FOR THE NEURON
    bias= 1* w0
    x1 = [i * w1 for i in x1]
    x2= [i * w2 for i in x2]
    q=[x1[i]+x2[i] for i in range(len(x1))]
    q = [i + bias for i in q]
    s = [binary(i) for i in q]
    return q,s

#NOR GATE FUNCTION
def find_nor(x1,x2):
    #INITIALIZING MANUAL WEIGHTS
    w0= 0.5
    w1= -1
    w2= -1
    #BIAS FOR THE NEURON
    bias= 1* w0
    x1 = [i * w1 for i in x1]
    x2= [i * w2 for i in x2]
    q=[x1[i]+x2[i] for i in range(len(x1))]
    q = [i + bias for i in q]
    s = [binary(i) for i in q]
    return q,s

#NOT GATE FUNCTION
def find_not(nx1):
    #INITIALIZING MANUAL WEIGHTS
    w0=1
    w1=-1
    #BIAS FOR THE NEURON
    bias = 1*w0
    nx1 = [i * w1 for i in nx1]
    q = [i + bias for i in nx1]
    s =[binary(i) for i in q]
    return q,s

#XOR GATE FUNCTION
def find_xor(x1,x2):
    q1,s1 = find_or(x1,x2)
    q2,s2 = find_nand(x1,x2)
    final_q,final_s = find_and(s1,s2)
    return final_q,final_s

#XNOR GATE FUNCTION
def find_xnor(x1,x2):
    q1,s1 = find_xor(x1,x2)
    final_q,final_s = find_not(s1)
    return final_q,final_s

nx1=[0,1]
q,s= find_not(nx1)
print("The output for NOT GATE is: ")
print()
print('x1',end="  ")
print('q',end="   ")
print('s')
print()
for i in range(len(nx1)):
    print(nx1[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
x1=[0,0,1,1]
x2=[0,1,0,1]
q,s= find_and(x1,x2)
print("The output for AND GATE is: ")
print()
print('x1',end="  ")
print('x2',end="   ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="   ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
q,s= find_or(x1,x2)
print("The output for OR GATE is: ")
print()
print('x1',end=" ")
print('x2',end="  ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="  ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
q,s = find_nand(x1,x2)
print("The output for NAND GATE is: ")
print()
print('x1',end=" ")
print('x2',end="  ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="  ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
q,s= find_nor(x1,x2)
print("The output for NOR GATE is: ")
print()
print('x1',end=" ")
print('x2',end="  ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="  ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
q,s= find_xor(x1,x2)
print("The output for XOR GATE is: ")
print()
print('x1',end=" ")
print('x2',end="  ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="  ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])
print()
q,s= find_xnor(x1,x2)
print("The output for XNOR GATE is: ")
print()
print('x1',end=" ")
print('x2',end="  ")
print('q',end="      ")
print('s')
print()
for i in range(len(x1)):
    print(x1[i],end="  ")
    print(x2[i],end="   ")
    print(q[i],end="   ")
    print(s[i])