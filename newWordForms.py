#!/usr/bin/python3
import re
import treetaggerwrapper
import os

def addStems(inputFile):
	# call TreeTagger
	# fiond stem of word
	# add it to the output file
	
	out_filepath = os.path.join('result_' + inputFile)
	tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
	i = 0
	with open(out_filepath, 'w', encoding="UTF-8") as output_file:
		with open(inputFile, 'r', encoding="UTF-8") as f:
			for line in f:
				for x in tagger.tag_text(line):
					text_word_per_line = '\n' + x
					output_file.write(text_word_per_line)
					i += 1
					if (i % 10):
						print (str(i))
	

if __name__=='__main__':
	import argparse
	import sys
	
	# working with arguments in the command line call
	# read fom file
	
	parser = argparse.ArgumentParser(description='get the input file containing the simple words')
	parser.add_argument('inputFile', type=str, help='the file containing the word to be used on the stemmer')
	
	if len(sys.argv) < 1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()
	addStems(args.inputFile)
	
	
	
	