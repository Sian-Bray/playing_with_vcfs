#Finds sample names in a vcf and shortens them

import argparse
parser = argparse.ArgumentParser(description="Finds sample names in a vcf and shortens them")
parser.add_argument('-i', type=str, metavar='input_file', required=True, help='Path to the input .vcf file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .vcf file. The output file will be created in your current directory.')
parser.add_argument('-n', type=int, metavar='number_of_letters', default=[7], help='The number of letters in the new name, the script will take the first letters from the current name, i.e. 7 will turn "ALO_006_other_stuff_bla_bla" into "ALO_006"')
args = parser.parse_args()

#Count lines in the input file
input_file=open(args.i, 'r')
input_length=len(input_file.readlines())
input_file.close

#Open the input and create the output
input_file=open(args.i, 'r')
output_file=open(args.o, 'w+')

line_count=0

#Work through the lines, reprinting unless they contain "#CHROM"
while input_length > line_count:
	current_line=input_file.readline()
	if "#CHROM" not in current_line:
		output_file.write(current_line)
	if "#CHROM" in current_line:
		headder=current_line.split('\t')
		headder_lenght=len(headder)
		#In my .vcfs the population names start at column 10
		index_count=0
		while index_count < 9:
			output_file.write(headder[index_count]+'\t')
			index_count+=1
		while index_count < headder_lenght-1:
			individual=headder[index_count]
			output_file.write(individual[slice(7)]+'\t')
			index_count+=1
		individual=headder[index_count]
		output_file.write(individual[slice(7)]+'\n')
	line_count+=1