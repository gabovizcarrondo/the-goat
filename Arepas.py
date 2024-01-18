harina = float(input ("Ingresa cantidad de tazas de harina: "))
agua = float(input("Ingresa cantidad de tazas de agua: "))
sal = float(input("Ingresa cantidad de cucharaditas de sal: "))
print ("Harina: , ",harina, "Agua: , ",agua, "Sal: ",sal)
bol = harina*16*3 + agua*16*3 + sal 
bolg = bol*7
print (bolg, "gramos de masa")