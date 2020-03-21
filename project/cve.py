import os
#print('enter cve id: ',end='')
#with open('test.txt','r+') as f:
cve = input()
(os.system('curl https://cve.circl.lu/api/cve/'+cve))
