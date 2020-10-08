#!/usr/bin/env perl

use 5.18.0;
use warnings;
use IO::File;

my $filename = "Perl_02.pl";

#open Perl_02.pl file

my $fh = IO::File->new($filename, 'r');

if (!$fh) {
   print("Can not open file $filename \n");
   exit;
   }

my $count =0;

while ($fh->getline){
   $count++;
   }

$fh->close;
say "Total Number of lines in $filename are $count";
