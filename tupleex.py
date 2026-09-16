# init_tuple_a ='a','b'
# init_tuple_b =('a','b')
# print(init_tuple_a == init_tuple_b)
#python  iss immutable thats whywe are getting true
#op=true
###############################################
# init_tuple_a ='1','2'
# init_tuple_b =('3','4')
# print(init_tuple_a +init_tuple_b)
#op=1234
##############################################
# l=[1,2,3]
# init_tuple=('python,')*(l.__len__()-l[::-1][0])
# print(init_tuple)
#op=0
#####################################################

# init_tuple=('python')*3
# print(type(init_tuple))
#","=shows tuple   if not ", then "str
###################################################
# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)
#error bec tuuple is immutable
###################################################
# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))
#4 
#################################################

# data='Malhar*is*a*good'
# val=''
# newname=''
# for i in data:
#     if i !='*':
#         newname+=i
#     else:
#         val+=i
# print(newname)    
# print(str(val+newname))        

###################################################

s = input()
count = {}
for ch in s:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1
for ch in count:
    print(ch, count[ch], end="")
    




