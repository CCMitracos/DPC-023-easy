# DPC 023 [E]
# List Splitter

L = [1,2,3,4,5,6,7,8,9]

def Lsplit(L):
  x = len(L)/2
  return [L[:x], L[x:]]
  
print Lsplit(L)
