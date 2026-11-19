# 05 – Mini projekt: FASTA → PHYLIP → fehérje FASTA

Bemenet:
- `samples_files/genes.fasta` – 8 rövid (150 nt) gén, a phiX174 fág valódi kódoló szakaszainak eleje. Szándékosan tartalmaz problémákat: egy kisbetűs szekvenciát, egy `N` bázist és egy belső stopkodont.
- `samples_files/phix174.fasta` – a teljes phiX174 fág genom (5386 nt, NC_001422.1), a kiegészítő feladathoz.

Cél: kisebb adatfeldolgozó program építése lépésről lépésre, saját kóddal. Biopythont csak ellenőrzésre használj (`pip install biopython`).

## Formátumok
**FASTA:** `>név leírás` fejléc, majd a szekvencia (tetszőleges sorhosszal).

**Szekvenciális PHYLIP (szigorú):** az első sorban a szekvenciák száma és a hossz, utána soronként egy szekvencia. A név **pontosan 10 karakter** (szóközzel kipótolva), utána a szekvencia. A szekvenciáknak **azonos hosszúságúnak** kell lenniük (igazítás).
```
 8 150
seq1      ATGGTTCGTT...
seq2      ATGAAATCGC...
```

## Feladatok
1. **FASTA beolvasása:** írj függvényt, amely `{név: szekvencia}` szótárat ad vissza. A fejlécből csak az első szót tartsd meg. Fűzd össze a többsoros szekvenciákat.
2. **Tisztítás:** a szekvenciát nagybetűsítsd, szűrd ki a nem betű karaktereket. Ellenőrizd: minden hossz osztható-e 3-mal és azonos-e?
3. **Rövid nevek:** a hosszú azonosítók (pl. `phiX174_NP_040703`) nem férnek a 10 karakterbe. Képezz `seq1`, `seq2`, … neveket, és mentsd el a megfeleltetést `names.tsv`-be.
4. **PHYLIP írása:** `out/genes.phy`. Ellenőrizd: az első sor ` 8 150`, minden további sor pontosan 160 karakter.
5. **PHYLIP visszaolvasása:** a fájlból olvasd be újra a szekvenciákat (a név az első 10 karakter, `strip()`-pel). Ez a pipeline következő lépése, ne a memóriából dolgozz tovább.
6. **Transzláció:** írd meg a kodontáblát (64 kodon → aminosav, stop = `*`) saját kóddal. Fordítsd le a szekvenciákat fehérjére. Kezeld: `N`-t tartalmazó kodon → `X`; belső stop → hagyd `*`-gal, de jelezd a kimeneten.
   Tipp: `AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"` a `TCAG` sorrendben (T, C, A, G) adja a kodonokat; `itertools.product("TCAG", repeat=3)`.
7. **Fehérje FASTA írása:** `out/genes_prot.fasta`, 60 karakteres sorokkal. A fejlécben állítsd vissza az eredeti nevet a `names.tsv` alapján.
8. **Ellenőrzés Biopythonnal:** `Bio.Seq.Seq(dna).translate()` ugyanazt adja? Hol tér el (`N`, stop)?
9. **Parancssori program:** `fasta2phylip2prot.py bemenet.fasta kimenet_prefix` (`argparse`), amely mind a három kimenetet előállítja. Ha a hossz nem azonos vagy nem osztható 3-mal, érthető hibaüzenettel álljon le.
10. **Teszt:** írj `assert`-ekkel egy kis tesztet, amely a program kimenetét összeveti a `solutions/genes_prot.expected` fájllal.

## Kiegészítő feladat: a teljes genom
A phiX174 genom nem „igazított” (egyetlen hosszú szekvencia), és nem kódoló szakasz-határokkal indul.
1. Fordítsd le mindhárom előre menő leolvasási keretben (frame 1, 2, 3).
2. Keresd meg az `M`-mel kezdődő, `*`-gal záruló szakaszokat (ORF-ek, `re.finditer(r"M[^*]*\*", prot)`).
3. Mi a leghosszabb ORF? Várható: 427 aminosav, a 2. keretben, a 1001. nukleotidnál kezdődik, ez a F fehérje (major head protein, az NCBI-annotáció 1001..2284).
4. Mit kell megváltoztatni, ha a komplementer szálat is vizsgálod? (`reverse complement`, 6 keret)
5. Ha a genomot be akarod tenni a PHYLIP-be a többi génnel: milyen kompromisszumot kell kötnöd? (Gyakorlatban csak azonos hosszúságú, igazított szekvenciák kerülhetnek bele; hosszabb igazításhoz `-` hézagokkal kell kipótolni.)

## Várt kimenet
- `out/genes.phy` első sora: ` 8 150`
- 5. fehérje (`seq5`) tartalmaz `X`-et, a 7. (`seq7`) belső `*`-t.
- Teljes referencia: `solutions/genes.phy`, `solutions/genes_prot.fasta`, `solutions/genes_names.tsv`; a mintamegoldás: `solutions/fasta2phylip2prot.py` (előbb saját megoldás, csak utána nézd meg!).
