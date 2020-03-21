import shodan

SHODAN_API_KEY = "rmijlWxRatPZGxTgjtYIjOWONZ2us9Wg"

api=shodan.Shodan(SHODAN_API_KEY)
S=input('search terms-->>')

try:
	results = api.search(S)

	print ('results found: %s' %results['total'])
	for result in results['matches']:
		print(result['ip_str'])
		print ('IP: %s'% result['ip_str'])
		print (result['data'])
		print ('')
		print('-------------------------------------------------------------------------')

except shodan.APIError as e:
	print ('Error: %s' %e)
