import random

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
numbers = '0,1,2,3,4,5,6,7,8,9'
cap = alphabet.upper()
symbols = '!,@,#,$,%,&,*'

combine = alphabet + ','+ numbers + ',' + cap +','+symbols
combine_list = combine.split(",")
# print(combine_list)
n1 = random.choice(combine_list)
n2 = random.choice(combine_list)
n3 = random.choice(combine_list)
n4 = random.choice(combine_list)
n5 = random.choice(combine_list)
n6 = random.choice(combine_list)
n7 = random.choice(combine_list)
n8 = random.choice(combine_list)
n9 = random.choice(combine_list)
n10 = random.choice(combine_list)


Password = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
print(f"We recommend using strong password like: {Password}")
