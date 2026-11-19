# 02 – awk: számolás, napló és táblázat ellenőrzése

Bemenet: `samples_files/fruit_data.txt`, `fruit_data.csv`, `sample_date.txt`, `reformat_dates.awk`, `nextflow.log`, `trace.txt`, `bacteria_metadata.tsv`.

Az awk soronként dolgozik: `awk 'minta { művelet }' fájl`. Hasznos: `$1`, `NR`, `NF`, `-F'\t'`, asszociatív tömbök, `BEGIN`/`END`, `printf`.

## A fájlok
- `nextflow.log`: egy bioinformatikai Nextflow pipeline naplója (időbélyeg, szál, szint, osztály, üzenet).
- `trace.txt`: ugyanennek a futásnak a trace táblázata (tabulátorral elválasztva: task_id, hash, name, status, exit, submit, duration, realtime, %cpu, peak_rss).
- `nextflow.real.log`: egy **valódi** (anonimizált) `.nextflow.log` egy megszakított futásból: 1652 sor, a nagy része DEBUG, sok többsoros blokk (konfiguráció-kiírás, Java üzenetek). Nem olyan tiszta, mint a másik, ezért nehezebb.
- `bacteria_metadata.tsv`: valódi NCBI RefSeq baktérium assembly metaadatok (80 genom).

## Feladatok
1. A `fruit_data.txt`-ben add össze gyümölcsönként a mennyiséget (`s[$1]+=$2`). Írd ki szépen: `printf "%-10s %5d\n"`.
2. Számold meg a `trace.txt` sorait státusz szerint (`COMPLETED`/`FAILED`). Ne számold a fejlécet (`NR>1`).
3. Hány feladat futott az egyes folyamatokból (FASTQC, FASTP, SPADES, PROKKA, AMRFINDER)? A `name` oszlop (`$3`) első szava kell: `split($3, a, " ")`. Miért van 9 a SPADES és a PROKKA mellett, a többinél 8?
4. Melyik feladat és milyen `exit` kóddal bukott el? Melyik a leghosszabb ideig futó feladat? (A `duration` értéke `717s` formátumú; `$7+0` számmá alakítja.)
5. A `nextflow.log`-ból számold meg, hányszor fordul elő `INFO`, `DEBUG`, `WARN`, `ERROR` szint. (Vigyázat: a `[Task submitter]` két mezőre esik szét, így a szint pozíciója sorról sorra változik. Használj mintaillesztést: `match($0, /(INFO|DEBUG|WARN|ERROR) /)`, vagy `-F'] '`.)
6. Hány `Submitted` üzenet van a naplóban percenként? (Az időbélyeg 2. mezőjéből vágd ki az `óra:perc` részt: `substr($2, 1, 5)`.)
7. `bacteria_metadata.tsv` (`-F'\t'`): hány genom van fajonként (első két szó az `organism_name` oszlopban)? Írd ki fajonként az átlagos genomméretet is, de csak azokra a fajokra, amelyekből legalább 2 van.
8. Számold ki az összes genom átlagos GC%-át és a legnagyobb genomot (név + méret).
9. Futtasd a `reformat_dates.awk`-t a `sample_date.txt`-n (`awk -f reformat_dates.awk sample_date.txt`). Miért nem jó a kimenet? Javítsd ki a mezőelválasztóval (`-F'[\t-]'`), majd bővítsd úgy, hogy a dátumokat `ÉÉÉÉ/HH/NN` formában is kiírja, évenkénti darabszámmal.

## Feladatok – a valódi napló (`nextflow.real.log`)
10. Hány sor **nem** időbélyeggel kezdődik? Mit tartalmaznak ezek (`NR`, `!/^[A-Z][a-z][a-z]-[0-9][0-9] /`)? Miért okoz ez gondot a szintenkénti számolásnál?
11. Számold meg a naplószinteket (DEBUG/INFO/WARN) csak az időbélyeges sorokból. Mennyi a DEBUG aránya?
12. Szálanként (`[main]`, `[Task submitter]`, ...) hány bejegyzés van? Melyik a legaktívabb?
13. Mennyi ideig tartott a futás az első és az utolsó időbélyeg között? (Az `óra:perc:másodperc` részből számolj másodpercet: `split($2, t, ":")`.)
14. A futás **megszakadt** (nézd meg az utolsó sorokat: `SIGINT`, `Killing running tasks`). Keresd meg az awk-kal a megszakítás pillanatát, és írd ki a sort közvetlenül előtte és utána.

## Várt kimenet
- 1.: `apple 35`, `banana 20`, `cherry 15`
- 2.: `COMPLETED 40`, `FAILED 2`
- 3.: `AMRFINDER 8`, `FASTP 8`, `FASTQC 8`, `PROKKA 9`, `SPADES 9`
- 4.: `SPADES (sample03)` (exit 137), `PROKKA (sample06)` (exit 1); leghosszabb: `SPADES (sample07)`, 717 s
- 7.: pl. `Escherichia coli 6 5080646`
- 10.: 1420 sor
- 11.: `DEBUG 220`, `INFO 10`, `WARN 2`
- 12.: a `[main]` 210 bejegyzéssel vezet

Teljes ellenőrzés: `solutions/02_awk.expected`.

## Extra
Írj egy awk-szkriptet (`awk -f`), amely egyetlen jelentést ad: összes feladat, sikertelenek, összes CPU-idő, maximális memória.
