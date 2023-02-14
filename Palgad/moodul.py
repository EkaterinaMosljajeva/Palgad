def lisa_andmed(i:list,p:list):
    """Lisage veel mõned inimesed ja palgad
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi:")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(nimi)
    return i,p

def kustutamine(i:list,p:list):
    """Eemaldage inimene ja tema palk
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p

def suurim_palk(i:list,p:list):
    """Leia suurim palk ja kes seda saab
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def vaiksem_palk(i:list,p:list):
    """Leia suurim palk ja kes seda saab
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def sorteerimine(i:list,p:list):
    """Korraldage palgad kasvavas ja kahanevas järjekorras koos nimedega
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    v=int(input("Palk 1-kahaneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi

    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    return i,p

def vordsed_palgad(i:list,p:list):
    """Selgitage välja, kes saavad sama palka, leidke välja, kui palju neid inimesi on ja kuvage nende andmed ekraanil
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid: #1200, n=2
        n=p.count(palk)
        k=-1
        print(f"{palk} saab kätte jargmised inimesed:")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)

def poisk(i:list,p:list):
    """Tehke palgaotsing isiku nime järgi.
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    """
    nimi=input("Kelle palk tahad leia? ")
    while nimi not in i:
        nimi=input("Palun kirjuta õige nimi ")
    n=i.count(nimi)
    if n!=1:
        print(f"Siin on mõned inimesed kes nimi on {nimi}") 
        kopia=i.copy()
        for j in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{j+1} {nimi} saab {p[ind]}")
    else:
        ind=i.index(nimi)
        print(f"{nimi} saab {p[ind]}")

def palgadfilter(i:list, p:list):
    """Leida kõik inimesed, kelle palk on suurem/väiksem kui sisestatud palk.
    ::param: list i: Inimeste järjend
    ::param: list p: Palgade järjend
    """
    o=int(input("Palk 1-suurem, 2-vähem?"))
    palk1=int(input("print palk"))
    list1 = []
    if o==1:
        for j in range(len(i)):
            if palk1<p[j]:
                list1.append((i[j], p[j]))
        print(f"kõik inimesed, kes teenivad rohkem kui {palk1} on {list1}")
    elif o==2:
        for j in range(len(i)):
            if palk1>p[j]:
                list1.append((i[j], p[j]))
        print(f"kõik inimesed, kes teenivad vähem kui {palk1} on {list1}")

def top3(i:list,p:list): 
    """3 kõige vaesemat ja rikkamat inimest
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    """
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(min(kopia))
        print(f"{j+1} inimene - {i[ind]} saab väikse palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(max(kopia))
        print(f"{j+1} inimene - {i[ind]} saab suur palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(p)+1)

def keskmine(i:list,p:list): 
    """Keskmine palk ja selle saaja nimi
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    """
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for j in range(len(j)):
        if p[j]>=kesk:
            print(f"{i[j]} saab suurem kui keskmine palk, ta saab {p[j]}")

def tulumaks(i:list, p:list):
    """Arvutage töötasu, mida inimene saab pärast tulumaksu arvutamist.
    :param: List i: People's list
    :param: List p: Salaries list
    """
    print(i)
    nimi=int(input("Valige selle isiku ametikoht, kelle palka soovite teada saada: "))
    nimi2=nimi-1
    palg=p[nimi2]
    if palg<=1200:
        palg-=500
        if palg < 0:
            palg = 0
            palg+=p[nimi2]
            print(f"{palg}")
        else:
            palg*=0.8
            palg += 500
            print(f"{palg}")
    elif palg > 1200 and palg < 2100:
        tulemaks = 500-0.55556*(palg-1200)
        palg-=tulemaks
        palg*=0.8
        palg+=tulemaks
        palg= round(palg,1)
        print(f"{palg}")
    else:
        palg*=0.8
        print(f"{palg}")

def alla_keskmise(i:list,p:list): 
    """Leidke üles need, kes teenivad alla keskmise palga, ja eemaldage nad nimekirjadest.
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """
    kesk_palk=sum(p)/len(p)
    v=int(input("Kellel palk 1-on suurem,2-on väiksem?"))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    else:
        for palk in p:
            if palk<kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    return i,p

def protsent_5(i:list,p:list): 
    """Igal aastal saavad ettevõtte töötajad 5% palgatõusu, mis on T aasta pärast teatud töötaja palk/palgad.
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtype:str
    """ 
