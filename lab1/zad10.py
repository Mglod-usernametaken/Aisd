def palindrom(wyraz):
	flag = True
	for i in range (int(len(wyraz)/2)):
		if wyraz[i] != wyraz[-(i+1)]: 
			flag = False
	return (flag)
		

a = "kajak"
b = "katmaran"
print(a , palindrom(a))
print(b, palindrom(b))
