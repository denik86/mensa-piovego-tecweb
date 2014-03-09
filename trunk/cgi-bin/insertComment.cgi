#!/usr/bin/perl -w

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use DateTime;

#Read GET parameters
my $oCGI = CGI->new();
my $nome = $oCGI->param('nome');
my $email = $oCGI->param('email');
my $lang = $oCGI->param('comment_lang');
my $id = $oCGI->param('element_id');
my $comment = $oCGI->param('comment_text');
if ($lang eq 'ENG') {
	$language = 'en';
} else {
	$language = 'it';
}

my $now = DateTime->now->ymd;
my $fileXML = "../public_html/piatti.xml";
my $parser = XML::LibXML->new();
my $data = $parser->parse_file($fileXML);

my $root = $data->getDocumentElement || die("Non accedo alla radice");
my @piatti = $root->findnodes("//piatto[\@id=$id]");

$numero = @piatti;
print $numero; 
if ($numero == 1) {
	$piatto = @piatti[0];
	$commentNode = $piatto->findnodes("commenti")->get_node(0);
	$newNode = "\n<commento lingua=\"$lang\">
	<autore>$nome</autore>
	<testo>$comment</testo>
	<data>$now</data>
	<email>$email</email>
	</commento>\n";
	$fragment = $parser->parse_balanced_chunk($newNode);
	$commentNode->appendChild($fragment);

	#serialize the three
	open (OUT, ">$fileXML");
	print OUT $data->toString;
	close (OUT);

	print "Content-Type: text/html\n\n";
	print "<meta http-equiv='refresh' content='0; url=./viewpiatto.cgi?id=$id&lang=$language' />";
} else {
	# TODO non si dovrebbe mai arrivare qui
}

#Answer
#print "Content-Type: text/html\n\n";
#print "nome $nome\n
#email $email\n
#lang $lang\n
#id $id\n
#date $now\n
#comment $comment\n";