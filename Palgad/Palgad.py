from moodul import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
while True:
    menu=int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Väiksem palk\n5-Sort\n6-\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}'l")
    elif menu==4:
        palk,nimi=vaiksem_palk(inimesed,palgad)
        print(f"Väiksem palk on {palk} {nimi}'l")
    elif menu==5:
        inimesed,palgad=sorteerimine(inimesed,palgad)
        print(inimesed,"\n",palgad)
    elif menu==6:
        