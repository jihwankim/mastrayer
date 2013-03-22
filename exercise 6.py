def check(str) :
	l = len(str)
	i = 0
	while i<int(l/2) :
		if(str[i] != str[l-i-1]) :
			return 'different'
		i = i+1
	return 'same'

temp = raw_input('input strings : ')
print check(temp)