# 06 – Házi feladat: saját projekt kis nyelvi modellel (Ollama)

Cél: egy **teljesen automatikusan futó pipeline** készítése, amely szöveges adatokból egy helyi, kis nyelvi modell (LLM) segítségével strukturált eredményt állít elő.

## Követelmények
1. **Saját téma és korpusz.** Pl. PubMed absztraktok (Biopython `Entrez`), egy weboldal cikkei, publikus riportok, saját jegyzetek. 20–100 dokumentum elég. A témát egyeztessétek az issue-ban.
2. **Pipeline lépései** (egyetlen paranccsal fusson végig: `python pipeline.py`):
   - adatgyűjtés (letöltés vagy beolvasás),
   - tisztítás (04-es feladat: kódolás, HTML eltávolítás, normalizálás),
   - promptolás helyi modellel (Ollama),
   - kimenet strukturált formában (JSON/CSV), a modell válaszának ellenőrzésével (érvényes JSON? ha nem: újrapróbálkozás),
   - összesítés (táblázat vagy rövid jelentés: pl. leggyakoribb címkék, entitások).
3. **Kis modell:** olyan, ami a saját gépeden is fut, pl. `gemma3:4b`, `qwen2.5:3b`, `llama3.2:3b` (`ollama pull <modell>`).
4. **Reprodukálhatóság:**
   - `requirements.txt` és `README.md` a mappában: mit csinál, hogyan kell futtatni (a lépéseket gépen kipróbálva),
   - a kimenetek mentése (`out/`), a nyers LLM-válaszokkal együtt,
   - nincsenek a kódban személyes elérési utak, e-mail címek, API kulcsok (környezeti változó vagy parancssori argumentum).
5. **Rövid értékelés a README-ben:** hol hibázott a modell, mit javítottál a promptban (min. 3 hibaeset példával).

## Kiindulópont
`llm_example/html_to_text.py`: weboldal → bekezdések → Ollama összefoglaló. Az elérési utat előbb javítsd relatívra, utána bővítsd (ciklus több dokumentumra, JSON kimenet).

Minimális modellhívás (a `ollama` Python csomaggal):
```python
import ollama
r = ollama.generate(model="gemma3:4b", prompt="...", format="json")
print(r["response"])
```

## Opcionális: teljesítménynapló
A `pipeline.py` írjon `out/performance.csv`-t dokumentumonként:

| doc_id | model | chars | prompt_tokens | output_tokens | seconds | tokens_per_sec | ok_json |
|---|---|---|---|---|---|---|---|

Az Ollama válasza tartalmazza az adatokat: `prompt_eval_count`, `eval_count`, `total_duration` (ns), `eval_duration` (ns). A `tokens_per_sec = eval_count / (eval_duration / 1e9)`.

Ezt kiegészítheted:
- két modell összehasonlításával (sebesség és helyesség egy kézzel ellenőrzött 10 dokumentumos mintán),
- a gép adataival (CPU/GPU, RAM) a README-ben.

## Beadás
A fork-ból **pull request** a kurzus repójába, a saját mappádba: `vezeteknev_keresztnev/`. A PR leírásában legyen: téma, modell, futtatás, és ha készült, a teljesítménynapló összefoglalója.

## Értékelési szempontok
Az automatikus futás (egy parancs), reprodukálhatóság, a kimenet ellenőrzése és hibakezelés, az értékelés őszintesége, a kód olvashatósága. A teljesítménynapló bónusz.
