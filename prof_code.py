s1 = [4,8,2,7,1,9]
s2 = []
 
menor = min(s1)
s2.append(menor)
print(s2)
 
while len(s2) < len(s1):
  x=0
 
  while x < len(s1):
    if s1[x] == (menor + 1) :
        s2.append(s1[x])
        menor = s1[x]
        x = 0
    else :          
        x = x + 1
  menor = menor + 1  
       
print(s2)