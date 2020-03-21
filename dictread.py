file ='test.txt'
dict=eval(open(file).read())
del dict['references']
del dict['vulnerable_product']
del dict['vulnerable_configuration']
for i,j in dict.items():
	print(i,': ',j)
	print('---------------------------------------------------------------')
#print(dict['summary'])
'''
k=dict(mydic)
for i,j in k.items():
	print(i)
'''
#file.close()
