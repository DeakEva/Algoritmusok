# Algoritmusok és Adatszerkezetek I. - Gyakorlat

## Elérhető feladatok:
### [1. feladat - Missing number](https://github.com/DeakEva/Algoritmusok/raw/main/teszt.py)
**Feladat leírása:**<br>
Adott két szám tömbje, keressük meg, hogy a második tömb mely elemei hiányoznak az első tömbből.
Ha egy szám többször előfordul a listákban, akkor gondoskodni kell arról, hogy a szám mindkét listában legyen. Ha ez nem így van, akkor is hiányzó szám.

**Kikötések**
- Csak egyszer adjon meg egy hiányzó számot, még akkor is, ha többször hiányzik.
- Az eredeti lista maximális és minimális száma közötti különbség kisebb vagy egyenlő, mint 100.
- Hiányzó számok növekvő sorrendben térjenek vissza
- 1 <= n
- m <= 2*10<sup>5</sup>
- n <= ma
- 1 <= brr[m] <= 10<sup>4</sup>
- max(brr) - min(brr) <= 100

**Függvény működése:**<br>
Bemenet:
- **int[n]**: egész számok, ahol az *"n"* a lista méretét jelöli
- **int[m]**: egész számok, ahol az *"m"* a lista méretét jelöli

Kimenet:
- **int[]**: egész számomat tartalmazó tömb

**Példa bement:**
- **arr[n]**: n darab szóközzel elválasztott, hiányzó számokat tartalmazó tömb<br>arr = [7,2,5,3,5,3]
- **brr[m]**: m darab szóközzel elválasztott, eredeti számokat tartalmazó tömb<br>brr = [7,2,5,4,6,3,5,3]

**Elvárt kimenet:**<br>
- [4,6] számo(ka)t tartalmazó tömb


### [2. feladat - Power sum](https://github.com/)
**Feladat leírása:**<br>
Határozzuk meg, hogy egy adott egész szám hányféleképpen fejezhető ki egyedi, természetes számok **N<sup>p</sup>**-edik hatványainak összegeként

**Kikötések**
- 1 <= X <= 1000
- 2 <= N <= 10

**Függvény működése:**<br>
Bemenet:
- **X**: összegszám
- **N**: hatványkitevő, amire a számokat emelni kell

Kimenet:
- **int**: az összes lehetséges kombinációt tartalmazó **egész** szám

**1) Példa bement:**
- **X**: 10
- **N**: 2

**Elvárt kimenet:**<br>
- 1
- Magyarázat: 10 = 1<sup>2</sup> + 3<sup>2</sup>

**2) Példa bement:**
- **X**: 100
- **N**: 2

**Elvárt kimenet:**<br>
- 3
- Magyarázat: 100 = (10<sup>2</sup>) = (6<sup>2</sup> + 8<sup>2</sup>) = (1<sup>2</sup> + 3<sup>2</sup> +4 <sup>2</sup> +5 <sup>2</sup> +7<sup>2</sup>)

###  [3. feladat - Fibonacci sequence]
Feladat leírása: Fibonacci sorozat
Valósítson meg módosított Fibonacci sorozatot a következők szerint:
Adott feltételek [i] és t[i+1] ahol i (1,) kifejezést [i+2]a következőképpen kerül kiszámításra: ti+2=ti+(ti+1)<sup>2</sup>
Adott három egész szám t1,t2 és n számítsa ki és nyomtassa ki az a n<sup>th</sup> egy módosított Fibonacci szekvencia kifejezését.
Töltse ki a fibonacciModdified függvényt az alábbi szerkesztőben. Vissza kell adnia az n <sup>th</sup> számot a sorozatban.
A fibonacciModified a következő paraméterekkel rendelkezik:
int t1: egész szám
int t2: egész szám
int n: a jelentő iteráció
Visszatér 
int: a n<sup>th</sup> szám a sorozatban
Beviteli formátum
Három szóközzel elválasztott egész szám egyetlen sora, értékei t1 t2 és n
Korlátozások
0<=t1,t2<=2
3<=n<=20
tn messze meghaladja 64 bit int tartományt>>>>
Minta bemenet
0 1 5
Minta kimenet
5



### [4. feladat - Dijkstra]
Feladat leírása: Adott egy irányíthatatlan gráf és egy kezdő csomópont, határozza meg a kezdő csomóponttól a gráf összes többi csomópontjáig vezető legrövidebb utak hosszát. Ha egy csomópont nem érhető el, a távolsága -1. A csomópont számozása folyamatosan történik 1 és n az élek távolsága vagy hosszúsága változó.
Töltse ki a shortestReach függvényt az alábbi szerkesztőben. Olyan egész számok tömbjét kell visszaadnia, amelyek az egyes csomópontok legrövidebb távolságát jelentik a kezdő csomóponttól a csomópontszám növekvő sorrendjében.
n: a csomópontok száma a gráfban
élek: egész számok 2D tömbje, ahol mindegyik sarok[i] három egész számból áll, amelyek egy él kezdő és végcsomópontját jelentik, majd az él hosszát
s: a kezdő csomópont száma
Beviteli formátum
Az első sor tartalmazza t a tesztesetek számát.
Az első sor két szóközzel elválasztott egész számot tartalmaz n és m a csomópontok és élek száma a gráfban.
Mindegyik következő m sor három szóközzel elválasztott egész számot tartalmaz x és y és r egy él kezdő és záró csomópontja, valamint az él hossza
Minden teszteset utolsó sorában van egy egész szám s, a kiindulási helyzetet jelöli.
Korlátozások
1<=t<=10
2<=n<=3000
1<=m<=N*(N-1)/2
1<=x,y,s<=N
1<=r<=10<sup>5</sup>>>>>>>>>>>
Kimeneti formátum
Az egyes t tesztesetek nyomtasson egyetlen sort, amelyből áll n-1 szóközzel elválasztott egész számok, amelyek a legrövidebb távolságot jelölik n-1 csomópontok a kiindulási helyzetből s cimkéik növekvő sorrendjében, kivéve s.
Az elérhetetlen csomópontok esetén nyomtasson -1





### Algoritmusok és Adatszerkezetek I. - Kollokvium feladat 
Nemes Tihamér versenyfeladat
Feladat leírása: (https://mester.inf.elte.hu:8181/faces/leiras.xhtml?jfwid=99e6a65c6c28a998de8377a8e05d:21) 

### Problémamegoldó szeminárium OKTV feladat
Gyémántok
Feladat leírása: (https://mester.inf.elte.hu:8181/faces/leiras.xhtml?jfwid=99e6a65c6c28a998de8377a8e05d:10)


# Készítette
- Deák Éva - JNGAXV
- rövidciklusú digitális kultúra tanári szak
