# 01 – Bash: grep, wc, sort, uniq, pipe

Bemenet: `samples_files/` (`fruit.txt`, `fruit_data.txt`, `grep_ex1.txt`, `numbers.txt`, `compare_text1.txt`, `compare_text2.txt`, `gutenberg/*`).

Cél: a szövegfeldolgozó parancsok összekapcsolása csővel (`|`) és átirányítással (`>`, `>>`, `<`).

## Feladatok
1. Hány sora, szava és karaktere van a `gutenberg/pg2701.txt` fájlnak? (`wc`)
2. Hány sor tartalmazza a `whale` szót kis-nagybetűtől függetlenül? Hány sorban szerepel *egész szóként*? (`grep -ic`, `grep -iw`)
3. Írd ki a `grep_ex1.txt` azon sorait, amelyek `an`-nal kezdődnek, sorszámmal együtt. Majd azokat, amelyek **nem** tartalmazzák az `an` szót. (`grep -n`, `-v`, `^`)
4. Rendezd a `numbers.txt`-et szövegesen és numerikusan. Mi a különbség? (`sort`, `sort -n`)
5. A `fruit_data.txt` oszlopai: név, mennyiség, ár. Rendezd ár szerint csökkenő sorrendben. (`sort -k3 -nr`)
6. **Szógyakoriság:** a `pg2701.txt` szövegéből készíts listát a 20 leggyakoribb szóról (kisbetűsítve, írásjelek nélkül):
   ```bash
   tr -cs 'A-Za-z' '\n' < samples_files/gutenberg/pg2701.txt | tr 'A-Z' 'a-z' | ... | head -20
   ```
   Egészítsd ki a hiányzó lépéseket (`sort`, `uniq -c`, `sort -rn`).
7. Hány különböző szó van a könyvben? Hány szó fordul elő pontosan egyszer? (`sort -u`, `uniq -c`, `awk` nélkül is megoldható)
8. Hasonlítsd össze a `compare_text1.txt` és `compare_text2.txt` fájlokat: melyik sor van csak az elsőben, csak a másodikban, mindkettőben? (`sort`, `comm -23`, `-13`, `-12`, vagy `diff`)
9. Fűzd össze a `paste_file1.txt` és `paste_file2.txt` fájlokat oszloponként, tabulátorral. (`paste`)
10. Mentsd el a 6. feladat eredményét `out/top20.txt` fájlba, és közben írd ki a képernyőre is. (`tee`)

## Várt kimenet
- 1. feladat: `22316  215838  ...` (sor, szó, bájt)
- 6. feladat: a lista első 5 sora: `the`, `of`, `and`, `a`, `to` (14727, 6746, 6514, 4805, 4709 előfordulással)

A teljes ellenőrzés: `solutions/01_top20.expected`.

## Extra
- Melyik a leggyakoribb 5 betűs szó? (`grep -E '^.{5}$'`)
- Futtasd ugyanezt mind a négy Gutenberg könyvre egy `for` ciklussal, és hasonlítsd össze a top 5 szavukat.
