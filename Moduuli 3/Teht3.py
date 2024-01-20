x1=input(f"Anna sukupuoli (M) tai (N): ")
hem=int(input("Anna hemoglobiiniarvo: "))
al=str("Hemoglobiiniarvo on alhainen")
nor=str("Hemoglobiiniarvo on normaali")
kor=str("Hemoglobiiniarvo on korkea")

if x1=="m" or x1=="M":
    if hem<134:
        print(al)
    elif hem>195:
        print(kor)
    else:
        print(nor)

elif x1=="n" or x1=="N":
    if hem < 117:
        print(al)
    elif hem > 175:
        print(kor)
    else:
        print(nor)

else:
    print("Kokeile uudestaan.")