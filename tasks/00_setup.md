# 00 – Előkészületek

A feladatokat egyedül, saját géppen oldjátok meg. Linux/bash környezet kell hozzá (Windows-on WSL), Python 3.10+, `perl` és `gawk`.

## 1. Fork és klónozás
1. GitHubon kattintsatok a **Fork** gombra a kurzus repóján.
2. `git clone https://github.com/<felhasznalonev>/text_processing_msc.git`
3. `cd text_processing_msc`
4. Minden feladathoz külön ágat vagy legalább külön commitot használjatok: `git switch -c feladat-01`.

## 2. Hol dolgozzatok?
- **Saját gép:** Linux, macOS, vagy Windows + WSL (`wsl --install`).
- **GitHub Codespaces:** a fork oldalán *Code → Codespaces → Create*. A `.devcontainer/` beállítása telepíti a Pythont, perlt, gawk-ot.
- Bármi más (pl. Colab) csak a Python-részekhez jó, a bash/awk/perl feladatokhoz nem.

## 3. Python környezet
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Eszközök ellenőrzése
```bash
bash --version | head -1
gawk --version | head -1
perl -v | head -2
python3 --version
ollama --version        # csak a házi feladathoz kell
```

## 5. Ellenőrzés
A `solutions/` mappában a **várt kimeneteket** találjátok (`*.expected`). Először mindig oldjátok meg magatok, utána vessétek össze:
```bash
diff <(a_ti_parancsotok) solutions/01_valami.expected && echo OK
```

## Mintafájlok
Minden bemeneti fájl a `samples_files/` mappában van. **Ne írjatok bele**, a kimeneteket új fájlba irányítsátok (`out/` mappa, a `.gitignore` kihagyja).
