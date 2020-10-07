#!/usr/bin/env perl

use warnings;
use 5.26.1;

my $filename = "Perl_01.pl";

open(FH, $filename);
my @lines = <FH>;
close(FH);

print FH;
my $count = scalar @lines;
say "There are $count lines in $filename";

print @lines;
print FH;


