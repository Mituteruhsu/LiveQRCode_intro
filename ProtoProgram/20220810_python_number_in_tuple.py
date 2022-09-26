import numpy as np
import math
pyptx = (216, 0) # <class 'tuple'> 
# pyptx = (216, 72) # <class 'tuple'> 
cvptx = (215, 78) # <class 'tuple'> 
# ==========================================
# pypty = (514, 5) # <class 'tuple'> 
pypty = (517, 360) # <class 'tuple'> 
cvpty = (527, 359) # <class 'tuple'>
# ==========================================
pypts = [[[216, 72],[225, 360],[514, 344],[493, 80]]]  #<class 'numpy.ndarray'> 
cvpts = [[215, 71], [490, 78], [527, 347], [225, 359]] # <class 'numpy.ndarray'>
cvpts=[cvpts[0],cvpts[3],cvpts[2],cvpts[1]]
# ==========================================
# print(type(pypts), 'pypts: ', pypts)
print(type(cvpts), 'cvpts: ',  cvpts)
pypts=pypts[0]
print(type(pypts), 'pypts: ',  pypts)
# pts1
print('----------------pts1----------------')
pts1p = tuple(pypts[0])
pts1c = tuple(cvpts[0])
print(pts1p, pts1c)
pts1minu = sum(pts1p)-sum(pts1c)
print(pts1minu)
if pts1minu >= -10 and pts1minu <= 10:
    x=tuple(map(sum,zip(pts1p,pts1c)))
    a=[math.ceil(i/2) for i in x]
    pts1= tuple(map(int, a))
    print(type(pts1), 'pts1 do average', pts1)
elif pts1minu <= -10 or pts1minu >= 10:
    pts1=(max(pts1p[0],pts1c[0]), max(pts1p[1],pts1c[1]))
    print(type(pts1),'pts1 do max number:', pts1)
# pts2
print('----------------pts2----------------')
pts2p = tuple(pypts[1])
pts2c = tuple(cvpts[1])
print(pts2p, pts2c)
pts2minu = sum(pts2p)-sum(pts2c)
print(pts2minu)
if pts2minu >= -10 and pts2minu <= 10:
    x=tuple(map(sum,zip(pts2p,pts2c)))
    a=[math.ceil(i/2) for i in x]
    pts2= tuple(map(int, a))
    print(type(pts2), 'pts2 do average', pts2)
elif pts2minu <= -10 or pts2minu >= 10:
    pts2=(max(pts2p[0],pts2c[0]), max(pts2p[1],pts2c[1]))
    print(type(pts2),'pts2 do max number:', pts2)
# pts3
print('----------------pts3----------------')
pts3p = tuple(pypts[2])
pts3c = tuple(cvpts[2])
print(pts3p, pts3c)
pts3minu = sum(pts3p)-sum(pts3c)
print(pts3minu)
if pts3minu >= -10 and pts3minu <= 10:
    x=tuple(map(sum,zip(pts3p,pts3c)))
    a=[math.ceil(i/2) for i in x]
    pts3= tuple(map(int, a))
    print(type(pts3), 'ptx do average', pts3)
elif pts3minu <= -10 or pts3minu >= 10:
    pts3=(max(pts3p[0],pts3c[0]), max(pts3p[1],pts3c[1]))
    print(type(pts3),'ptx do max number:', pts3)
# pts4
print('----------------pts4----------------')
pts4p = tuple(pypts[3])
pts4c = tuple(cvpts[3])
print(pts4p, pts4c)
pts4minu = sum(pts4p)-sum(pts4c)
print(pts4minu)
if pts4minu >= -10 and pts4minu <= 10:
    x=tuple(map(sum,zip(pts4p,pts4c)))
    a=[math.ceil(i/2) for i in x]
    pts4= tuple(map(int, a))
    print(type(pts4), 'ptx do average', pts4)
elif pts4minu <= -10 or pts4minu >= 10:
    pts4=(max(pts4p[0],pts4c[0]), max(pts4p[1],pts4c[1]))
    print(type(pts4),'ptx do max number:', pts4)
pts=(pts1,pts2,pts3,pts4)
pts=[pts]
pts=np.array(pts, np.int32)
print(type(pts))
print(pts)



ptxmax=(max(pyptx[0],cvptx[0]), max(pyptx[1],cvptx[1]))
# print(type(pyptx), pyptx)
# print(type(cvptx), cvptx)
# print(sum(pyptx))
# print(sum(cvptx))
# print(sum(pyptx)-sum(cvptx))


# ptxminus = sum(pyptx)-sum(cvptx)
# # print(type(ptxminus), ptxminus)

# if ptxminus >= -10 and ptxminus <= 10:
#     x=tuple(map(sum,zip(pyptx,cvptx)))
#     a=[i/2 for i in x]
#     ptx= tuple(map(int, a))
#     print(type(ptx), 'ptx do average', ptx)
    
# elif ptxminus <= -10 or ptxminus >= 10:
#     ptx=(max(pyptx[0],cvptx[0]), max(pyptx[1],cvptx[1]))
#     print(type(ptx),'ptx do max number:', ptx)
# ptyminus = sum(pypty)-sum(cvpty)
# if ptyminus >= -10 and ptyminus <= 10:
#     x=tuple(map(sum,zip(pypty,cvpty)))
#     a=[i/2 for i in x]
#     pty= tuple(map(int, a))
#     print(type(pty), 'pty do average', pty)
    
# elif ptyminus <= -10 or ptyminus >= 10:
#     pty=(max(pypty[0],cvpty[0]), max(pypty[1],cvpty[1]))
#     print(type(pty),'pty do max number:', pty)

# finally:
#     print(type(ptx), 'ptx do average', ptx)
#     print(type(ptx),'ptx do max number:', ptx)
#     print(type(pty), 'pty do average', pty)
#     print(type(pty),'pty do max number:', pty)

# =======↓↓↓↓↓↓↓test zone↓↓↓↓↓↓↓=========
'''
tuple1 = (1,2,3)
tuple2 = (4,5,6)
zipped = zip(tuple1,tuple2)
mapped = map(sum,zipped)
x=tuple(mapped)
print(x)
factor=2
a=[i/factor for i in x]
print(a)
int32=np.array(a, np.int32)
print(type(int32), int32)
tupletype=tuple(int32)
print(type(tupletype), tupletype)
'''
# ===============================================
# # Python3 code to demonstrate working of 

# # Tuple division 

# # using map() + floordiv 

# from operator import floordiv

#   # initialize tuples 

# test_tup1 = (10, 4, 6, 9) 

# test_tup2 = (5, 2, 3, 3) 

#   # printing original tuples 

# print("The original tuple 1 : " + str(test_tup1)) 

# print("The original tuple 2 : " + str(test_tup2)) 

#   # Tuple division

# # using map() + floordiv 

# res = tuple(map(floordiv, test_tup1, test_tup2)) 

#   # printing result 

# print("The divided tuple : " + str(res))
# # --------------------------------------------------------# Python3 code to demonstrate working of 

# # Tuple division

# # using zip() + generator expression 

#   # initialize tuples 

# test_tup1 = (10, 4, 6, 9) 

# test_tup2 = (5, 2, 3, 3) 

#   # printing original tuples 

# print("The original tuple 1 : " + str(test_tup1)) 

# print("The original tuple 2 : " + str(test_tup2)) 

#   # Tuple division 

# # using zip() + generator expression 

# res = tuple(ele1 // ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 

#   # printing result 

# print("The divided tuple : " + str(res)) 



#输出(5,7,9)