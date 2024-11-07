
N = int(input())

def Felosztasok(osszeg, max_szam):
    if osszeg == 0:
        return 1
    lehetsegesFelosztasok = 0
    for i in range(min(osszeg, max_szam), 0, -1):
        lehetsegesFelosztasok += Felosztasok(osszeg-i, i-1)
    return lehetsegesFelosztasok

print(Felosztasok(N,N))


#lefele a régi kód van, itt a felosztások mikéntje is látható. A fenn lévőben csak a felosztások száma

"""
def Felosztasok(N):
    lehetsegesFelosztasok =[]

    def BackTrack(osszeg, max_szam, akt_felosztas):
        if osszeg == 0:
            lehetsegesFelosztasok.append(akt_felosztas[:])
            return
        for i in range(min(osszeg, max_szam), 0, -1):
            akt_felosztas.append(i)
            BackTrack(osszeg-i, i-1, akt_felosztas)
            akt_felosztas.pop()

    BackTrack(N, N, [])
    return lehetsegesFelosztasok

N = int(input("\nAdj meg egy számot 1<=N<=200 között! Szám: "))
    
lehetsegesFelszotasok = Felosztasok(N)
meret = len(lehetsegesFelszotasok)

print(f"\n{N} = {N}")
for i in range(1, meret):
    j = 0
    for ertek in lehetsegesFelszotasok[i]:
        if j != len(lehetsegesFelszotasok[i])-1:
            print(f"{ertek}", end=' + ')
        else:
            if i == meret - 1:
                print(f"{ertek}")
            else:
                print(f"{ertek}", end=' vagy ')
        j+=1
    print()
"""