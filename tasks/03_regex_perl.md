# 03 – Reguláris kifejezések: grep -P, perl, sed

Bemenet: `samples_files/bacteria_metadata.tsv`, `nextflow.log`, `trace.txt`.

Eszközök:
- `grep -oP 'minta'` – csak az illeszkedő rész kiírása (Perl-regex; `\K`, lookahead)
- `perl -ne 'print "$1\n" if /minta(...)/'` – csoportok kinyerése
- `perl -pe 's/minta/csere/g'` – cseréhez
- `sed -E 's/minta/csere/'` – egyszerű cserék

Ha a `grep -P` hibát ír (`supports only unibyte and UTF-8 locales`), futtasd előtte: `export LC_ALL=C.UTF-8`.

## Feladatok – kinyerés
1. Add ki az összes assembly azonosítót (`GCF_015775755.1` alakú) a `bacteria_metadata.tsv`-ből. Hány van? (`GC[AF]_\d+\.\d`)
2. Add ki a BioSample azonosítókat (`SAMN` + számok).
3. Az `infraspecific_name` oszlopban a törzsek `strain=...` alakúak. Írd ki csak a törzs nevét (a `strain=` nélkül) – `\K` vagy csoport használatával.
4. Egy sorból csak a faj nevét (két szó: nagybetűs nemzetség + kisbetűs faj) és a genomméretet kérd, tabulátorral elválasztva (`perl -ne`).
5. A `nextflow.log`-ból add ki az időbélyegeket (`Mar-12 09:14:07.104`), majd csak az óra-perc-másodperc részt.
6. Add ki az összes `[xx/yyyyyy]` hash-t (két hexa karakter, perjel, hat hexa karakter) a naplóból.
7. Add ki a hibás folyamatok nevét: az `Error executing process > '...'` sorból csak az aposztrófok közti részt.
8. Add ki a `terminated with an error exit status (...)` sorokból csak a kilépési kódot (lookbehind vagy `\K`). Mit ad ki, és melyik folyamathoz tartozik?

## Feladatok – csere
9. Alakítsd át a `seq_rel_date` oszlop dátumait `ÉÉÉÉ-HH-NN`-ről `NN.HH.ÉÉÉÉ` alakra (`perl -pe 's/(\d{4})-(\d\d)-(\d\d)/$3.$2.$1/'`).
10. A szervezetnevet írd át rövid alakra: `Escherichia coli` → `E. coli` (a nemzetség kezdőbetűje + pont). Csak az `organism_name` oszlopra alkalmazd.
11. Töröld a `strain=` előtagot az egész fájlból, és a törzs nevét tedd zárójelbe.
12. A `nextflow.log`-ban cseréld az összes `sampleNN` nevet `S_NN`-re.

## Gondolkodtató
- Mi a különbség a `.*` (mohó) és a `.*?` (lusta) között? Próbáld ki a 4. feladatban.
- Mi történik, ha az 1. feladat mintájából elhagyod a `GC[AF]_` előtagot, és csak `\d+\.\d`-t keresel?
- Írj olyan mintát, amely csak azokat a sorokat adja ki, ahol a genom mérete 7 jegyű és a GC% 60 fölötti. (Nehéz, de megoldható regexszel *és* awk-val is: melyik olvashatóbb?)

## Várt eredmények
- 1.: 80 azonosító (az első `GCF_015775755.1`)
- 3.: az első sor törzse `DK1622::pDPO-Mxn116-Pvan-Tpase`
- 7.: `SPADES (sample03)` és `PROKKA (sample06)`

Teljes ellenőrzés: `solutions/03_regex.expected`.
