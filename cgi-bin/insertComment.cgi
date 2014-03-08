#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;

#Read GET parameters
my $oCGI = CGI->new();
my $nome = $oCGI->param('nome');
my $email = $oCGI->param('email');
my $lang = $oCGI->param('comment_lang');
my $id = $oCGI->param('element_id');
my $comment = $oCGI->param('comment_text');

my $fileXML = "../public_html/piatti.xml";
my $parser = XML::LibXML->new();
my $data = $parser->parse_file($fileXML);

my $root = $data->getDocumentElement || die("Non accedo alla radice");
my @piatti = $root->findnodes("//piatto[\@id=$id]");

#Answer
print "Content-Type: text/html\n\n";
print "nome $nome\n
email $email\n
lang $lang\n
id $id\n
comment $comment\n---";

print $piatti; #Dovrebbe stampare 0 o 1 ma non stampa nulla!
if ($piatti == 1) {
	$piatto = @piatti[0];
	print $piatto;
}