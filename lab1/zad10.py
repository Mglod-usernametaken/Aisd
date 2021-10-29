def palindrom(wyraz):
	flag = True
	for i in range (int(len(wyraz))):
		if wyraz[i] != wyraz[-(i+1)]:
			flag = False
		print( wyraz[i]+ " " + wyraz[-(i+1)])
	return (flag)
		

a = "kajk"
print(int(3.5))
print(palindrom(a))
