import sys
sys.stdout = open('output.txt','w')
sys.stdin = open('input.txt','r')

def add(a,b):
    print(a+b)
a=int(input())
b=int(input())
add(a,b)