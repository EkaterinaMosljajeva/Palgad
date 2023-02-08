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

