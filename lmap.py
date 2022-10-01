#write a python program to square the element of a list using map() function
sample_list=[4,5,2,9]
def squares(x):
    return x**2
b=list(map(lambda x:x**2,sample_list))
print(b)