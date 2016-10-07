def r(a,b):
     A = ord(a)
     B = ord(b)
     C = B - A
     list1 = []
     print(A)
     list1.append(chr(A))
     for i in range(C):
       A=A+1
       print(A)
       list1.append(chr(A))
     return list1
