use strict;
use warnings;

# Kodontábla
my $AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG";

my @bases = split //, "TCAG";
my @amino = split //, $AMINO;

my %CODON;
my $i = 0;

for my $b1 (@bases) {
    for my $b2 (@bases) {
        for my $b3 (@bases) {
            my $codon = $b1 . $b2 . $b3;
            $CODON{$codon} = $amino[$i++];
        }
    }
}

# Eredeti nevek beolvasása
my %names;

open(my $nf, "<", "samples_files/names.tsv") or die $!;

while (my $line = <$nf>) {
    chomp $line;
    my ($short, $original) = split /\t/, $line;
    $names{$short} = $original;
}

close($nf);

# PHYLIP beolvasása
open(my $fh, "<", "output/genes.phy") or die $!;

my $header = <$fh>;

open(my $out, ">", "output/genes_prot.fasta") or die $!;

while (my $line = <$fh>) {
    chomp $line;

    my $short = substr($line, 0, 10);
    $short =~ s/^\s+|\s+$//g;

    my $seq = substr($line, 10);

    my $original = $names{$short} // $short;

    my $protein = "";

    # Transzláció
    for (my $j = 0; $j + 2 < length($seq); $j += 3) {
        my $codon = substr($seq, $j, 3);

        my $aa;

        if ($codon =~ /N/) {
            $aa = "X";
        } else {
            $aa = $CODON{$codon} // "X";
        }

        $protein .= $aa;
    }

    # FASTA fejléc
    print $out ">$original\n";

    # 60 karakteres sorokra tördelés
    for (my $j = 0; $j < length($protein); $j += 60) {
        print $out substr($protein, $j, 60), "\n";
    }
}

close($fh);
close($out);

print "Elkeszult: output/genes_prot.fasta\n";
