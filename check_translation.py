from Bio.Seq import Seq
from Bio import SeqIO
from pathlib import Path

# Fájlok helye
base = Path("output") if Path("output/genes.phy").exists() else Path(".")

# PHYLIP beolvasása
with open(base / "genes.phy") as f:
    header = f.readline()
    dna_sequences = []

    for line in f:
        name = line[:10].strip()
        dna = line[10:].strip()
        dna_sequences.append((name, dna))

# Saját Perl-program eredménye
proteins = list(SeqIO.parse(base / "genes_prot.fasta", "fasta"))

# Összehasonlítás
for (name, dna), protein in zip(dna_sequences, proteins):

    biopython = str(Seq(dna).translate())
    perl = str(protein.seq)

    print("\nSzekvencia:", protein.id)

    if biopython == perl:
        print("EREDMÉNY: EGYEZIK")
    else:
        print("EREDMÉNY: ELTÉR")

        if "N" in dna:
            print("N karakter található a DNS-ben")

        if "*" in biopython or "*" in perl:
            print("Stop kodon található")

        print("Biopython:", biopython)
        print("Saját Perl:", perl)

        print("Biopython hossza:", len(biopython))
        print("Perl hossza:", len(perl))

if len(dna_sequences) != len(proteins):
    print("\nFIGYELEM: eltérő számú szekvencia!")
