from moodul import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A"]
while True:
    menu=int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Väiksem palk\n5-Sort\n6-Palga dubleerimine\n7-Palgaotsing nime\n8-Rohkem/vähem kui märgitud palk\n8-Leida kõik inimesed, kelle palk on suurem/väiksem kui sisestatud palk\n9-3 kõige vaesemat/rikkamat inimest\n10-Keskmine palk\n11-Palgad pärast tulumaksu\n12-Sorteerimine nime järgi\n13-Eemaldada keskmisest madalamad palgad\n"))
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
        inimesed,palgad=vordsed_palgad(inimesed,palgad)
    elif menu==7:
        poisk(inimesed,palgad)
    elif menu==8:
        palgadfilter(inimesed,palgad)
    elif menu==9:
        inimesed,palgad=top3(inimesed,palgad)
    elif menu==10:
        keskmine(inimesed,palgad)
    elif menu==11:
        tulumaks(inimesed,palgad)
    elif menu==12:
        palgad,inimesed=sorteerimine(palgad,inimesed)
        print(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=alla_keskmise(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==15:
        protsent_5(inimesed,palgad)
