#!/usr/bin/env python3
"""Reference solution: DNA FASTA -> sequential PHYLIP -> protein FASTA.

usage: python solutions/fasta2phylip2prot.py samples_files/genes.fasta out_prefix
"""
import re
import sys
from itertools import product

BASES = "TCAG"
AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON = {"".join(c): a for c, a in zip(product(BASES, repeat=3), AMINO)}


def read_fasta(path):
    seqs, name = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = []
        elif name and line:
            seqs[name].append(line)
    return {n: re.sub(r"[^A-Za-z]", "", "".join(p)).upper() for n, p in seqs.items()}


def short_names(names):
    """PHYLIP strict format: names are max 10 characters -> seq1, seq2 ... plus a mapping."""
    return {n: f"seq{i}" for i, n in enumerate(names, 1)}


def write_phylip(seqs, mapping, path):
    lengths = {len(s) for s in seqs.values()}
    assert len(lengths) == 1, f"sequences must have equal length, got {lengths}"
    with open(path, "w") as out:
        out.write(f" {len(seqs)} {lengths.pop()}\n")
        for n, s in seqs.items():
            out.write(f"{mapping[n]:<10}{s}\n")


def read_phylip(path):
    lines = open(path).read().splitlines()
    n, _ = map(int, lines[0].split())
    return {l[:10].strip(): l[10:].strip() for l in lines[1 : n + 1]}


def translate(dna):
    assert len(dna) % 3 == 0, "length is not a multiple of 3"
    return "".join(CODON.get(dna[i : i + 3], "X") for i in range(0, len(dna), 3))


def write_fasta(seqs, path, width=60):
    with open(path, "w") as out:
        for n, s in seqs.items():
            out.write(f">{n}\n")
            for i in range(0, len(s), width):
                out.write(s[i : i + width] + "\n")


if __name__ == "__main__":
    src, prefix = sys.argv[1], sys.argv[2]
    dna = read_fasta(src)
    mapping = short_names(dna)
    write_phylip(dna, mapping, prefix + ".phy")
    prot = {k: translate(v) for k, v in read_phylip(prefix + ".phy").items()}
    write_fasta(prot, prefix + "_prot.fasta")
    with open(prefix + "_names.tsv", "w") as out:
        for long, short in mapping.items():
            out.write(f"{short}\t{long}\n")
