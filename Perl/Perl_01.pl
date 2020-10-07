#!/usr/bin/env perl

use 5.18.0;
use warnings;

print("Hello World\n");
say "Hello, World";

#saclar declaration and usage
#my $x = 21; #my assigns a local scope to variable x
#say $x;

#an array declaration and usage
my @array = (1, 2, 3);
say foreach @array;
my $count = @array;
say "There are $count elements in an array.";

my ( $x, $y, $z ) = ( 1, 2, 3 );
say $x;
say $y;
say $z;
