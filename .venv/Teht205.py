leiv=int(input("Anna leiviskät: "))
naul=int(input("Anna naulat: "))
luo=int(input("Anna luodit: "))
grammat=int(leiv*8512)+(naul*425.6)+(luo*13.3)
#print(f"Massa nykymittojen mukaan: \n{grammat} ")
if grammat<1000:
    print(f"Massa nykymittojen mukaan: \n{grammat} grammaa")

else:
    a=0
    while grammat>1000:
        grammat-=1000
        a += 1
    print(f"Massa nykymittojen mukaan: \n{a} kilogrammaa ja {grammat} grammaa")


