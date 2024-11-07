# Algoritmusok és Adatszerkezetek I. - Gyakorlat

## Elérhető feladatok:
### [1. feladat - Missing number](https://github.com/DeakEva/Algoritmusok/raw/main/teszt.py)
Feladat leírása: Hiányzó szám
Adott két szám tömbje, keresse meg, hogy a második tömb mely elemei hiányoznak az első tömbből.
Példa: arr = [7,2,5,3,5,3]
       brr = [7,2,5,4,6,3,5,3]
Abrr array az eredeti lista. A hiányzó számok [4,6]
Ha egy szám többször előfordul a listákban, akkor gondoskodni kell arról, hogy a szám mindkét listában legyen. Ha ez nem így van, akkor is hiányzó szám.
Adja vissza a hiányzó számokat növekvő sorrendben.
Csak egyszer adjon meg egy hiányzó számot, még akkor is, ha többször hiányzik.
Az eredeti lista maximális és minimális száma közötti különbség kisebb vagy egyenlő, mint 100.
A missingNumbs a következő paraméterekkel rendelkezik: 
int arr[n]: a hiányzó számokat tartalmazó tömb
int brr[m]: az eredeti számtömb
Visszatér int[]: az egész számok tömbje
Beviteli formátum
Négy beviteli sor lesz:
n- az első lista mérete.arr
A következő sor tartalmazza n szóközzel elválasztott egész számokat arr[i]
m- a másokdi lista mérete.brr
A következő sor tartalmazza m szóközzel elválasztott egész számokat brr[i]
Korlátozások
1<=n, m<=2*10<sup>5</sup>
n<=ma
1<=brr[i]<=10<sup>4</sup>
max(brr)-min(brr)<=100
>>>>>>


###  [2. feladat - Power sum](https://github.com/)
Feladat leírása: NÉV?
Keresse meg, hogy az adott egész hány módon X az összegeként fejezhető ki N<sup>th</sup> egyedi, természetes számok hatványai.
Töltse ki a powerSum függvényt, egy egész számot kell visszaadnia, amely lehetséges kombinációk számát jelenti.
A poweSum a következő paraméterekkel rendelkezik:
X: az az egész szám, amelyhez összegezni kell
N: az egész szám hatványa, amelyre a számokat emeljük
Beviteli formátum
Az első sor egy egész számot tartalmaz X
A második sor egy egész számot tartalmaz N
Korlátozások
1<=X<=1000
2<=N<=10
Kimeneti formátum
Egyetlen egész szám kiadása, a lehetséges kombinációk kiszámítása.
Minta bemenet 0
10
2 
Minta kimement 0
1
>>>>


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
