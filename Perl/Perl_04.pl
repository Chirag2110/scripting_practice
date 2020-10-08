#!/usr/bin/env perl

use 5.26.1;
use warnings;
use IO::File;

main(@ARGV);


#entry point
sub main
{
     my $filename = shift || "Perl_03.pl";
     my $count = countlines($filename);
     say "There are $count lines in $filename";
}

#count lines in $filename
sub countlines
{
     my $filename = shift;
     error("Countlines: missing filename") unless $filename;

     my $fh = IO::File->new($filename, 'r');

     my $count = 0;
     $count++ while($fh->getline);

     $fh->close;

     return $count;
}

sub error
{
    my $e = shift || 'unkown error';
    say "$0: $e";
    exit 0;
}

