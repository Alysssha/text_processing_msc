use strict;
use warnings;

my $AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG";

my @bases = split //, "TCAG";
my @amino = split //, $AMINO;

my %CODON;
my $i = 0;

for my $b1 (@bases) {
    for my $b2 (@bases) {
        for my $b3 (@bases) {
            my $codon = $b1 . $b2 . $b3;
            $CODON{$codon} = $amino[$i];
            $i++;
        }
    }
}

print "Kodonszam: ", scalar(keys %CODON), "\n";

for my $codon (qw(TTT ATG TAA TAG TGA GCT GGG)) {
    print "$codon -> $CODON{$codon}\n";
}
