def inicjaly(imie, nazwisko):
         output = imie[0].upper() + ". " + nazwisko.capitalize()
         return output
def napisz(fname, lname, funkcja):
		return funkcja(fname, lname)

print(napisz("marcel", "glod", inicjaly))
