v1=int(input("Anna vuosi: "))
if v1 % 4==0 and v1 % 100 != 0 or v1 % 400 == 0:
    print("Annettu vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")