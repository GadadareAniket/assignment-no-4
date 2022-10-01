#write a python prog to triple all numbers of a given list of integers use python map 
sample_number=(1,2,3,4,5,6,7)
print("original list :",sample_number)
result = map(lambda x: x+x+x,sample_number)
print("/n triple of said list number :")
print(list(result))