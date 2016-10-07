def r(a,b):
     A = ord(a) # writes integer equvalent of a
     B = ord(b) # writes integer equvalent of b
     C = B - A
     list1 = []
     #print(A) # this is for testing  
     list1.append(chr(A))
     for i in range(C):
       A=A+1
       #print(A)
       list1.append(chr(A))
     return list1
