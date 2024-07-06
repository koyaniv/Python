# name = input("What is your nme? ")

# if name == "yan":
#     print("Great yaniv")
# elif name == "ron":
#     print("Greate Ron")
# else:
#     print("ohhhh")

#-------  slice ---------
# x = [0,1,2,3,4,5,6,7,8]
# slice = x[::-1]
# print(slice)
#
# y = "abcdcba"
# slice = y[::-1]
# print(slice)
#
# if y == y[::-1]:
#     print("---- palindrome -----")
# else:
#     print("not palindrome")

#-------  set & distionary  ---------
# s = {4,32,2,2}
# s2 = {3,5,22,1}
# print(s)
# print(s2)
#
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))

#-------

#
# x= [i for i in range(10) if i%2==0]
# print(x)
#
# #Dictionary
# x= {i:0 for i in range(10) if i%2==0}
# print(x)
#
# #Tuplle
# x= tuple(i for i in range(10) if i%2==0)
# print(x)


#-------  Func ---------

def func(x):
    print("Hello",x)
    return x+1

func(3)

#--------

# x = [1,23,42323,2324]
#
# print(x)
# print(*x)

#--------

# def func(x,y):
#     print(x,y)
#
# pairs = [(1,2),(3,4),(5,6)]
#
# for pair in pairs:
#     func(*pair)

#-------- try ctch --------

try:
    x = 1/0
except Exception as e:
    print(e)    # division by zero

#--------  F strings --------
tim = 68

x = f'Hello {3 + 4} {tim}'
print(x)

print(f'Hello {3 + 4} {tim}')