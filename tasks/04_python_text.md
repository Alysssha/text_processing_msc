# 04 – Python: beolvasás, tisztítás, tokenizálás

Bemenet: `samples_files/gutenberg/*.txt`, `doc1.txt`, `doc2.txt`, `llm_example/article.htm`.

Cél: ugyanazt a szógyakoriság-listát elkészíteni Pythonban, amit a 01-es feladatban bash-ben, majd tovább tisztítani.

Hozzatok létre egy `04_text.py` fájlt a saját mappátokban (`vezeteknev_keresztnev/`), és lépésenként bővítsétek.

## Feladatok
1. **Beolvasás:** nyisd meg a `pg2701.txt`-t `encoding="utf-8"` megadásával. Hány sor, hány karakter? Mi történik, ha rossz kódolást adsz meg (`latin-1`) a `219.txt.utf-8` fájlra?
2. **Gutenberg keret levágása:** a szöveg a `*** START OF` sor után kezdődik és a `*** END OF` sor előtt ér véget. Vágd le a keretet.
3. **Normalizálás:** kisbetűsítés, többszörös szóközök egyre cserélése, írásjelek eltávolítása (`re.sub`). Miért hagyod meg az aposztrófot a `don't` szóban? Döntsd el és indokold.
4. **Tokenizálás háromféleképpen:** (a) `text.split()`, (b) `re.findall(r"[A-Za-z']+", text)`, (c) opcionális: `nltk.word_tokenize` vagy spaCy. Hasonlítsd össze a tokenszámokat.
5. **Gyakoriság:** `collections.Counter` – a 20 leggyakoribb token. Egyezik a bash-os (01/6) listával? Ha nem, miért?
6. **Stopszavak:** távolítsd el a leggyakoribb funkciószavakat (írj saját, 50 szavas listát, vagy használd az NLTK-ét). Mi marad a top 20-ban?
7. **Mondatokra bontás:** egyszerű szabály (`. `, `? `, `! `) alapján; add meg az átlagos mondathosszt szavakban. Milyen hibák maradnak (pl. `Mr.`)?
8. **Kimenet:** írd a gyakoriságokat `out/freq.csv` fájlba (`szo,db`), rendezve; a `csv` modullal.
9. **HTML tisztítás:** olvasd be `llm_example/article.htm`-t BeautifulSoup-pal, szedd ki a bekezdéseket (`<p>`), és futtasd rájuk a fenti tisztítást.
10. **Függvényesítés:** szervezd a lépéseket függvényekbe (`read_text`, `clean`, `tokenize`, `count`), és legyen `if __name__ == "__main__":` ágad, amely parancssori argumentumból (`sys.argv` vagy `argparse`) veszi a fájlnevet.

## Várt eredmények
- A `pg2701.txt` 22316 sorból áll.
- A bash-os top 5: `the, of, and, a, to`. A Python-listában is ugyanennek kell lennie a keret nélkül, kisebb eltérésekkel (az aposztróf kezelése miatt).

## Extra
- Hasonlítsd össze két könyv szókincsét Jaccard-hasonlósággal.
- Rajzold fel a gyakoriság–rang összefüggést log-log skálán (Zipf-törvény): `matplotlib`.
