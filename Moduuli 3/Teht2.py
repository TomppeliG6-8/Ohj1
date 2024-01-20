m1=input(f"Anna hyttiluokka (LUX, A, B, C): ")
if m1=="LUX" or "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif m1=="A" or "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif m1=="B" or "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif m1=="C" or "c":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")